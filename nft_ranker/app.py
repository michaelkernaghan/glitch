#!/usr/bin/env python3
"""
NFT Ranking Web App
Compare two random NFTs side-by-side and build a ranking over time
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import json
import random
from pathlib import Path

app = Flask(__name__)

# Paths
NFT_DIRS = [
    '../my_nft_collection/tezos',
    '../my_nft_collection/evm',
    '../imported_images',
]

RANKINGS_FILE = 'rankings.json'


def is_valid_image_file(file_path):
    """Check if file is actually a valid image/video"""
    import subprocess
    
    try:
        # Use 'file' command to check actual file type
        result = subprocess.run(
            ['file', '--mime-type', '-b', str(file_path)],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        mime_type = result.stdout.strip()
        
        # Valid types
        valid_types = [
            'image/png', 'image/jpeg', 'image/gif', 'image/webp',
            'video/mp4', 'video/quicktime', 'video/webm'
        ]
        
        is_valid = any(valid in mime_type for valid in valid_types)
        
        if not is_valid:
            print(f"⚠️  Skipping corrupted: {file_path.name} (type: {mime_type})")
        
        return is_valid
        
    except Exception as e:
        # If check fails, assume it's valid
        return True


def get_all_nfts():
    """Get list of all NFT image files (excluding corrupted)"""
    nfts = []
    
    base_path = Path(__file__).parent.parent
    
    for nft_dir in NFT_DIRS:
        path = Path(__file__).parent / nft_dir
        if path.exists():
            for file in path.glob('*'):
                if file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.mp4', '.webm', '.mov']:
                    # Check if actually valid
                    if is_valid_image_file(file):
                        relative = str(file.relative_to(base_path))
                        nfts.append({
                            'path': str(file),
                            'name': file.name,  # Full filename with extension
                            'relative_path': relative
                        })
    
    print(f"✅ Found {len(nfts)} valid NFTs (corrupted files filtered out)")
    return nfts


def load_rankings():
    """Load current rankings"""
    rankings_path = Path(__file__).parent / RANKINGS_FILE
    
    if rankings_path.exists():
        with open(rankings_path, 'r') as f:
            existing = json.load(f)
            
            # Add any new NFTs that weren't in rankings yet
            current_nfts = get_all_nfts()
            for nft in current_nfts:
                if nft['name'] not in existing:
                    existing[nft['name']] = {
                        'name': nft['name'],
                        'path': nft['relative_path'],
                        'elo': 1500,
                        'wins': 0,
                        'losses': 0,
                        'comparisons': 0
                    }
            
            return existing
    
    # Initialize with ELO ratings
    nfts = get_all_nfts()
    rankings = {}
    
    for nft in nfts:
        rankings[nft['name']] = {
            'name': nft['name'],
            'path': nft['relative_path'],
            'elo': 1500,  # Starting ELO rating
            'wins': 0,
            'losses': 0,
            'comparisons': 0
        }
    
    return rankings


def save_rankings(rankings):
    """Save rankings to file"""
    rankings_path = Path(__file__).parent / RANKINGS_FILE
    with open(rankings_path, 'w') as f:
        json.dump(rankings, f, indent=2)


def calculate_new_elo(winner_elo, loser_elo, k=32):
    """Calculate new ELO ratings after a match"""
    # Expected scores
    expected_winner = 1 / (1 + 10 ** ((loser_elo - winner_elo) / 400))
    expected_loser = 1 / (1 + 10 ** ((winner_elo - loser_elo) / 400))
    
    # New ratings
    new_winner_elo = winner_elo + k * (1 - expected_winner)
    new_loser_elo = loser_elo + k * (0 - expected_loser)
    
    return new_winner_elo, new_loser_elo


@app.route('/')
def index():
    """Main ranking page"""
    return render_template('index.html')


@app.route('/api/random-pair')
def get_random_pair():
    """Get two random NFTs to compare"""
    from urllib.parse import quote
    
    nfts = get_all_nfts()
    
    if len(nfts) < 2:
        return jsonify({'error': 'Not enough NFTs'}), 400
    
    pair = random.sample(nfts, 2)
    
    # URL encode the paths properly
    return jsonify({
        'nft1': {
            'name': pair[0]['name'],
            'path': '/nft/' + quote(pair[0]['relative_path'])
        },
        'nft2': {
            'name': pair[1]['name'],
            'path': '/nft/' + quote(pair[1]['relative_path'])
        }
    })


@app.route('/api/vote', methods=['POST'])
def record_vote():
    """Record a vote and update rankings"""
    data = request.json
    winner_name = data.get('winner')
    loser_name = data.get('loser')
    
    if not winner_name or not loser_name:
        return jsonify({'error': 'Missing winner or loser'}), 400
    
    rankings = load_rankings()
    
    # Get current ELO ratings
    winner_elo = rankings[winner_name]['elo']
    loser_elo = rankings[loser_name]['elo']
    
    # Calculate new ratings
    new_winner_elo, new_loser_elo = calculate_new_elo(winner_elo, loser_elo)
    
    # Update rankings
    rankings[winner_name]['elo'] = new_winner_elo
    rankings[winner_name]['wins'] += 1
    rankings[winner_name]['comparisons'] += 1
    
    rankings[loser_name]['elo'] = new_loser_elo
    rankings[loser_name]['losses'] += 1
    rankings[loser_name]['comparisons'] += 1
    
    save_rankings(rankings)
    
    return jsonify({
        'success': True,
        'winner_new_elo': round(new_winner_elo),
        'loser_new_elo': round(new_loser_elo)
    })


@app.route('/api/rankings')
def get_rankings():
    """Get full rankings sorted by ELO"""
    rankings = load_rankings()
    
    # Sort by ELO
    sorted_rankings = sorted(
        rankings.values(),
        key=lambda x: x['elo'],
        reverse=True
    )
    
    return jsonify(sorted_rankings)


@app.route('/api/stats')
def get_stats():
    """Get statistics"""
    rankings = load_rankings()
    
    total_comparisons = sum(r['comparisons'] for r in rankings.values()) // 2
    total_nfts = len(rankings)
    
    # Get top 5 and bottom 5
    sorted_rankings = sorted(rankings.values(), key=lambda x: x['elo'], reverse=True)
    
    return jsonify({
        'total_nfts': total_nfts,
        'total_comparisons': total_comparisons,
        'top_5': sorted_rankings[:5],
        'bottom_5': sorted_rankings[-5:] if len(sorted_rankings) >= 5 else []
    })


@app.route('/nft/<path:filename>')
def serve_nft(filename):
    """Serve NFT images"""
    from urllib.parse import unquote
    
    base_dir = Path(__file__).parent.parent
    # Decode URL-encoded filename
    decoded_filename = unquote(filename)
    full_path = base_dir / decoded_filename
    
    print(f"📥 Request: {filename}")
    print(f"   Decoded: {decoded_filename}")
    print(f"   Full path: {full_path}")
    print(f"   Exists: {full_path.exists()}")
    
    try:
        if not full_path.exists():
            print(f"   ❌ File not found!")
            return "File not found", 404
        
        return send_from_directory(base_dir, decoded_filename)
    except Exception as e:
        print(f"   ❌ Error serving: {e}")
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎨 NFT RANKING WEB APP")
    print("="*70)
    print("\nStarting server...")
    print("Open in browser: http://localhost:5000")
    print("\nPress Ctrl+C to stop")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)


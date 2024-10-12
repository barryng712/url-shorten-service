from flask import Blueprint, request, jsonify
from .models import URL
from . import db
import random
import string
from .utils import is_valid_url
from datetime import datetime

url_shortener_bp = Blueprint("shorten", __name__)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def generate_unique_url(url):
    while True:
        url = generate_short_url()
        if not db.session.query(URL).filter_by(shortCode=url).first():
            return url
        
def get_url_item(short_code):
    return URL.query.filter(URL.shortCode == short_code).first_or_404()

@url_shortener_bp.route('/', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'message': 'you must provide a url field'}), 400
    
    url = data.get('url')
    if not is_valid_url(url):
        return jsonify({'message': 'invalid url format'}), 400 
    short_code = generate_unique_url(url)
    new_url = URL(url=url, shortCode=short_code)
    db.session.add(new_url)
    db.session.commit()
    item = get_url_item(short_code)
    return jsonify({
        'id':item.id,
        'url':item.url,
        'shortCode':item.shortCode,
        'createdAt':item.createdAt,
        'updatedAt':item.updatedAt
    }), 201

@url_shortener_bp.route('/shorten/<short_code>', methods=['GET'])
def retrieve_url(short_code):
    item = get_url_item(short_code)
    if not item:
        return jsonify({'message': 'url not found'}), 404
    item.accessCount += 1
    db.session.commit()
    return jsonify({
        'id':item.id,
        'url':item.url,
        'shortCode':item.shortCode,
        'createdAt':item.createdAt,
        'updatedAt':item.updatedAt
    }), 200

@url_shortener_bp.route('/shorten/<short_code>', methods=['PUT'])
def update_url(short_code):
    data=request.get_json()
    item = get_url_item(short_code)
    if not item:
        return jsonify({'message': 'url not found'}), 404
    item.url = data.get('new_url')
    db.session.commit()
    return jsonify({
        'id':item.id,
        'url':item.url,
        'shortCode':item.shortCode,
        'createdAt':item.createdAt,
        'updatedAt':datetime.now()
    }), 200

@url_shortener_bp.route('/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    item = get_url_item(short_code)
    if not item:
        return jsonify({'message': 'url not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message':'deleted successfully'}), 204

@url_shortener_bp.route('/shorten/<shortcode>/stats', methods=['GET'])
def get_stats(short_code):
    item=get_url_item(short_code)
    if not item:
        return jsonify({'message': 'url not found'}), 404
    return jsonify({
        'id':item.id,
        'url':item.url,
        'shortCode':item.shortCode,
        'createdAt':item.createdAt,
        'updatedAt':item.updatedAt,
        'accessCount': item.accessCount
    }), 200
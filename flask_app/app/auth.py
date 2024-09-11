from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "用户名和密码不能为空"}), 400

    hashed_password = generate_password_hash(password)
    
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
    except:
        return jsonify({"error": "用户名已存在"}), 400
    finally:
        conn.close()
        
    return jsonify({"message": "注册成功"}), 201

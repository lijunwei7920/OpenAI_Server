from flask import Blueprint, jsonify

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": "这是一些示例数据"})

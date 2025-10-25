from flask import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)

# Health check
@main_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'})

# Example API endpoint
@main_bp.route('/deploy', methods=['POST'])
def deploy():
    data = request.get_json()
    app_name = data.get('app_name', 'Unknown')
    
    # Here you could trigger CI/CD scripts or shell commands
    # Example: logging.info(fDeploying {app_name})
    
    return jsonify({'message': f'Deployment triggered for {app_name}'}), 202


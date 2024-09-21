import logging

def init_logging(app):
    logging.basicConfig(filename='app.log', level=logging.INFO)
    app.logger.info('App startup')

def format_response(data):
    """Helper function to format responses."""
    return {'status': 'success', 'data': data}

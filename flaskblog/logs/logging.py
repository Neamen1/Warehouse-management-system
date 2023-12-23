from datetime import datetime
from flaskblog import logger_db


def log_to_couchdb(message):
    timestamp = datetime.utcnow().timestamp()
    date_str = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    # Check if a document for the date already exists
    doc_id = f"logs_{date_str}"
    log_document = logger_db.get(doc_id)

    if log_document:
        # If the document exists, append the log entry to the existing logs
        log_document['logs'].append({'timestamp': timestamp, 'message': message})
        logger_db.save(log_document)
    else:
        # If the document doesn't exist, create a new one with the log entry
        new_log_document = {
            '_id': doc_id,
            'date': date_str,
            'logs': [{'timestamp': timestamp, 'message': message}]
        }
        logger_db.save(new_log_document)

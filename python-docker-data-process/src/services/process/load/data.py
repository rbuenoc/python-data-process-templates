from common.logging import log_info
from services.mongodb import insert_many, delete_all


def load_data(payload):
    log_info(payload, name='entity-get')
    #delete_all()
    #result_insert = insert_many(payload)
    #log_info(str(len(result_insert.inserted_ids)) + ' documents inserted.')

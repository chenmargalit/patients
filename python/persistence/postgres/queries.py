from .connection import cur
from utils.static_messages import FETCH_QUERY_FAILED, RECORD_INSERTED_SUCCESSFULLY, UNABLE_TO_INSERT_RECORD

def fetch_record(table, identifier_type, identifier_value):
    try:
        SQL = f'SELECT {identifier_type} FROM {table} where {identifier_type} = {identifier_value}'
        cur.execute(SQL)
        res = cur.fetchone()
        return {'err': False, 'msg': res[0] if res else None} 
    except Exception:
        return {'err': True, 'msg': FETCH_QUERY_FAILED}

def insert_to_patients_table(value: int):
    try:
        SQL = 'INSERT INTO patients_details(patient_id) VALUES(%s)'
        data = value
        cur.execute(SQL, (data,))
        return {'err': False, 'msg': RECORD_INSERTED_SUCCESSFULLY}
    except Exception:
        return {'err': True, 'msg': UNABLE_TO_INSERT_RECORD}



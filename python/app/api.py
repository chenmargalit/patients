import pandas as pd
from fastapi import APIRouter, Response
from persistence.postgres.queries import fetch_record, insert_to_patients_table
from utils.df_utils import get_random_code
from utils.static_messages import UNEXPECTED_ERROR, BAD_VALUE
from utils.validation import validate_inp

router = APIRouter()

df = pd.read_csv('./data/data.csv')

@router.get("/inference")
async def root(patientId: int, text: str, response: Response) -> Response:
    try:
        is_id_valid = validate_inp(patientId, int)
        is_text_valid = validate_inp(text, str)
        if not is_id_valid or not is_text_valid: 
            raise ValueError

        code = get_random_code(df)

        does_patient_exist = fetch_record('patients_details', 'patient_id', patientId)
        if does_patient_exist['err']:
            raise Exception

        if not does_patient_exist['msg']:
            insert_res = insert_to_patients_table(patientId)
            if insert_res['err']:
                raise Exception

        return {'id': patientId, 'text': text, 'code': code, 'is_new_patient':
        False if does_patient_exist['msg'] else True}

    except ValueError:
        response.status_code = 400
        return BAD_VALUE

    except Exception:
        response.status_code = 500
        return UNEXPECTED_ERROR



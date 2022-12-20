from pandas import DataFrame
import random

def get_random_code(df: DataFrame) -> int:
    random_num = random.randint(0, len(df))
    return df.code[random_num]
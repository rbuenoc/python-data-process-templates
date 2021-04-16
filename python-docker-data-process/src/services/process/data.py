from .extract import extract_data
from .transform import transform_data
from .load import load_data


def process_data():
    extracted_data = extract_data()
    transformed_data = transform_data(extracted_data)
    load_data(transformed_data)

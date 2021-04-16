from common.tools.json import deserialize_json

def transform_data(data_df):
    payload = data_df.to_dict('records')
    return payload

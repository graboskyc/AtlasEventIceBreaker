import pymongo
import io
import boto3
from bson.json_util import loads

def main(event, context):
    csURI = event['csURI']
    dsURI = event['dsURI']
    db = event['db']
    col = event['col']
    bucket = event['bucket']
    fn = event['fn']
    conn = pymongo.MongoClient(csURI)

    data_stream = io.BytesIO()
    s3 = boto3.resource('s3')
    s3.meta.client.download_fileobj(bucket,  fn, data_stream)
    data_stream.seek(0)

    a = []
    for line in data_stream.readlines():
        a.append(loads(line.decode('utf8')))

    conn[db][col].insert_many(a)


from base64 import b64encode
import traceback
import sys
import boto3
import datetime


def write(*args, stream=sys.stdout):
    for a in args:
        if isinstance(a, Exception):
            traceback.print_exception(type(a), a, a.__traceback__, file=stream)
            stream.flush()
        else:
            print(a, file=stream, flush=True)


def info(*args):
    write(*args, stream=sys.stdout)


def error(*args):
    write(*args, stream=sys.stderr)


def fatal(*args):
    error(*args)
    sys.exit(1)


def metric(metric, namespace, dimensions, value):
    client = boto3.client('cloudwatch', 'us-west-2')
    client.put_metric_data(
        Namespace=namespace,
        MetricData=[{
            'MetricName': metric,
            'Dimensions': dimensions,
            'Timestamp': datetime.datetime.utcnow(),
            'Value': value
        }]
    )


def metadata_fill(metadata, status, rows=0, e=None):
    exception = ''.join(traceback.format_exception(type(e), e, e.__traceback__)) if e else None
    metadata['END_TIME'] = datetime.datetime.utcnow()
    metadata['RUN_TIME'] = metadata['END_TIME'] - metadata['START_TIME']
    metadata['ROWS'] = rows
    metadata['STATUS'] = status
    metadata['EXCEPTION'] = b64encode(exception.encode()).decode() if e else None
    metadata['START_TIME'] = str(metadata['START_TIME'])  # This is mildly gross, but we record them as
    metadata['END_TIME'] = str(metadata['END_TIME'])      # datetime objects so we can do math on them, then
    metadata['RUN_TIME'] = str(metadata['RUN_TIME'])      # convert to string so we can json serialize.

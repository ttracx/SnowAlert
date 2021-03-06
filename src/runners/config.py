import os

from runners.helpers.dbconfig import DATABASE

# schema names
DATA_SCHEMA_NAME = os.environ.get('SA_DATA_SCHEMA_NAME', "data")
RULES_SCHEMA_NAME = os.environ.get('SA_RULES_SCHEMA_NAME', "rules")
RESULTS_SCHEMA_NAME = os.environ.get('SA_RESULTS_SCHEMA_NAME', "results")

# table names
RESULTS_ALERTS_TABLE_NAME = os.environ.get('SA_RESULTS_ALERTS_TABLE_NAME', "alerts")
RESULTS_VIOLATIONS_TABLE_NAME = os.environ.get('SA_RESULTS_VIOLATIONS_TABLE_NAME', "violations")
RESULTS_METADATA_TABLE_NAME = os.environ.get('SA_METADATA_TABLE_NAME', "metadata")

# schemas
DATA_SCHEMA = os.environ.get('SA_DATA_SCHEMA', f"{DATABASE}.{DATA_SCHEMA_NAME}")
RULES_SCHEMA = os.environ.get('SA_RULES_SCHEMA', f"{DATABASE}.{RULES_SCHEMA_NAME}")
RESULTS_SCHEMA = os.environ.get('SA_RESULTS_SCHEMA', f"{DATABASE}.{RESULTS_SCHEMA_NAME}")

# tables
ALERTS_TABLE = os.environ.get('SA_ALERTS_TABLE', f"{RESULTS_SCHEMA}.{RESULTS_ALERTS_TABLE_NAME}")
VIOLATIONS_TABLE = os.environ.get('SA_VIOLATIONS_TABLE', f"{RESULTS_SCHEMA}.{RESULTS_VIOLATIONS_TABLE_NAME}")
METADATA_TABLE = os.environ.get('SA_METADATA_TABLE', f"{RESULTS_SCHEMA}.{RESULTS_METADATA_TABLE_NAME}")

# misc
ALERT_QUERY_POSTFIX = "alert_query"
ALERT_SQUELCH_POSTFIX = "alert_suppression"
VIOLATION_QUERY_POSTFIX = "violation_query"
VIOLATION_SQUELCH_POSTFIX = "violation_suppression"

# enabling sends metrics to cloudwatch
CLOUDWATCH_METRICS = os.environ.get('CLOUDWATCH_METRICS', False)

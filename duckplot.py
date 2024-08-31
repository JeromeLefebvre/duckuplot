import subprocess
import duckdb
from io import StringIO

sample = """curl -sL https://git.io/AirPassengers \
| cut -f2,3 -d, \
| uplot line -d, -w 50 -h 15 -t AirPassengers --xlim 1950,1960 --ylim 0,600"""

output = subprocess.run(sample, shell=True, check=True, text=True, capture_output=True)

for line in output.stderr.split('\n'):
    print(line)

db = duckdb.connect()

values = db.sql('''
copy (
    select time, value from read_csv('https://git.io/AirPassengers')
) TO '/dev/stdout' WITH (FORMAT 'csv', header false);''').to_csv()

values = db.sql('''select time, value from read_csv('https://git.io/AirPassengers')''').to_df()


csv_data = StringIO()
values.to_csv(csv_data, index=False)
csv_data.seek(0)  # Go back to the start of the StringIO object

sample = """cut -f2,3 -d, \
| uplot line -d, -w 50 -h 15 -t AirPassengers --xlim 1950,1960 --ylim 0,600"""

output = subprocess.run(sample, stderr=csv_data.getvalue(), text=True, capture_output=True, shell=True)

for line in output.stdout.split('\n'):
    print(line)


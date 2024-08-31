import subprocess
from io import StringIO

# Example CSV data as a string
csv_data = """Year,Passengers
1949,112
1950,118
1951,132
1952,129
1953,121
1954,135
1955,148
1956,148
1957,136
1958,119
1959,104
1960,118
"""

# Command 1: `cut -f2,3 -d,` (Cut columns 2 and 3)
cut_command = ["cut", "-f2,3", "-d,"]

# Command 2: `uplot line -d, -w 50 -h 15 -t AirPassengers --xlim 1950,1960 --ylim 0,600`
uplot_command = [
    "uplot", "line", "-d,", "-w", "50", "-h", "15", "-t", "AirPassengers",
    "--xlim", "1950,1960", "--ylim", "0,600"
]

#print(csv_data)
print(csv_data.encode())

# Open the first process (cut) with subprocess, and pipe its output to the next process (uplot)
with subprocess.Popen(cut_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as cut_proc:
    # Pass the output of the cut process to the next command using PIPE
    # Write the CSV data to the stdin of the cut process
    cut_proc.stdin.write(csv_data.encode())
    cut_proc.stdin.close()  # Close the stdin after writing the data
    #print(cut_proc.stdout.readlines())
    with subprocess.Popen(uplot_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as uplot_proc:
        uplot_proc.stdin.write(csv_data.encode())
        uplot_proc.stdin.close()
        # Get the output from the uplot process
        uplot_output = uplot_proc.communicate()[0]

# Print the output from the uplot command
print(uplot_output.decode())

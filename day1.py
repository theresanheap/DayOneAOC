import re
import sys

file_path = "day1.txt"
results = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            temp = re.findall(r'\d+', line)
            resfirst = [int(seq[0]) for seq in temp]
            reslast = [int(seq[-1]) for seq in temp]
            x = str(resfirst[0])
            y = str(reslast[-1])
            z = x+y
            
            if z:
                results.append(int(z))
                
            else:
                print(f"No digits found in the line: {line.strip()}")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    sys.exit()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit()

print(sum(results))
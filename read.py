def splits(string):
    array = []
    substring = ''
    for i in string:
        if (i != ";"):
            substring += i
        else:
            array.append(substring)
            substring = ''
    array.append(substring)
    return array

def convert_line_to_data(line):
  raw_array_of_data = splits(line)
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data

def convert_data_to_value(array_data):
    copy_array = array_data
    for i in range(3):
        if(i == 0):
            copy_array[i] = int(copy_array[i])
        if(i == 2):
            copy_array[i] = float(copy_array[i])
    return copy_array

with open('hai.csv','r') as f:
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)
    print(header)

    raw_lines = f.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

    for line in lines:
      array_of_data = convert_line_to_data(line)
      print(array_of_data)




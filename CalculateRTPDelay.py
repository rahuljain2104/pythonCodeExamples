dn_file_path = "D:\codes\datasets\\temp\MO3_rtp_dn.txt"
up_file_path = "D:\codes\datasets\\temp\MO3_rtp_up.txt"

dn_file = open(dn_file_path)
dn_file_lines = dn_file.readlines()

up_file = open(up_file_path)
up_file_lines = up_file.readlines()

if len(dn_file_lines) >= len(up_file_lines):
    file1 = dn_file_lines
    file2 = up_file_lines
else:
    file2 = dn_file_lines
    file1 = up_file_lines

delay_array = []
j = 0
count = 0
try:
    for i in range(len(file1)):
        packet1 = (file1[i].split('\t')[1].strip())
        packet2 = (file2[j].split('\t')[1].strip())
        delay1 = float(file1[i].split('\t')[0].strip())
        delay2 = float(file2[j].split('\t')[0].strip())

        if packet1 == packet2:
            delay_array.append(abs(delay1 - delay2))
            j += 1
            count += 1
        if packet1 > packet2:
            j += 2
        if packet1 < packet2:
            i += 1

except Exception:
    print("")

average = (sum(delay_array) / count)
delay_array.sort()
index = int(count * 0.95)
per95_val = delay_array[index]

print(average)
print(per95_val)

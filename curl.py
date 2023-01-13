import subprocess

start = 2000001
end = 2074446

with open("raw_data.txt", "w") as file:
    for sbd in range(start, end):
        command = 'curl -F "SoBaoDanh=0' + str(sbd) + '" + diemthi.hcm.edu.vn/Home/Show'
        result = subprocess.check_output(command)
        file.write(str(result) + "\n")
import subprocess
import sys

img_path = sys.argv[1]
yolo_command = "./darknet detector test yolo-display-petrobras/data/display.data yolo-display-petrobras/cfg/yolov3.cfg backup/yolov3_6000.weights -dont_show "+img_path
process = subprocess.Popen(yolo_command.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
output, error = process.communicate()

# Yolo result post processing
number_value = lambda string_search, string_val : string_search[string_search.find(string_val)+len(string_val)]
signal_value = lambda string_search: "-" if string_search.find("sinal_apenas")!=-1 else ("-1" if string_search.find("sinal_e_um")!=-1 else ("" if string_search.find("sinal_zero") else "1"))

sup_esq_value = number_value(output.decode('ascii'), "sup_esq_")
sup_dir_value = number_value(output.decode('ascii'), "sup_dir_")
inf_dir_value = number_value(output.decode('ascii'), "inf_dir_")
inf_esq_value = signal_value(output.decode('ascii'))

superior_value = sup_esq_value+sup_dir_value+"%"
inferior_value = inf_esq_value+inf_dir_value+"%"

print(superior_value)
print(inferior_value)

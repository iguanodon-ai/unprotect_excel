import os, sys, re

REGEX = "<sheetProtection.+?>"

input_d = sys.argv[1]
os.system(f"unzip {input_d}/* -d {input_d}")	
sheets = [os.path.join(input_d, "xl/worksheets", file) for file in os.listdir(os.path.join(input_d, "xl/worksheets")) if file.endswith(".xml")]


def unprotect_sheet(sheet):
	print(sheet)
	with open(sheet) as f:
		t = f.read()
	#print(len(t))
	t = re.sub(REGEX, "", t)
	#print(len(t))
	os.remove(sheet)
	if len(t) > 0:
		with open(sheet, "w") as f:
			f.write(t)

	
for sheet in sheets:
	unprotect_sheet(sheet)

os.system(f"cd {input_d} &&  zip -r new_excel.zip . && mv new_excel.zip ../new_excel.xlsx")

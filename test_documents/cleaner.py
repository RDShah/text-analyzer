with open('graduation_raw.txt') as rfile:
	with open('graduation.txt','w') as wfile:
		for line in rfile:
			if line == '\n': continue
			if '[' not in line:
				wfile.write(line)
			elif ']' in line:
				wfile.write(line[:line.index('[')])
				wfile.write(line[line.index(']')+1:])
		wfile.close()

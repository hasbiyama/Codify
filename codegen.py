from srcode import *
import folder_create
import generate_code
import file_create_add


def codeGen():

	folder_create.Folder.createFolder() # module

	os.chdir("../data") # new current dir

def inputPart():


	# INPUT USER


	inp0 = input("\n\t[?] What's the username you wanna add? ->  ").lower()
	print("")

	
	if inp0 == "":

		print(colored("\n\t[x] Please input the name!", 'red', attrs=['bold']))
		
		sys.exit()

	
	with open(uD1, 'r') as f:

		fp = str(f.readlines())
	
		newF = fp.strip()
			
		for ln in newF:
			
			if re.search(r"\bCode: {}\b".format(str(inp0)), newF):

				time.sleep(1)

				print(colored("\t[!] User '" + inp0 + "' already exists in " + uD1, 'yellow', attrs=['bold']))
				
				time.sleep(1)

				sys.exit()

			else: pass

	
	print(colored("\t[*] Adding " + inp0 + " to " + uD0 + "... ", 'cyan', attrs=['bold']))
	
	file_create_add.Attributes(uD0, inp0, 1, 2, 3, "Added at: ").createFile() 

	time.sleep(2)

	print("\t++++++++++++++++++++++++++++++++++++++++")
	print(colored("\t[+] User " + inp0 + " has been added!", 'green', attrs=['bold']))
	print("\t++++++++++++++++++++++++++++++++++++++++\n")

	generate_code.Generator.reGen(inp=inp0)

if __name__ == '__main__':
	codeGen()
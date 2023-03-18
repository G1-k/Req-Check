import sys

dataset_csv_path = 'datasets/forbidden_words_dataset.csv'

def prRed(text): 
	print("\033[91m {}\033[00m" .format(text))
 
def prGreen(text): 
	print("\033[92m {}\033[00m" .format(text))
  
def prYellow(text): 
	print("\033[93m {}\033[00m" .format(text))

def load_forbidden_words():

	forbidden_words_list=[]
	lang_file = open(dataset_csv_path,'rb')
	for word in lang_file:
		forbidden_words_list.append(str(word,'utf-8').strip())
	return forbidden_words_list

def load_file(filename):
	file=open(filename,'rb')
	return file


def SSDVS_Checker(filename):

	# filename = sys.argv[1]
	print ('Input File Name : '+filename)
	try:
		input_file = load_file(filename)
		req = ''
		line_count=1
		for i in input_file:
			req += str(line_count)+'| '+str(i,'utf-8')
			line_count+=1
		print ('\n')
		print ('----------------- Requirement -----------------')
		print (req)
		print ('--------------------------------------------\n')
	except Exception as e:
		print ('Error Occured while loading text file. Error : ' + str(e))
	finally:
		input_file.close()


	forbidden_words = load_forbidden_words()


	req_list = req.split('\n')


	print ('\n')
	print ('----------------- Output -----------------')

	is_found = False
	found_forbidden_list = []
	for sentence in req_list:
		line_number = sentence[0:1:1]
		found_forbidden_list=[i for i in sentence.lower().split() if i in forbidden_words]
		if found_forbidden_list == []:
			continue
		else:
			prRed ('-- '+str(len(found_forbidden_list))+' Forbidden Words found at line number : '+line_number+' --')
			x_words=''
			for i in found_forbidden_list:
				x_words+=i+', '
			prRed ('Forbidden Words : '+x_words[:-2])
			is_found = True

	print('\n')
	if not is_found:
		prGreen("Requirement Check Passed!")
	else:
		prRed("Requirement Check Failed!")

	print ('--------------------------------------------\n')

	return (is_found, found_forbidden_list)
import docx
import json
# from itertools import tee


# fp = "../sample-files/Camila Ferezin do Amarante ( Ginastica ritmica ).docx"
# Convert .docx file to a list of paragraph strings
# Removes empty strings
def docxToStrings(fp):
	txt = [para.text for para in docx.Document(fp).paragraphs]
	return list(filter(None, txt))

# Separate bold paragraphs from non-bold paragraphs
# Consecutive bold or nonbold paragraphs are treated as one element
# 	So, they are concatenated into one string, separated by '\n'
def docxToStringsSepBold(fp):
	bold, nonbold = [], []
	doc = docx.Document(fp)
	start=0

	# Get first element and append
	prev = None
	for n, paragraph in enumerate(doc.paragraphs):
		for run in paragraph.runs:
			if run.bold:
				bold.append(run.text)
			else:
				nonbold.append(run.text)
			prev = run
			start = n
			break

	# Get remaining elements
	# In each iteration, compare with previous element for bold/nonbold match
	# If mathing, join the two paragraphs into one strings
	# Else, append as usual
	for n, paragraph in enumerate(doc.paragraphs, start+1):
		for run in paragraph.runs:
			if run.bold and prev.bold:
				"\n".join([bold[-1], run.text])
			elif run.bold:
				bold.append(run.text)
			elif not(run.bold or prev.bold):
				"\n".join([nonbold[-1], run.text])
			else:
				nonbold.append(run.text)
			prev = run
	return bold, nonbold

if __name__ == '__main__':
	fp = input("Type the filepath to the .docx: ")
	jdoc = {}
	jdoc["text"] = docxToStrings(fp)
	jdoc["bold"], jdoc["nonbold"] = docxToStringsSepBold(fp)

	with open(fp.replace(".docx", ".json"), "w+") as f:
		json.dump(jdoc, f, ensure_ascii=False, indent=4)
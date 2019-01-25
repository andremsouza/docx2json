# docx-to-json
Python script that converts text from a .docx file into .json format.

## Usage:
The user must type the relative or absolute path to the desired .docx file.

## Output:
The script will then convert all text from the .docx to a .json file with the same name, at the same directory as the input file. The structure of the output JSON is as follows:
```json
{
	"text": ["A list of strings containing all paragraphs from the input file.", "..."],
	"bold": ["A list of strings containing all paragraphs that start with bold characters.", "..."],
	"nonbold": ["A list of strings containing all paragraphs that start with non-bold characters.", "..."]
}
```


## API Reference:
* [python-docx](https://github.com/python-openxml/python-docx "python-docx")
* [json](https://docs.python.org/3/library/json.html "python-json")

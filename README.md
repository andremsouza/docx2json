# docx2json
Python script that converts text from a .docx file into .json format.

# Installation
```bash
pip3 install docx2json
```

## Usage:
If using as one python script, the user must type the relative or absolute path to the desired .docx file.

If using as a class, the user may choose one of the public methods to convert as desired.

Method for conversion:
```python
import docx2json
# Converts .docx file situated in the inputFile string path
# if sepBold==True
#	separates paragraphs starting or not with bold characters into two lists: "bold", "nonbold"
# if withSave==True
# 	saves output file to outputFile filepath, with default value being at the same location as the input file inputFile
# returns a json variable
convert(inputFile, sepBold=True, withSave=False, outputFile=None)
```

## Output:
The script will then convert all text from the .docx to a .json file with the same name, at the same directory as the input file. The structure of the output JSON is as follows:
```json
{
	"text": ["A list of strings containing all paragraphs from the input file.", "..."],
	"bold": ["A list of strings containing all paragraphs that start with bold characters.", "..."],
	"nonbold": ["A list of strings containing all paragraphs that start with non-bold characters.", "..."]
}
```

**Important**: In the bold/nonbold values, any two or more consecutive paragraphs belonging to the same type are concatenated with the "\n" separator.

## Example of Input and Output:
### Input text in .docx:

**Lorem** ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat luctus euismod. Ut pulvinar fermentum pellentesque. Nullam ultricies feugiat orci, eu pellentesque lorem fringilla eu. In malesuada elit sed velit auctor maximus. Vivamus suscipit risus sem, sit amet faucibus nisi gravida a. Aliquam erat volutpat. Integer blandit vestibulum turpis, eget molestie nisi interdum ut. Quisque ante nisi, elementum in enim sed, suscipit rutrum nisl. Cras vitae odio risus. Fusce at congue metus. Pellentesque pulvinar posuere purus vel tincidunt. Nam suscipit scelerisque cursus. Fusce ultricies imperdiet ante, sit amet mollis nunc pharetra a.

**Ut vel arcu dolor. Donec a dolor lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum eu nisl mollis, maximus magna in, volutpat arcu. Vivamus a enim non elit egestas auctor ut dapibus velit. Praesent vehicula enim pellentesque tortor mattis semper. Donec gravida, mauris nec euismod bibendum, nisi sem porttitor dui, non dignissim ante neque quis erat.**

Quisque imperdiet efficitur diam. Morbi mauris mauris, malesuada ut eros non, accumsan egestas neque. Sed eu risus enim. Etiam pellentesque iaculis turpis a venenatis. Ut in justo et nibh finibus aliquet sit amet in ligula. Phasellus ultrices placerat lectus, ac laoreet turpis finibus non. In consequat augue vel sapien finibus dapibus. Fusce in tincidunt nunc, a auctor orci. Etiam suscipit elit nisl, non molestie elit ultrices in. Sed sollicitudin, nisi quis pretium fringilla, ex tellus mattis eros, iaculis congue lacus quam eget felis. Ut mattis auctor eleifend. Donec malesuada id quam at viverra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Phasellus ultrices neque non sollicitudin dapibus. Nulla facilisi. Nunc efficitur augue quis elit lobortis pretium vel ut diam. Morbi auctor in nisi vitae finibus. Sed nisl odio, varius a enim ultricies, porttitor porttitor urna. Duis varius lorem id odio iaculis, quis feugiat neque ultrices. Nulla pharetra, enim vel volutpat lobortis, lacus risus suscipit sapien, vel posuere nisi quam pretium odio. Sed a rutrum tortor. Aliquam eu ultrices tellus.

**Donec** ultrices eros quam, vitae maximus nisi commodo sit amet. Etiam tristique lectus metus, sed sollicitudin orci ultricies sit amet. Cras finibus nunc ut gravida tincidunt. Pellentesque facilisis orci nec pharetra fringilla. Ut eu imperdiet risus, eget porta nibh. Phasellus ut nisl libero. Nam sed ex eu nulla egestas pellentesque et congue sem. Duis nec interdum ante, non tincidunt urna. Ut congue tempor dapibus. Suspendisse potenti. Nam sollicitudin est purus, eu dictum urna ultrices et. Curabitur a quam ut ex pretium aliquet eu a purus. Curabitur lacinia mi quis magna commodo, eu sodales purus ullamcorper.

### Output:

```json
{
	"text":[
		"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat luctus euismod. Ut pulvinar fermentum pellentesque. Nullam ultricies feugiat orci, eu pellentesque lorem fringilla eu. In malesuada elit sed velit auctor maximus. Vivamus suscipit risus sem, sit amet faucibus nisi gravida a. Aliquam erat volutpat. Integer blandit vestibulum turpis, eget molestie nisi interdum ut. Quisque ante nisi, elementum in enim sed, suscipit rutrum nisl. Cras vitae odio risus. Fusce at congue metus. Pellentesque pulvinar posuere purus vel tincidunt. Nam suscipit scelerisque cursus. Fusce ultricies imperdiet ante, sit amet mollis nunc pharetra a.",
		"Ut vel arcu dolor. Donec a dolor lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum eu nisl mollis, maximus magna in, volutpat arcu. Vivamus a enim non elit egestas auctor ut dapibus velit. Praesent vehicula enim pellentesque tortor mattis semper. Donec gravida, mauris nec euismod bibendum, nisi sem porttitor dui, non dignissim ante neque quis erat.",
		"Quisque imperdiet efficitur diam. Morbi mauris mauris, malesuada ut eros non, accumsan egestas neque. Sed eu risus enim. Etiam pellentesque iaculis turpis a venenatis. Ut in justo et nibh finibus aliquet sit amet in ligula. Phasellus ultrices placerat lectus, ac laoreet turpis finibus non. In consequat augue vel sapien finibus dapibus. Fusce in tincidunt nunc, a auctor orci. Etiam suscipit elit nisl, non molestie elit ultrices in. Sed sollicitudin, nisi quis pretium fringilla, ex tellus mattis eros, iaculis congue lacus quam eget felis. Ut mattis auctor eleifend. Donec malesuada id quam at viverra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
		"Phasellus ultrices neque non sollicitudin dapibus. Nulla facilisi. Nunc efficitur augue quis elit lobortis pretium vel ut diam. Morbi auctor in nisi vitae finibus. Sed nisl odio, varius a enim ultricies, porttitor porttitor urna. Duis varius lorem id odio iaculis, quis feugiat neque ultrices. Nulla pharetra, enim vel volutpat lobortis, lacus risus suscipit sapien, vel posuere nisi quam pretium odio. Sed a rutrum tortor. Aliquam eu ultrices tellus.",
		"Donec ultrices eros quam, vitae maximus nisi commodo sit amet. Etiam tristique lectus metus, sed sollicitudin orci ultricies sit amet. Cras finibus nunc ut gravida tincidunt. Pellentesque facilisis orci nec pharetra fringilla. Ut eu imperdiet risus, eget porta nibh. Phasellus ut nisl libero. Nam sed ex eu nulla egestas pellentesque et congue sem. Duis nec interdum ante, non tincidunt urna. Ut congue tempor dapibus. Suspendisse potenti. Nam sollicitudin est purus, eu dictum urna ultrices et. Curabitur a quam ut ex pretium aliquet eu a purus. Curabitur lacinia mi quis magna commodo, eu sodales purus ullamcorper.",
	],
	"bold":[
		"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat luctus euismod. Ut pulvinar fermentum pellentesque. Nullam ultricies feugiat orci, eu pellentesque lorem fringilla eu. In malesuada elit sed velit auctor maximus. Vivamus suscipit risus sem, sit amet faucibus nisi gravida a. Aliquam erat volutpat. Integer blandit vestibulum turpis, eget molestie nisi interdum ut. Quisque ante nisi, elementum in enim sed, suscipit rutrum nisl. Cras vitae odio risus. Fusce at congue metus. Pellentesque pulvinar posuere purus vel tincidunt. Nam suscipit scelerisque cursus. Fusce ultricies imperdiet ante, sit amet mollis nunc pharetra a.\nUt vel arcu dolor. Donec a dolor lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum eu nisl mollis, maximus magna in, volutpat arcu. Vivamus a enim non elit egestas auctor ut dapibus velit. Praesent vehicula enim pellentesque tortor mattis semper. Donec gravida, mauris nec euismod bibendum, nisi sem porttitor dui, non dignissim ante neque quis erat.",
		"Donec ultrices eros quam, vitae maximus nisi commodo sit amet. Etiam tristique lectus metus, sed sollicitudin orci ultricies sit amet. Cras finibus nunc ut gravida tincidunt. Pellentesque facilisis orci nec pharetra fringilla. Ut eu imperdiet risus, eget porta nibh. Phasellus ut nisl libero. Nam sed ex eu nulla egestas pellentesque et congue sem. Duis nec interdum ante, non tincidunt urna. Ut congue tempor dapibus. Suspendisse potenti. Nam sollicitudin est purus, eu dictum urna ultrices et. Curabitur a quam ut ex pretium aliquet eu a purus. Curabitur lacinia mi quis magna commodo, eu sodales purus ullamcorper.",
	],
	"nonbold":[
		"Quisque imperdiet efficitur diam. Morbi mauris mauris, malesuada ut eros non, accumsan egestas neque. Sed eu risus enim. Etiam pellentesque iaculis turpis a venenatis. Ut in justo et nibh finibus aliquet sit amet in ligula. Phasellus ultrices placerat lectus, ac laoreet turpis finibus non. In consequat augue vel sapien finibus dapibus. Fusce in tincidunt nunc, a auctor orci. Etiam suscipit elit nisl, non molestie elit ultrices in. Sed sollicitudin, nisi quis pretium fringilla, ex tellus mattis eros, iaculis congue lacus quam eget felis. Ut mattis auctor eleifend. Donec malesuada id quam at viverra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
		"Phasellus ultrices neque non sollicitudin dapibus. Nulla facilisi. Nunc efficitur augue quis elit lobortis pretium vel ut diam. Morbi auctor in nisi vitae finibus. Sed nisl odio, varius a enim ultricies, porttitor porttitor urna. Duis varius lorem id odio iaculis, quis feugiat neque ultrices. Nulla pharetra, enim vel volutpat lobortis, lacus risus suscipit sapien, vel posuere nisi quam pretium odio. Sed a rutrum tortor. Aliquam eu ultrices tellus.",
	]
}
```


## API Reference:
* [python-docx](https://github.com/python-openxml/python-docx "python-docx")
* [json](https://docs.python.org/3/library/json.html "python-json")

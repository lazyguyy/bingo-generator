# Bingo Generator

Have you ever wanted to generate your own Bingo boards?  
Were there ever meetings boring enough for you to notice certain patterns in how participants behave?  
Now you may generate your own Bingo boards to pass the time with something fun and interesting to do.

## Usage

To use the generator you must have the packages ``Python`` and its standard library installed.

### Minimal Example
You can call the generator from the command line like this:  
``>python bingo_generator.py < bingo_values.txt > bingo.tex``

To generate a Bingo board, the generator expects a list of at least 25 possible values for Bingo fields 
seperated by ``newline`` characters from the ``stdin``. 
The first value is treated as the center value of the Bingo board, 
all others will be drawn randomly (without repetition) from the remaining list.

The generator will then output a valid latex file which compiles to a document containing a Bingo board on ``stdout``.

### Advanced Example
Of course, for most of these events, a single Bingo board might not suffice (especially if you want to play with friends).  
We provide a few command line options for a more customized experience.  
Consider this example:  
``>python bingo_generator.py 5 -b board_template.tex -d document_template.tex < bingo_values.txt > bingo.tex``

Here we specifiy three options. The first, positional argument is ``n``, the number of boards to be generated.

With the optional argument ``-b`` we can specify the name of a file containing a latex template for a bingo board, in which we can insert our bingo values.

Finally, we may also change the latex template in which our bingos will be embedded. If we specify a filename with ``-d``, our bingo boards will be embedded in this file.

The files ``board_template.tex`` and ``document_template.tex`` from the repository are embedded in the python code, so you only need to take care of one file.

### More Arguments
You might not be a fan of latex. That is totally fine. And it is not a problem, because we offer the amazing command line option ``-s`` where you can specifiy a file containing a seperator to be used between two bingos (by default it is ``\n\newpage\n``).  
If you're more into html (some people say CSS is easier to use), you can modify all templates to produce valid html code instead. Use the placeholder ``#INSERT_HERE#`` to account for the bingo values that are being inserted into your document (Naturally, you can modify the default placeholder with the option ``-p``).  

You can also refer to the built-in help for more information.

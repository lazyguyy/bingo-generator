# Bingo Generator

Have you ever wanted to generate your own Bingo boards?  
Were there ever meetings boring enough for you to notice certain patterns in how participants behave?  
Now you may generate your own Bingo boards to pass the time with something fun and interesting to do.

## Usage

To use the generator you must have ``Python`` and its standard library installed. You will also need an installation of ``latex`` with the package ``tikz`` (unless you are willing to hack a bit, but more on how to do that later)

### Minimal Example
You can call the generator from the command line like this:  
``$ python bingo_generator.py < bingo_values.txt > bingo.tex``

To generate a Bingo board, the generator expects a list of at least 25 possible values for Bingo fields 
separated by ``newline`` characters from the ``stdin``. 
The first value is treated as the center value of the Bingo board, 
all others will be drawn randomly (without replacement) from the remaining list.

The generator will then output a valid latex file which compiles to a document containing 4 Bingo boards on ``stdout``.  

### Advanced Example
Of course, most of the time, a single Bingo board might not suffice (especially if you want to play with friends).  
We provide a few command line options for a more customized experience.  
Consider this example:  
``$ python bingo_generator.py 5 -b board_template.tex -d document_template.tex < bingo_values.txt > bingo.tex``

Here we specifiy three options. The first, positional argument is ``n``, the number of board templates to be filled (by default the board template contains 4 Bingo boards arranged on a single page).

With the optional argument ``-b`` we can specify the name of a file containing a latex template for a bingo board, in which the bingo values will be inserted. The string ``#INSERT_HERE#`` is used to represent a single field of the Bingo field. We assume that all fields belonging to the same board appear successively in the template and that the 13th field is the center of the board.

We may also want to change the template file in which the Bingo boards will be embedded. By specifying a filename with ``-d``, the generated bingo boards will be inserted into the given file.

The creation of the final latex file then goes as follows:
First, the number of Bingo boards in the board template is determined (each board contains 25 fields, so the number of boards is given by the number of fields divided by 25).
Then, for each of the Bingo boards, a random selection of values (with the center value being fixed) is generated and injected into the board template.
This process is repeated ``n`` times and finally all of the filled board templates are joined with a separator (by default ``\n\newpage\n``) and inserted into the document template. The result is then printed to ``stdout``.

The files ``board_template_4_bingos.tex`` and ``document_template.tex`` from the repository are embedded in the python code and used by default (for your convenience).  

### More Arguments
You might not be a fan of latex. That is totally fine and not problematic at all, because we offer the amazing command line option ``-s`` where you can specifiy a file containing a seperator to be used between two ``bingo-templates`` (by default it is ``\n\newpage\n``).  
If you're more into html (some people say CSS is easier to use), you can modify all templates to produce valid html code instead. Use the placeholder ``#INSERT_HERE#`` to account for the bingo values that are being inserted into your document (Naturally, you can modify the default placeholder with the option ``-p``).  

You can also refer to the built-in help for more information.

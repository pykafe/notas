# VIM

## Moving - Muda

- We can move using the mouse - using the mouse is slow

- We can also move using the cursor keys - also slow

- Fastest is to use the shortcut keys in normal mode

  - h - j - k - l

  - prefix with a number - 3j moves 3 rows up

- There are lost of useful shortcut keys

  - gg - move to the top of the file

  - G - move to the bottom of the file

  - 0 - move to start of the line

  - ^ - move to the first non-whitespace character

  - $ - move to the end of the line

  - w - forward one word - try 3w!

  - b - back one word - try 5b!

- Finding things

  - f<char> to jump forward to a char - use 2f<char> to jump over chars

  - F<char> to jump backwards - use 2F<char> to jump over chars

  - /<word> searches the document for <word>

    - hit enter to go to first match

    - n to next match

    - N to previous match

  - \* is the same as /<word_my_cursor_is_on><enter>

## Changing - Troka

- i - enter insert mode - <esc> to exit

### Deleting

- x - delete one character - 

  - use 5x to delete 5 characters

- d - delete things more than a character

  - dd - delete a line - try 4dd

  - dw - delete a word - try 3dw
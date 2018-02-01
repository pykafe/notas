
- What does chmod +x  <filename> do?
    
    chmod +x <filename> is a command to grant the excution permission to a file


- Why do you need `#!/usr/bin/env python` on the first line of runme.py?

    UNIX doesn't know to use python on .py files.
    So we tell UNIX to use /usr/bin/env python to execute the file.


- What is `$PATH`?

    $PATH is an environmental variable.
    $PATH lists directories which contain binaries (e.g. /usr/local/bin)


- Why does `$PATH` begin with a `$`?

    In BASH and other languages, all variables must begin with `$`


- What is a symbolic link?

    A symbolic link is a reference to a file on the file system


- Why would you use a symbolic link?

    1) You may want to reference a single file by different names
    2)  You may want to reference a single file in different locations


- How do you create a symbolic link?

    1) Find the full path to file you want to link to
    2) Find the full path to the directory you want to put the symbolic link
    3) You run the command 
        ln -s <path_of_file> <path_of_directory>


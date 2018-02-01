## CHMOD

Change the permissions of a file

#### Syntax 1 - add or remove permissions

The syntax here adds or removes individual permissions for a file

`chmod XXX filename`

X			          X    X

**u**ser/**g**roup/**o**ther  **+**/**-**  **r**ead/**w**rite/e**x**ecute

##### Examples:

- `chmod u+w myfile.txt` add write permissions for the owning user
- `chmod g-x myfile.txt` remove execute permissions for group users
- `chmod o-r myfile.txt` remove read permissions for other users

#### Syntax 2 - set all permissions at once

The syntax here sets all permissions at once

ugo

777

1 = execute

2 = write	

3 = execute + write = 1 + 2

4 = read

5 = execute + read = 4 + 1

6 = write + read = 2 + 4

7 = execute + write + read = 1 + 2 + 4



##### Examples:

- `chmod 777 myfile.txt` set the permissions for myfile.txt to read, write and execute for the owning user, the owning group, and all other users
- `chmod 755 my file.txt` set the permissions for my file.txt to read, write and execute for the owning user, but just read and execute for the owning group and other users
- `chmod 644 my file.txt` set the permissions for my file.txt to read and write for the owning user, but just read for the owning group and other users
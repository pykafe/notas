# Challenge!!!

## Create PyTree

PyTree is a clone of the tree command... kinda.
For a given directory PyTree will write a manifest of the files and directories.
For every Directory we will list the files.
PyTree will use recursion to follow through any nested directories.

For every directory level we go down, we will add an additional tab (4 spaces) to make a nice tree output like
the `tree` command.

## Example

```>> pytree('static')

static
    css
        bootstrap.min.css
        tweety.css
        tweety.css~
    js
        jquery-1.11.3.min.js
    templates
        tweety
            base.html
            tweety_index.html
            tweety_index_tweetpage.html
            tweety_like.html
            tweety_like_tweetpage.html
            tweety_tweetycomment.html
            tweety_tweetycomment_tweetpage.html
````

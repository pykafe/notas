Django Logging
==============

Logging is important.  Django makes it easy.
We log things. We _don't_ use `print` in production code.

# Read The Docs
Django has great documentation which includes a [logging primer](https://docs.djangoproject.com/en/1.9/topics/logging/). From the docs, we'll have a bit of an über-quick start.

There are levels of importance. The order of the list below is important. 

  - __DEBUG:__ Low level system information for debugging purposes
  - __INFO:__ General system information
  - __WARNING:__ Information describing a minor problem that has occurred.
  - __ERROR:__ Information describing a major problem that has occurred.
  - __CRITICAL:__ Information describing a critical problem that has occurred.

The `LEVEL` you select will in you `settings.py` will include the `LEVEL` you select __and__ all other levels below it.  So if your logger `LEVEL` is set to `DEBUG` you will log everything.  If you set the logger level to `WARNING` the log will include `WARNING` as well as `ERROR` and `CRITICAL`.

Use the appropriate logger. Below is an simple example of what your `views.py` might look like:

    # import the logging library
    import logging

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def my_view(request, *args, **kargs):
        # Log debugging information
        logger.debug("Got here!")
        
        try:
          # Log general information
          logger.info('My view has been viewed')
        except:
          # Log an error message
          logger.error('Something went wrong in my view!')

To log `DEBUG` messages and above to console add the following to `settings.py`.

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'example_app': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        },
    }

And you should see the following in your console log
Writing the result to a file as well just means adding a handler `file`.
In the example below, we write `INFO` messages and below to the file. 
`DEBUG` and everything else is written to the console.

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'INFO.log'),
            },
        },
        'loggers': {
            'example_app': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            },
        },
    }

... And that is our quick intro. You now have general logging for your app.
You console is helping you debug and you log file is logging general information like user activity.




luigi credstash
===============

`luigi-credstash` is a small utility to use credstash keys in your luigi configuration file in order to avoid
committing secrets into your repository.


## Installation
`pip install luigi-credstash`


## Client configuration file
Update your current configuration file

FROM:
```
[fancy_api]
user = my_user_name
password = SuperSecretPassword
```

TO:

```
[fancy_api]
credstash_table = super_secret_table
credstash_user_key = fancy_api.user
credstash_password_key = fancy_api.password
```

## Usage

In your code where you would have loaded credentials directly from the configuration file change it to use 
`luigi_credstash`


```python
from luigi_credstash import get_credentials_from_config


credentials = get_credentials_from_config('fancy_api')

api_user_name = credentials['user']
api_password = credentials['password']
```

## Using the mixin
We have also written a mixin to add to any class that needs credentials from the luigi configuration file. The mixin
adds two properties to the class `self.user` and `self.password`, along with a class variable called `config_key`. 

To use the mixin add it to your class (see example below) and set the `config_key`, the mixin will load the 
credentials using the credstash keys defined in the configuration file.

Example section of your config file:
```
[gmail]
credstash_table = super_secret_table
credstash_user_key = gmail.user
credstash_password_key = gmail.password
```


Example Luigi Task:
```python
import logging
import luigi
import imaplib

from luigi_credstash import credential_mixin

logger = logging.getLogger('luigi-interface')


class ExampleJob(luigi.Task, credential_mixin.CredentialMixin):

    config_key = 'gmail'

    def run(self):
        imap_session = imaplib.IMAP4_SSL('imap.gmail.com')
        result, account_details = imap_session.login(self.user, self.password)
        logger.info('Login result: {0}'.format(result))
        logger.info('Account details: {0}'.format(account_details))
```
# InstaPlus-CoinUp
Reverse Engineering With InstaPlus







## Installation

```bash
pip install NamasteAes
pip install curl_cffi
pip install pycrypto
pip install pycryptodome
pip install pycryptodomex
```

## Usage
```bash



from InstaPlus import InstaPlus

UserName = 'Your_Instagram_Username'
UserID = 'Your_Instagram_UserID'

cl = InstaPlus(UserName, UserID)
cl.appStatus()
cl.SignUp()
cl.GetFollowList()
```


{{ META START }}

{
    "category": "CaptureTheFlag",
    "sub_category": "HackTheBox",
    "title": "Craft",
    "date": "February 01, 2017"
}

{{ META END }}

# User

I wrote a simple python function to do the job for me

```python
def crack_key(raw, encrypted):
    key = ''
    index = 0
    index_old = None

    while index < len(raw):
        if index != index_old:
            index_old = index
        else:
            print('No key chars found :(')
            exit()
        for char in printables:
            decrypted = ori_decrypt(encrypted, key + char)
            if raw[index] == decrypted[index]:
                key += char
                index += 1

                print(f'Key: {key}')

                if raw.strip() == decrypted.strip():
                    return key
                break
```

Output:
``` 
_____________________________________

Starting Cracking!
_____________________________________

Key: a
Key: al
Key: ale
Key: alex
Key: alexa
Key: alexan
Key: alexand
Key: alexandr
Key: alexandro
Key: alexandrov
Key: alexandrovi
Key: alexandrovic
Key: alexandrovich
_____________________________________

Key Found: alexandrovich
Decrypted: SecThruObsFTW
_____________________________________
```

# Root

I saw this and knew what to do...

```sql
FROM * SELECT user WHERE password = 'test123'
```

```
slick@froto:~# whoami
root
```

thanks for reading!
{{ META START }}

{
    "category": "HTB",
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

![Flower](https://user-images.githubusercontent.com/4943215/55412447-bcdb6c80-5567-11e9-8d12-b1e35fd5e50c.jpg)

thanks for reading!
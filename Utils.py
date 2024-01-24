import random
import string

def encrypt_payload(data, key):
    bytes1 = bytearray(data.encode('UTF-8'))
    bytes2 = bytearray(key.encode())
    length = len(bytes1) + 6
    bArr = bytearray(length)

    for i5 in range(len(bytes1)//2):
        b6 = bytes1[i5]
        bytes1[i5] = bytes1[(len(bytes1) - i5) - 1]
        bytes1[(len(bytes1) - i5) - 1] = b6

    # for i6, ii in {0: 111, 1: 38, 2: 101}.items():
    #
    #     bArr[i6] = ii
    for i6 in range(3):
        bArr[i6]=random.randint(10,120)

    # for i7 ,io in {4: 86, 5: 38}.items():
    #
    #     bArr[i7] = io
    for i7 in range(4,6):
        bArr[i7]=random.randint(10,120)

    b7 = 0
    for b8 in bytes1:
        b7 = b7 ^ b8

    bArr[3] = b7
    i8 = 0

    for i9 in range(len(bytes1)):
        i10 = bytes2[i8] ^ b7
        i8 += 1
        if i8 >= len(bytes2):
            i8 = 0
        bArr[i9 + 6] = (i10 ^ bytes1[i9]) % 256

    i11 = 0
    i12 = 0

    for i13 in range(length):
        i11 = (i11 ^ bArr[i13]) ^ i12
        i12 += 1
        bArr[i13] = i11 % 256

    return bytes(bArr)


def decrypt_payload(data, key):
    byte_array = [int(byte) for byte in data]
    bArr = [(byte + 256) % 256 for byte in byte_array]

    bytes_str = key.encode()
    length = len(bArr) - 6
    bArr2 = bytearray(length)
    i5 = 0
    b6 = 0
    i6 = 0

    while i5 < len(bArr):
        b7 = bArr[i5]
        i7 = (b6 ^ b7) ^ i6
        i6 += 1
        bArr[i5] = i7 % 256
        i5 += 1
        b6 = b7

    b8 = bArr[3]
    i8 = 0

    for i9 in range(length):
        i10 = bytes_str[i8] ^ b8
        i8 += 1
        if i8 >= len(bytes_str):
            i8 = 0
        bArr2[i9] = (i10 ^ bArr[i9 + 6]) % 256

    for i11 in range(length // 2):
        b9 = bArr2[i11]
        i12 = length - i11 - 1
        bArr2[i11] = bArr2[i12]
        bArr2[i12] = b9

    return bArr2.decode('utf-8')

def Device_Data():
    android_mobile_companies = [
        "Samsung",
        "Google (Pixel)",
        "OnePlus",
        "Xiaomi",
        "Huawei",
        "Motorola",
        "LG",
        "Sony",
        "Nokia",
        "Oppo",
        "Vivo",
        "Realme",
        "Asus",
        "HTC",
        "Lenovo",
        "ZTE",
        "Meizu",
        "TCL",
        "Alcatel",
        "Micromax",
        "Infinix",
        "Tecno",
        "Itel",
        "Gionee",
        "Honor",
        "Panasonic",
        "Sharp",
        "Blackview",
        "Umidigi",
        "Doogee",
        "Cubot",
        "Wiko",
        "Symphony",
        "Lava",
        "Karbonn",
        "Intex",
        "Xolo"
    ]

    random_company = random.choice(android_mobile_companies).lower()
    random_model = f"{random_company}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}"

    return random_company, random_model.upper()


def Gen_UserAgent():


    dictionary = {
        "23": "6.0",
        "24": "7.0",
        "27": "8.1.0",
        "23": "6.0.1",
        "28": "9",
        "25": "7.1.2",
        "26": "8.0.0",
        "29": "10",
        "30": "11",
        "31": "12",
        "32": "12",
        "33": "13"
    }
    random_key = random.choice(list(dictionary.keys()))
    random_value = dictionary[random_key]

    return random_key,random_value


# if __name__ == '__main__':
#     data='1d 33 3c 1a 6a 00 33 5c 32 06 0c 36 4e 35 3e 41 6c 4d 0f 4e 65 4d 45 51 2a 77 0c 2c 1f 3c 0f 51 7d 20 7f 60 34 69 71 7e 36 37 46 17 1d 64 65 1c 79 2c 77 3b 7e 41 23 56 31 65 2d 49 22 2d 36 0f 5c 04 4c 2f 77 2f 65 38 12 3e 6c 15 74 4b 02 14 51 22 56 0e 0f 23 70 03 50 36 44 00 63 15 3e 54 0c 29 3d 57 15 5e 14 0a 78 53 21 4a 45 29 03 53 09 73 31 4c 7c 0d 6a 3b 64 20 21 31 05 3b 58 31 ca 4d c4 5d e5 40 bc 45 9d 63 ff 4c 96 36 b0 1e b7 33 8a 33 ca 6e da 5b c5 7b f7 7e fd 2a f7 47 df 5b ce 6f c3 10 90 09 9f 55 e7 65 ff 12 88 73 9d 5a 8e 52 c7 29 de 37 cb 16 93 03 e1 40 e2 4a e1 64 d6 6b f1 52 fe 49 b7 56 93 70 8b 7e f2 58 a7 70 bc 77 cc 35 f8 2e db 06 f0 18 a0 0a ac 7f 98 04 9f 42 da 19 8a 53 d4 0f e3 30 ab 08 dc 77 d1 44 df 53 d1 35 c5 7e 80'.replace(' ','')
#     print(data)
#     key='mo1yDn01E3yVWM8lIKdMfpo92FN79uwq99p5Mm1I3CCcvx0FSKXu84YPJGlMwkKr'
#     de=decrypt_payload(bytes.fromhex(data),key)
#     print(de)
#
#
#
#     from NamasteAes import NamasteAes
#
#
#     print(NamasteAes.dec_ecb('ZR+7SLTVUGUOGxNxpBYfe7h9Csw+D42wRTYn2tr64zfmZHggQScMLYRmwHpROe0ztYjVSVb7uJkWJJi0HcTQIOgf8yy9vPDJrnXqZdJG+No=', "ksd%lsld@@ls86ms@lmsf4f8",16))

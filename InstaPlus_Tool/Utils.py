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



def transform_letter(letter):
    letter = int(letter, 16) ^ 13
    new_letter = chr(letter)


def decrypt_flag(flag):
    flag = [detransform_letter(letter) for letter in flag]
    start = flag[: int(len(flag) / 2)]
    end = flag[len(flag) / 2 :]
    flag = start + list(reversed(end))
    return "".join(flag)


def main():
    flag = ['0x6e', '0x79', '0x6b', '0x76', '0x74', '0x62', '0x78', '0x52', '0x6c', '0x7f', '0x70', '0x24', '0x37', '0x52', '0x79', '0x6c', '0x68', '0x7f', '0x6a', '0x52', '0x68']
    flag = decrypt_flag(flag)
    print(flag)


if __name__ == "__main__":
    main()

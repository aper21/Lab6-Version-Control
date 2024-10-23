def decode(encoded_password):
    pass
    decoded_pass = ""
    for c in encoded_password:
        decoded_char = (int(c) - 3) % 10
        decoded_pass += str(decoded_char)
    return decoded_pass

print(decode('45678888'))
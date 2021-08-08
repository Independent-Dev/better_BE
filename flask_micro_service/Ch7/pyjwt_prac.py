import jwt, base64, json

SECRET = 'secret'


def decode_base64(data):
    pad = len(data) % 4
    if pad > 0:
        data += '=' * (4 - pad)
    return base64.urlsafe_b64decode(data)

def create_token(alg='HS256', secret=SECRET, **data):
    return jwt.encode(data, secret, algorithm=alg)


def read_token(token, secret=SECRET):
    token_header_str = token.split(".")[0]
    token_header_dict = json.loads(decode_base64(token_header_str).decode('utf-8'))
    return jwt.decode(token, secret, algorithms=token_header_dict['alg'])


if __name__ == '__main__':
    token = create_token(some='data', inthe='token')
    print(token)
    token_arr = token.split(".")
    read = read_token(token)
    print(read)


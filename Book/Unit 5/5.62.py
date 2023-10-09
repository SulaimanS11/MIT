book = "Once upon a time, in a house in a land far away,"
plain_text = "no is no"
gen_code_keys = (lambda book, plain_text: (
    {c: str(book.find(c)) for c in plain_text}))

print(gen_code_keys(book, plain_text))

encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])
encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))

gen_decode_keys = (lambda book, cipher_text:
                   {s: book[int(s)] for s in cipher_text.split('*')})

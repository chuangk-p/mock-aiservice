def word_tokenize(text:str, normalize:bool=False, return_json:bool=False, engine:str='lexto'):
    if engine == 'lexto':
        from mockaiservice.tokenize.lexto import tokenize
        return tokenize(text, normalize=normalize, return_json=return_json)
    if engine == 'trexplus':
        from mockaiservice.tokenize.trexplus import tokenize
        return tokenize(text, return_json=return_json)
    if engine == 'trexplusplus':
        from mockaiservice.tokenize.trexplusplus import tokenize
        return tokenize(text, return_json=return_json)
    else:
        raise ValueError(
            f"""Tokenizer \"{engine}\" not found."""
        )

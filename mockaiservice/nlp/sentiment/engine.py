def analyze(text:str, engine:str='ssense', return_json:bool=True):
    if engine == 'emonews':
        from mockaiservice.nlp.sentiment.emonews import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'ssense':
        from mockaiservice.nlp.sentiment.ssense import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'thaimoji':
        from mockaiservice.nlp.sentiment.thaimoji import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'cyberbully':
        from mockaiservice.nlp.sentiment.cyberbully import analyze
        return analyze(text, return_json=return_json)
    else:
        raise ValueError(
            f"""Analyzer \"{engine}\" not found."""
        )

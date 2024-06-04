def word_similarity(text:str, model:str='thwiki', numword:int=5, 
                    return_json:bool=False, engine:str='base'):
    if engine == 'base':
        from mockaiservice.similarity.base import similarity
        return similarity(text, model=model, numword=numword, return_json=return_json)
    else:
        raise ValueError(
            f"""Engine \"{engine}\" not found."""
        )

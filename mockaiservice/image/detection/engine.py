def analyze(file:str, return_json:bool=True, engine:str='face'):
    if engine == 'face':
        from mockaiservice.image.detection.facedetection import analyze
        return analyze(file, return_json=return_json)
    elif engine == 'facemask':
        from mockaiservice.image.detection.maskdetection import analyze
        return analyze(file, return_json=return_json)
    else:
        raise ValueError(
            f"""Detection Model \"{engine}\" not found."""
        )

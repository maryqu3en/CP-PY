# Is Integer Array? ------------------------------------------------------------------
def is_int_array(arr):
    if not arr and arr is not None and arr != '' and not isinstance(arr, bool):
        return True
    
    if isinstance(arr, list):
        return all(isinstance(e, (int, float)) and e == int(e) for e in arr)
    
    return False


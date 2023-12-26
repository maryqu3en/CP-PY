# Is Integer Array? ------------------------------------------------------------------
def is_int_array(arr):
    if arr is None or arr == '' or isinstance(arr, bool):
        return False
    if not arr:
        return True
    if isinstance(arr, list):
        return all(isinstance(e, (int, float)) and e == int(e) for e in arr)
    return False



from airport_csv_functions import fetchLatLongFromName, fetchLatLongFromIdent

def test_fetch_coords_name_bad():
    assert fetchLatLongFromName("asdkfjh") == "ERROR: coordinates not found"

def test_fetch_coords_name_good():
    res = fetchLatLongFromName("Grove Field")
    assert  res[0] == "45.62779998779297", res[1] == "-122.40399932861328"

def test_fetch_coords_ident_bad():
    assert fetchLatLongFromIdent(02348) == "ERROR: coordinates not found"

def test_fetch_coords_ident_good():
    res = fetchLatLongFromIdent("00A")
    assert  res[0] == "40.07080078125", res[1] == "-74.93360137939453"

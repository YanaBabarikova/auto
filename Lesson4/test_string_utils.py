import pytest
from string_utils import StringUtils

@pytest.mark.parametrize( 'string, result', [
    ("skypro", "Skypro"),
    ("hello", "Hello"),
    ("name1", "Name1"),
    ("name_lastname", "Name_lastname"),
    ("yanaSh", "Yanash"),
    ("anna mary", "Anna mary"),
    ("GPS", "Gps"),
    ("name-1", "Name-1"),
    (" ", " "),
    ("Baby", "Baby"),] )

def test_small_or_big(string, result):
    string_unit = StringUtils()
    res = string_unit.capitilize(string)
    assert res == result

@pytest.mark.parametrize( 'string, result', [
    (" skypro", "skypro"),
    ("  hello", "hello"),
    (" name 1", "name 1"),
    (" name _ lastname ", "name _ lastname "),
    (" y a n a S h", "y a n a S h"),
    ("   Anna-Mary", "Anna-Mary"),
    (" G P S", "G P S"),
    (" name-1", "name-1"),
    ("Тame", "Тame"),
    ("  .", "."),] )

def test_space(string, result):
    string_unit = StringUtils()
    res = string_unit.trim(string)
    assert res == result

@pytest.mark.parametrize( 'string, delimeter, result', [
    ("s,k,y,p,r,o", ",", ["s","k","y","p","r","o"] ),
    ('h:e:l:l:o', ':', ['h','e','l','l','o']),
    ("n_a_m_e_l_a_s_t_n_a_m_e", "_", ["n","a","m","e","l","a","s","t","n","a","m","e"]),
    ("A-n-n-a-M-a-r-y", "-", ["A","n","n","a","M","a","r","y"]),
    ("G&P&S", "&", ["G","P","S"]),
    ("n?a?m?e?-?1", "?", ["n","a","m","e","-","1"]),
    ("Тamae", "a", ["Т","m","e"])])

def test_separators(string, result, delimeter):
    string_unit = StringUtils()
    res = string_unit.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [
    ("skypro", "s", True),
    ("hello", "g", False),
    ("name1", "1", True),
    ("name_lastname", "r", False),
    ("yanaSh", "y", True),
    ("Anna-Mary", "M", True),
    ("GPS", "P", True),
    ("name-1", "e", True),
    ("Тame", "Т", True),] )

def test_contains(string, symbol, result):
    string_unit = StringUtils()
    res = string_unit.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [
    ("skypro", "s", "kypro"),
    ("hello", "lo", "hel"),
    ("name1", "1", "name"),
    ("name_lastname", "name_", "lastname"),
    ("yanaSh", "Sh", "yana"),
    ("Anna-Mary", "Mary", "Anna-"),
    ("GPS", "P", "GS"),
    ("name-1", "-1", "name"),
    ("Тame", "Т", "ame")] )

def test_delete_symbol(string, symbol, result):
    string_unit = StringUtils()
    res = string_unit.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [
    ("skypro", "s", True),
    ("hello", "g", False),
    ("name1", "n", True),
    ("name_lastname", "r", False),
    ("yanaSh", "y", True),
    ("Anna-Mary", "A", True),
    ("GPS", "P", False),
    ("name-1", "e", False),
    (" Тame", "Т", False)] )

def test_starts_with(string, symbol, result):
    string_unit = StringUtils()
    res = string_unit.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, symbol, result', [
    ("skypro", "o", True),
    ("hello", "g", False),
    ("name1", "1", True),
    ("name_lastname", "m", False),
    ("yanaSh", "h", True),
    ("Anna-Mary ", " ", True),
    ("GPS", "P", False),
    ("name-1", "e", False),
    (" Тame", "Т", False)] )

def test_end_with(string, symbol, result):
    string_unit = StringUtils()
    res = string_unit.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize( 'string, result', [
    (" ", True),
    ("  .", False),
    ("  ", True),
    (" yanaSh", False),
    ("   ", True),
    ("Anna-Mary ", False),
    ("GPS", False),
    ("123", False),
    (" Тame", False)] )

def test_is_empty(string, result):
    string_unit = StringUtils()
    res = string_unit.is_empty(string)
    assert res == result

@pytest.mark.parametrize( 'lst, joiner, result', [
    (["s","k","y","p","r","o"], ",", "s,k,y,p,r,o"),
    (['h','e','l','l','o'], ':', 'h:e:l:l:o'),
    (["n","a","m","e","l","a","s","t","n","a","m","e"], "_", "n_a_m_e_l_a_s_t_n_a_m_e"),
    (["A","n","n","a","M","a","r","y"], "-", "A-n-n-a-M-a-r-y"),
    (["G","P","S"], "&", "G&P&S"),
    (["n","a","m","e","-","1"],  "?", "n?a?m?e?-?1"),
    (["Т","m","e"], "a", "Тamae")])

def test_list_to_string(lst, joiner, result):
    string_unit = StringUtils()
    res = string_unit.list_to_string(lst, joiner)
    assert res == result
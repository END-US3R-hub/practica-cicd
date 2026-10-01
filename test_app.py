from app import es_ip_valida

def test_ip_valida():
    assert es_ip_valida('192.168.1.1') == True

def test_ip_invalida():
    assert es_ip_valida('999.999.999.999') == False

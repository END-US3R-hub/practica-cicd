import ipaddress

def es_ip_valida(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

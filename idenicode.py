import socket

def get_service_name(port):
    try:
        result = socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"
    return result


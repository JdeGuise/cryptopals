import base64
def hex_to_64(str_to_convert):
	return base64.b64encode(bytes(str_to_convert.decode("hex")), 'utf-8')
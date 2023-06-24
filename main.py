import qrcode

# Criando um objeto QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionando texto ao QR Code
qr.add_data('Esse QR Code foi gerado com linguagem Python')

# Gerando o QR Code
qr.make(fit=True)

# Criando um objeto de imagem a partir do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvando a imagem que foi gerada em um arquivo com extensão PNG
img.save('qr_code.png')

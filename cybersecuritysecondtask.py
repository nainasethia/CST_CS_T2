from PIL import Image # type: ignore

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

 # image path
input_image = r"C:\Users\naina\OneDrive\Documents\CS Task\CST_CS_T2\input.jpg.jpeg"
encrypted_image = r"C:\Users\naina\OneDrive\Documents\CS Task\CST_CS_T2\encrypted_image.jpg.jpeg"
decrypted_image = r"C:\Users\naina\OneDrive\Documents\CS Task\CST_CS_T2\decrypted_image.jpg.jpeg"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None) 
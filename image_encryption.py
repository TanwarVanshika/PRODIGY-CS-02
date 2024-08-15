from PIL import Image as im
import numpy as np

def encrypt_image(image_path, result_path, key):
    image = im.open(image_path)
    pixels = np.array(image)

    #Applying basic mathematical operation to each pixel
    encrypted_pixels = (pixels+key)%256

    encrypted_image = im.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(result_path)
    print(f"Image encrypted and saved to {result_path}")

def decrypt_image(image_path, result_path, key):
    image = im.open(image_path)
    pixels = np.array(image)

    #Reversing the mathematical operation
    decrypted_pixels = (pixels-key)%256

    decrypted_image = im.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(result_path)
    print(f"Image decrypted and saved to {result_path}")

def main():
    while True:
        action = input("Input 'encrypt' to encrypt OR 'decrypt' to decrypt : ").lower()
        if action not in ['encrypt', 'decrypt']:
            print("Invalid Input. Please input a valid one. ")
            continue

        image_path = input("Enter the path of the image : ")
        result_path = input("Enter the path to save the resulting image : ")
        key = int(input("Enter the encryption/decryption key (should be an integer) : "))

        if action == 'encrypt':
            encrypt_image(image_path, result_path, key)
        else:
            decrypt_image(image_path, result_path, key)

        if input("Do you want to attempt again? (yes/no) : ").lower()!='yes':
            break

if __name__ == "__main__":
    main()


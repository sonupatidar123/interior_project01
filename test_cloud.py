import cloudinary
import cloudinary.uploader

# Credentials manually set kar rahe hain verification ke liye
cloudinary.config( 
  cloud_name = "dguujmj75", 
  api_key = "441238871653336", 
  api_secret = "IdV3dJ8PFjvWzR7vqrWJajtJVog",
  secure = True
)

print("Testing Cloudinary upload...")

try:
    # Ek sample photo upload kar rahe hain
  # Purani butterfly wali line ko hata kar ye likhein
    response = cloudinary.uploader.upload("image.png") # "test.jpg" ki jagah apni file ka naam likhein
    print("--- SUCCESS! ---")
    print("Mubarak ho! Photo Cloudinary par upload ho gayi.")
    print("Aapki Photo ka URL ye hai:", response['secure_url'])
except Exception as e:
    print("--- FAILED! ---")
    print("Error aa gaya:", e)
from deepface import DeepFace

def verify_faces(image1_path, image2_path):
    result = DeepFace.verify(image1_path, image2_path)
    
    if result["verified"]:
        print("Verification successful: The faces belong to the same person.")
    else:
        print("Verification failed: The faces belong to different persons.")
        print(f"Distance: {result['distance']:.2f}")

# Provide the file paths for the two images you want to verify
image1_path = "elon1.jpg"
image2_path = "bezos1.jpg"

verify_faces(image1_path, image2_path)

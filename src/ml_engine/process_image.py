from PIL import Image
import torch
import torchvision.transforms as transforms
def prepare_image(image_path):
img = Image.open(image_path).convert('RGB')
transform = transforms.Compose([transforms.resize((224,224)),transforms.ToTensor(),])
img_tensor = transform(img)
print(f"Image converted to Tensor of shape: {img_tensor.shape}")
return img_tensor
if __name__ == "__main__":
print("Image processor ready.")


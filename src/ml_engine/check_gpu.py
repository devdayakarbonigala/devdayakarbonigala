import torch

# Check for Apple Silicon GPU support (Metal Performance Shaders)
if torch.backends.mps.is_available():
    print("✅ Success! Your MacBook GPU (MPS) is available for Deep Learning.")
else:
    print("❌ Using CPU. (Ensure you have torch installed via 'pip install torch')")

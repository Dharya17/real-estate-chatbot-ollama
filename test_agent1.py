from agent1 import agent1_flow

if __name__ == "__main__":
    # Provide the path to a sample image
    image_path = "wall_damage.jpeg"  # Replace with your test image file
    
    caption, suggestion = agent1_flow(image_path)

    print("🖼️ Image Caption:")
    print(caption)
    print("\n🛠️ Troubleshooting Suggestion:")
    print(suggestion)

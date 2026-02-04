import os
import sys

def main():
    print("🚀 Pipeline Doctor Target App is running...")
    
    # Simulate a potential failure based on environment variable
    if os.getenv("CAUSE_FAILURE") == "True":
        print("❌ Simulating a failure...")
        # Intentional failure: ModuleNotFoundError
        import non_existent_module
    
    print("✅ App finished successfully!")

if __name__ == "__main__":
    main()

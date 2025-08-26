import logging
import argparse, json, sys

from pathlib import Path

logging.basicConfig(level=logging.INFO)

def main():
    p = argparse.ArgumentParser() # Create an argument parser 
    p.add_argument("--input", required=True) # input file path
    p.add_argument("-filter",type=str) 
    args = p.parse_args() #

    try:
        data = json.loads(Path(args.input).read_text())
        filterWord = args.filter
        
        if data is None:
            raise ValueError("No data found in the input file.")
        else :
            if filterWord:
                filteredList = [item for item in data if filterWord in item] # Filter items based on the provided word
            else:
                filteredList = [item for item in data]
            
    except Exception as e:
        logging.error(f"Error: {e}",file=sys.stderr) # sterr is the standard error stream
        sys.exit(1)
    print(f"Items: {len(data)}")
    print(f"Filtered Items: {len(filteredList)}")

if __name__ == "__main__": # This ensures the main function runs only when the script is executed directly
    main()
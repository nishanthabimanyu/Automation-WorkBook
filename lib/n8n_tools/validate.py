import json
import os
import sys
import click

def validate_workflow(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, dict):
            print(f"❌ Invalid: {file_path} (Root is not an object)")
            return False
            
        if "nodes" not in data or "connections" not in data:
            print(f"❌ Invalid: {file_path} (Missing 'nodes' or 'connections')")
            return False
            
        # Basic check passed
        return True
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON: {file_path}")
        return False
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False

@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path):
    """Validate n8n workflow files."""
    if os.path.isfile(path):
        if validate_workflow(path):
            print(f"✅ Valid: {path}")
            sys.exit(0)
        else:
            sys.exit(1)
            
    # If it's a directory, walk through it
    failed = False
    count = 0
    
    for root, dirs, files in os.walk(path):
        # Skip node_modules and .git
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith('.json'):
                full_path = os.path.join(root, file)
                # Skip package.json or tsconfig.json if they exist
                if file in ['package.json', 'tsconfig.json', 'lock.json']:
                    continue
                    
                if not validate_workflow(full_path):
                    failed = True
                else:
                    # Optional: Don't print every success to reduce noise, or print simple dot
                    # print(f"✅ Valid: {full_path}")
                    count += 1

    print(f"Validated {count} workflows.")
    
    if failed:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()

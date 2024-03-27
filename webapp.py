from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def launch():
    # Specify the path to your .bat or .cmd file
    bat_file_path = r'script.bat'  # Update this with your actual file path

    try:
        # Execute the .bat or .cmd file
        completed_process = subprocess.run(bat_file_path, shell=True, capture_output=True, text=True)

        # Check if the process completed successfully
        if completed_process.returncode == 0:
            return "Execution successful" 
        else:
            msg = f"Execution failed. Error output: {completed_process.stderr}"
            return msg
    
    except Exception as e:
        msg = f"An error occurred: {str(e)}"
        return msg

    
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

## How to Use WiFi Password Viewer:


```bash
wifi_password_viewer/
├── wifi_password_viewer/
│   ├── __init__.py
│   ├── core.py
├── tests/
│   ├── test_wifi_password_viewer.py
├── pyproject.toml
```

#### Step 1: Install the Package:
- Run the following command to install the package using pip:

```bash
pip install wifi-password-viewer
```

#### Step 2: Use in a Python Script
- Create a Python script (e.g., run_wifi_viewer.py) with the following content:

```python
from wifi_password_viewer import display_wifi_passwords

if __name__ == "__main__":
    display_wifi_passwords()
```

#### Step 3: Run the Script
Execute the script to display the Wi-Fi names and passwords in a table:

```bash
python run_wifi_viewer.py
```

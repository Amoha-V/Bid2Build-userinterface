# Page Configuration - MUST BE FIRST
import streamlit as st
st.set_page_config(
    page_title="Bid 2 Build: Tech Component Marketplace",
    page_icon="🔧",
    layout="wide"
)

import pandas as pd
import os
from PIL import Image
import base64

def load_components_data():
    components_data = {
        'Category': [],
        'Component Name': [],
        'Base Price': [],
        'Points': [],
        'Virtual Hardware': [],
        'Image': []
    }
    
    def add_component(category, name, base_price, points, virtual_hardware, image_file):
        try:
            # Try to open the image first to verify it exists
            img_path = os.path.join('images', image_file)
            Image.open(img_path)
            image_path = img_path
        except:
            # Use placeholder if image doesn't exist
            image_path = os.path.join('images', 'placeholder.png')
            st.warning(f"Image not found: {image_file}")
        
        components_data['Category'].append(category)
        components_data['Component Name'].append(name)
        components_data['Base Price'].append(base_price)
        components_data['Points'].append(points)
        components_data['Virtual Hardware'].append(virtual_hardware)
        components_data['Image'].append(image_path)
    
    # Microcontrollers
    add_component('Microcontrollers', 'Arduino UNO(Real)', 2200, 100, 4, 'arduino_uno.png')
    add_component('Microcontrollers', 'ESP32(Real)', 3000, 150, 2, 'esp32.png')
    add_component('Microcontrollers', 'Raspberry Pi(Real)', 4000, 150, 2, 'raspberrypi.png')
    add_component('Microcontrollers', 'Arduino UNO(Virtual)', 800, 100, 4, 'arduino_uno.png')
    add_component('Microcontrollers', 'ESP32(Virtual)', 1600, 150, 2, 'esp32.png')
    # Sensors
    sensor_data = [
        ('HC-SR04', 400, 60, 'hc_sr04.png'),
        ('MQ3', 800, 60, 'mq3.jpg'),
        ('DHT11', 600, 55, 'dht11.jpg'),
        ('Gyro Sensor', 880, 70, 'gyro_sensor.jpg'),
        ('IR Sensors', 120, 55, 'ir_sensor.jpeg'),
        ('Soil Moisture Sensor', 400, 55, 'soil_moisture_sensor.jpg'),
        ('Force Sensor', 720, 80, 'pressure_sensor.jpg'),
        ('PIR Sensor', 800, 50, 'pir_sensor.jpg'),
        ('Photo Resistance', 200, 60, 'photo_resistance.jpg'),
        ('Metal Touch', 560, 85, 'metal_touch.jpg'),
        ('Flame Sensor', 600, 65, 'flame_sensor.jpg'),
        ('Vibration Sensor', 720, 70, 'vibration_sensor.jpg'),
    ]
    
    for name, price, points, image in sensor_data:
        add_component('Sensors', name, price, points, 1, image)
    
    # Actuators
    actuator_data = [
        ('Servo Motor', 600, 100, 'servo_discrete.png'),
        ('Push Buttons', 40, 10, 'push_buttons.jpg'),
        ('DC Motors', 400, 70, 'dc_motors.jpg'),
        ('Motor Shield', 1400, 60, 'motor_shield.jpg'),
        ('RGB', 380, 35, 'rgb.jpg'),
        ('LCD Display', 1280, 100, 'lcd_display.jpg'),
        ('LED', 40, 3, 'led.jpg'),
        ('Buzzer', 80, 10, 'buzzer.jpg')
    ]
    
    for name, price, points, image in actuator_data:
        add_component('Actuators', name, price, points, 1, image)
    
    # Software
    software_data = [
        ('Python 311', 1500, 75, 'python_logo.png'),
        ('Embedded C', 1200, 60, 'embedded_c.png'),
        ('Arduino IDE', 2500, 55, 'arduino_ide.png'),
        ('Flask/fastAPI', 1000, 55, 'flask.png'),
        ('Tinker CAD/WOKWI', 2600, 50, 'tinkercad.png'),
        ('Adafruit Libraries', 1500, 75, 'adafruit.png'),
        ('NewPing', 1250, 75, 'newping.png'),
        ('I2C', 1500, 95, 'i2c.png'),
        ('Streamlit', 1000, 95, 'streamlit.png'),
        ('HTML+CSS', 800, 95, 'html.png'),
        ('PySerial', 500, 95, 'pyserial.png'),
        ('Other Libraries', 2500, 50, 'libraries.png')
    ]
    
    for name, price, points, image in software_data:
        add_component('Software', name, price, points, '-', image)
    
    return pd.DataFrame(components_data)

def img_to_bytes(img_path):
    """Convert image to base64 for HTML display"""
    img_bytes = None
    try:
        with open(img_path, 'rb') as f:
            img_bytes = f.read()
        return base64.b64encode(img_bytes).decode()
    except:
        return ""

def main():
    # Custom CSS for a more professional look
    st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f4;
    }
    .css-1aumxhk {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    .component-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 12px;
        overflow: hidden;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .component-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    .component-card img {
        transition: transform 0.3s ease;
    }
    .component-card:hover img {
        transform: scale(1.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and Subtitle
    st.markdown("""
    <h1 style="text-align: center; color: #2c3e50;">Bid 2 Build 🔧</h1>
    <h3 style="text-align: center; color: #7f8c8d; margin-bottom: 30px;">
    Your Ultimate Tech Component Marketplace
    </h3>
    """, unsafe_allow_html=True)

    # Load Components Data
    df = load_components_data()

    # Sidebar Filters
    st.sidebar.header("🔍 Component Filters")
    category = st.sidebar.multiselect(
        "Select Categories", 
        df['Category'].unique(),
        default=df['Category'].unique()
    )
    
    min_price, max_price = st.sidebar.slider(
        "Price Range (₹)", 
        min_value=0, 
        max_value=int(df['Base Price'].max()), 
        value=(0, int(df['Base Price'].max()))
    )

    # Filter Data
    filtered_df = df[
        (df['Category'].isin(category)) & 
        (df['Base Price'] >= min_price) & 
        (df['Base Price'] <= max_price)
    ]

    # Display Components
    st.markdown("## 🛠 Available Components")
    
    if filtered_df.empty:
        st.warning("No components match your filters!")
    else:
        columns = st.columns(3)
        
        for i, (index, row) in enumerate(filtered_df.iterrows()):
            col = columns[i % 3]
            
            with col:
                # Convert image to base64 for reliable display
                img_bytes = img_to_bytes(row['Image'])
                
                if img_bytes:
                    img_html = f"data:image/png;base64,{img_bytes}"
                else:
                    img_html = ""
                
                st.markdown(f"""
                <div class="component-card" style="margin-bottom: 20px; padding: 15px; text-align: center;">
                    <div style="height: 250px; display: flex; justify-content: center; align-items: center; margin-bottom: 15px;">
                        <img src="{img_html}" style="max-width:100%; max-height:250px; object-fit: contain;">
                    </div>
                    <h3 style="margin-top:10px; color: #2c3e50;">{row['Component Name']}</h3>
                    <p style="color: #7f8c8d;"><strong>Category:</strong> {row['Category']}</p>
                    <p style="color: #27ae60;"><strong>Base Price:</strong> ₹ {row['Base Price']}</p>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
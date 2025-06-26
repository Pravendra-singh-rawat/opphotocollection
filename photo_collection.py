# import streamlit as st
# from datetime import datetime

# # --- Streamlit Config ---
# st.set_page_config(
#     page_title="Exam Day Photo Capture",
#     page_icon="📸",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# st.markdown("<h1 style='text-align: center;'>📸 Exam Day Photo Capture</h1>", unsafe_allow_html=True)
# st.markdown("#### Capture and confirm your exam selfie with center code & section")

# st.divider()

# # --- Layout Inputs ---
# col1, col2 = st.columns(2)

# with col1:
#     section = st.selectbox(
#         "🗂️ Select Photo Section",
#         ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"],
#         index=0
#     )

# with col2:
#     center_code = st.text_input("🏷️ Enter Center Code")

# st.write("")

# # --- Webcam Capture ---
# st.markdown("### 📷 Capture Your Selfie")
# image = st.camera_input("")

# # --- Preview & Confirmation ---
# if image:
#     st.markdown("### 🖼️ Photo Preview")
#     st.image(image, caption="✅ Your Captured Photo", use_column_width=True)

#     st.markdown("---")

#     col3, col4 = st.columns([1, 2])
#     with col3:
#         confirm = st.button("✅ Confirm & Submit", use_container_width=True)
#     with col4:
#         retake = st.button("🔁 Retake Photo", use_container_width=True)

#     if confirm and center_code:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         st.success("✅ Photo confirmed successfully!")
#         st.markdown(f"""
#         **📄 Section:** `{section}`  
#         **🏷️ Center Code:** `{center_code}`  
#         **🕒 Time:** `{timestamp}`
#         """)
#     elif confirm and not center_code:
#         st.error("🚫 Please enter a center code before submitting.")

#     if retake:
#         st.experimental_rerun()

# else:
#     st.info("📸 Please capture a selfie using the camera above to preview.")











# import streamlit as st
# from datetime import datetime

# # --- Streamlit Config ---
# st.set_page_config(
#     page_title="Exam Day Photo Capture",
#     page_icon="📸",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# st.markdown("<h1 style='text-align: center;'>📸 Exam Day Photo Capture</h1>", unsafe_allow_html=True)
# st.markdown("#### Capture and confirm your exam selfie with center code, section & location")

# st.divider()

# # --- Layout Inputs ---
# col1, col2 = st.columns(2)

# with col1:
#     section = st.selectbox(
#         "🗂️ Select Photo Section",
#         ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"],
#         index=0
#     )

# with col2:
#     center_code = st.text_input("🏷️ Enter Center Code")

# # --- Get GeoLocation (via JS) ---
# geo_coords = st.text_input("📍 Auto-filled Geo Coordinates")

# st.components.v1.html("""
#     <script>
#     navigator.geolocation.getCurrentPosition(
#         function(position) {
#             const coords = position.coords.latitude + "," + position.coords.longitude;
#             const input = window.parent.document.querySelector('input[data-testid="stTextInput"][placeholder="📍 Auto-filled Geo Coordinates"]');
#             if (input) {
#                 input.value = coords;
#                 input.dispatchEvent(new Event("input", { bubbles: true }));
#             }
#         }
#     );
#     </script>
# """, height=0)

# st.divider()

# # --- Webcam Capture ---
# st.markdown("### 📷 Capture Your Selfie")
# image = st.camera_input("")

# # --- Preview & Confirmation ---
# if image:
#     st.markdown("### 🖼️ Photo Preview")
#     st.image(image, caption="✅ Your Captured Photo", use_container_width=True)

#     st.markdown("---")

#     col3, col4 = st.columns([1, 2])
#     with col3:
#         confirm = st.button("✅ Confirm & Submit", use_container_width=True)
#     with col4:
#         retake = st.button("🔁 Retake Photo", use_container_width=True)

#     if confirm:
#         if not center_code or not geo_coords:
#             st.error("🚫 Please enter center code and allow location access.")
#         else:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             lat, lon = geo_coords.split(",") if "," in geo_coords else ("", "")

#             st.success("✅ Photo confirmed successfully!")
#             st.markdown(f"""
#             **📄 Section:** `{section}`  
#             **🏷️ Center Code:** `{center_code}`  
#             **🕒 Time:** `{timestamp}`  
#             **📍 Latitude:** `{lat.strip()}`  
#             **📍 Longitude:** `{lon.strip()}`
#             """)
#     if retake:
#         st.experimental_rerun()

# else:
#     st.info("📸 Please capture a selfie using the camera above to preview.")



















# import streamlit as st
# from datetime import datetime
# from streamlit_js_eval import streamlit_js_eval

# # --- App Config ---
# st.set_page_config(page_title="Exam Day Photo", page_icon="📸", layout="centered")

# st.markdown("<h1 style='text-align: center;'>📸 Exam Day Photo Capture</h1>", unsafe_allow_html=True)
# st.markdown("#### Select section, enter center code, capture selfie & auto-capture your location")
# st.divider()

# # --- Form Inputs ---
# col1, col2 = st.columns(2)
# with col1:
#     section = st.selectbox("🗂️ Select Photo Section", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])
# with col2:
#     center_code = st.text_input("🏷️ Enter Center Code")

# # --- Get GeoLocation (automatically) ---
# coords = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition", key="get_position", timeout=10)
# geo_success = False

# if coords and "coords" in coords:
#     lat = coords['coords']['latitude']
#     lon = coords['coords']['longitude']
#     geo_success = True
# else:
#     lat, lon = "", ""

# # --- Webcam Input ---
# st.markdown("### 📷 Capture Your Selfie")
# image = st.camera_input("")

# # --- Preview & Confirmation ---
# if image:
#     st.markdown("### 🖼️ Photo Preview")
#     st.image(image, caption="✅ Your Captured Photo", use_container_width=True)
#     st.divider()

#     col3, col4 = st.columns([1, 2])
#     with col3:
#         confirm = st.button("✅ Confirm & Submit", use_container_width=True)
#     with col4:
#         retake = st.button("🔁 Retake Photo", use_container_width=True)

#     if confirm:
#         if not center_code:
#             st.error("🚫 Please enter the center code.")
#         elif not geo_success:
#             st.error("📍 Location access failed or was denied.")
#         else:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#             st.success("✅ Photo confirmed successfully!")
#             st.markdown(f"""
#             **📄 Section:** `{section}`  
#             **🏷️ Center Code:** `{center_code}`  
#             **🕒 Time:** `{timestamp}`  
#             **📍 Latitude:** `{lat}`  
#             **📍 Longitude:** `{lon}`
#             """)
#     if retake:
#         st.experimental_rerun()
# else:
#     st.info("📸 Please take a selfie using the camera above.")

























import streamlit as st
from streamlit_js_eval import get_geolocation
import time
import base64
from datetime import datetime

# App Title & Description
st.set_page_config(page_title="Capture Verification", layout="centered")
st.title("📸 Capture Verification Portal 📌")
st.markdown("Welcome! Please complete the verification process below.")

# Section Selection
section = st.selectbox("✅ Select Your Section:", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])

# Center Code Input
center_code = st.text_input("🏢 Enter Your Center Code:")

# Geolocation Retrieval
st.markdown("📍 Fetching your location...")
geo_data = get_geolocation()

if geo_data:
    lat = geo_data['coords']['latitude']
    lon = geo_data['coords']['longitude']
else:
    lat, lon = None, None

# Photo Capture
st.markdown("📷 Take a photo:")
img_file_buffer = st.camera_input("Capture your photo")

# Preview and Retake Option
if img_file_buffer is not None:
    st.image(img_file_buffer, caption="Preview", use_column_width=True)
    if st.button("🔁 Retake Photo"):
        img_file_buffer = None  # Reset the image buffer
        st.experimental_rerun()
else:
    st.info("Please take a photo to continue.")

# Submission
if img_file_buffer and st.button("✅ Submit") and lat is not None and lon is not None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Encode image to base64 for display or storage
    encoded_img = base64.b64encode(img_file_buffer.getvalue()).decode()
    
    st.success("✅ Submission Successful!")
    st.markdown(f"**Section:** {section}")
    st.markdown(f"**Center Code:** {center_code}")
    st.markdown(f"**Timestamp:** {timestamp}")
    st.markdown(f"**Latitude:** {lat:.6f}")
    st.markdown(f"**Longitude:** {lon:.6f}")

    # Optional: Show submitted image again from base64
    st.markdown('<h4>Submitted Photo:</h4>', unsafe_allow_html=True)
    st.markdown(
        f'<img src="data:image/png;base64,{encoded_img}" width="300">',
        unsafe_allow_html=True
    )

elif img_file_buffer and (lat is None or lon is None):
    st.error("❌ Unable to retrieve your location. Please allow location access and reload the page.")

# Footer
st.markdown("---")
st.markdown("🔒 All data collected is used solely for verification purposes.")

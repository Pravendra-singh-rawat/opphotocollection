# import streamlit as st
# from streamlit_js_eval import get_geolocation
# import time
# import base64
# from datetime import datetime

# # App Title & Description
# st.set_page_config(page_title="Capture Verification", layout="centered")
# st.title("📸 Capture Verification Portal 📌")
# st.markdown("Welcome! Please complete the verification process below.")

# # Section Selection
# section = st.selectbox("✅ Select Your Section:", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])

# # Center Code Input
# center_code = st.text_input("🏢 Enter Your Center Code:")

# # Geolocation Retrieval
# st.markdown("📍 Fetching your location...")
# geo_data = get_geolocation()

# if geo_data:
#     lat = geo_data['coords']['latitude']
#     lon = geo_data['coords']['longitude']
# else:
#     lat, lon = None, None

# # Photo Capture
# st.markdown("📷 Take a photo:")
# img_file_buffer = st.camera_input("Capture your photo")

# # Preview and Retake Option
# if img_file_buffer is not None:
#     st.image(img_file_buffer, caption="Preview", use_column_width=True)
#     if st.button("🔁 Retake Photo"):
#         img_file_buffer = None  # Reset the image buffer
#         st.experimental_rerun()
# else:
#     st.info("Please take a photo to continue.")

# # Submission
# if img_file_buffer and st.button("✅ Submit") and lat is not None and lon is not None:
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     # Encode image to base64 for display or storage
#     encoded_img = base64.b64encode(img_file_buffer.getvalue()).decode()
    
#     st.success("✅ Submission Successful!")
#     st.markdown(f"**Section:** {section}")
#     st.markdown(f"**Center Code:** {center_code}")
#     st.markdown(f"**Timestamp:** {timestamp}")
#     st.markdown(f"**Latitude:** {lat:.6f}")
#     st.markdown(f"**Longitude:** {lon:.6f}")

#     # Optional: Show submitted image again from base64
#     st.markdown('<h4>Submitted Photo:</h4>', unsafe_allow_html=True)
#     st.markdown(
#         f'<img src="data:image/png;base64,{encoded_img}" width="300">',
#         unsafe_allow_html=True
#     )

# elif img_file_buffer and (lat is None or lon is None):
#     st.error("❌ Unable to retrieve your location. Please allow location access and reload the page.")

# # Footer
# st.markdown("---")
# st.markdown("🔒 All data collected is used solely for verification purposes.")











# import streamlit as st
# from streamlit_js_eval import streamlit_js_eval
# from datetime import datetime
# from PIL import Image
# from io import BytesIO

# st.set_page_config(page_title="📸 Selfie Submission", layout="centered")

# st.title("📍📸 Selfie Submission App")
# st.markdown(
#     """
#     This app is for **official use only**. Please take your selfie and allow location access 📌.  
#     _Your data is used solely for verification purposes._
#     """
# )

# # --- SECTION SELECTION ---
# section = st.selectbox("📂 Select Section", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])

# # --- CENTER CODE ENTRY ---
# center_code = st.text_input("🏫 Enter Center Code", max_chars=10)

# # --- CAPTURE LOCATION ---
# st.subheader("📍 Location Access")

# latitude = None
# longitude = None

# if st.button("📍 Get Current Location"):
#     js_code = """
#     async () => {
#       return new Promise((resolve) => {
#         navigator.geolocation.getCurrentPosition(
#           (position) => {
#             resolve({
#               latitude: position.coords.latitude,
#               longitude: position.coords.longitude,
#             });
#           },
#           (error) => {
#             resolve({ error: error.message, code: error.code });
#           }
#         );
#       });
#     }
#     """

#     location = streamlit_js_eval(js_expressions=js_code, key="geo_location_manual")

#     if location:
#         if "error" not in location:
#             latitude = location["latitude"]
#             longitude = location["longitude"]
#             st.success(f"✅ Location captured: Latitude {latitude}, Longitude {longitude}")
#         else:
#             st.warning(f"⚠️ Location permission denied or unavailable. (Error: {location['error']})")
#     else:
#         st.info("📡 Could not retrieve location.")

# # --- MANUAL LOCATION INPUT (FALLBACK) ---
# use_manual = st.checkbox("🔧 Use manual location entry (fallback)")
# if use_manual:
#     latitude = st.number_input("🌐 Enter Latitude", format="%.6f")
#     longitude = st.number_input("🌐 Enter Longitude", format="%.6f")

# # --- PHOTO CAPTURE ---
# st.subheader("📸 Capture Photo")
# img_file = st.camera_input("Take a clear selfie")

# # --- Preview and Confirm ---
# if img_file:
#     st.image(img_file, caption="📷 Preview of your photo", use_column_width=True)
    
#     if st.button("🔁 Retake Photo"):
#         st.experimental_rerun()

#     if st.button("✅ Submit"):
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         st.success("✔️ Submission Successful!")

#         # Display submitted data
#         st.markdown("### 📝 Submitted Details")
#         st.markdown(f"**Section:** {section}")
#         st.markdown(f"**Center Code:** `{center_code}`")
#         st.markdown(f"**Timestamp:** {timestamp}")
#         st.markdown(f"**Latitude:** {latitude if latitude else 'Not Available'}")
#         st.markdown(f"**Longitude:** {longitude if longitude else 'Not Available'}")

#         st.image(img_file, caption="🖼️ Submitted Photo", use_column_width=True)

# # --- Footer Note ---
# st.markdown("---")
# st.markdown("🔒 _Photo and location data are only used for verification purposes. Your privacy is respected._")















import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime

st.set_page_config(page_title="📸 Selfie Submission", layout="centered")

st.title("📍📸 Selfie Submission App")
st.markdown("""
This app is for **official use only**. Please take your selfie and allow location access 📌.  
_Your data is used solely for verification purposes._
""")

# --- SECTION SELECTION ---
section = st.selectbox("📂 Select Section", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])

# --- CENTER CODE ENTRY ---
center_code = st.text_input("🏫 Enter Center Code", max_chars=10)

# --- LOCATION CAPTURE (HTML + JS) ---
location_html = """
<script>
function getLocation() {
  const status = document.getElementById("status");
  if (!navigator.geolocation) {
    status.innerText = '⚠️ Geolocation not supported.';
    return;
  }

  status.innerText = '📡 Getting location...';
  navigator.geolocation.getCurrentPosition(
    function(position) {
      document.getElementById("lat").value = position.coords.latitude.toFixed(6);
      document.getElementById("lon").value = position.coords.longitude.toFixed(6);
      status.innerText = `✅ Latitude: ${position.coords.latitude.toFixed(6)}, Longitude: ${position.coords.longitude.toFixed(6)}`;
    },
    async function(error) {
      let msg = '';
      switch(error.code) {
        case error.PERMISSION_DENIED:
          msg = "🛑 Permission denied.";
          break;
        case error.POSITION_UNAVAILABLE:
          msg = "📡 Position unavailable.";
          break;
        case error.TIMEOUT:
          msg = "⏳ Timeout occurred.";
          break;
        default:
          msg = "❓ Unknown error.";
      }
      status.innerText = msg;

      // Fallback to IP-based geolocation
      try {
        const res = await fetch('https://ipapi.co/json/ ');
        const data = await res.json();
        if (data && data.latitude && data.longitude) {
          document.getElementById("lat").value = data.latitude.toFixed(6);
          document.getElementById("lon").value = data.longitude.toFixed(6);
          status.innerText += `\n🌐 Fallback IP Geo: ${data.city}, ${data.region}`;
        } else {
          status.innerText += "\n❌ IP geolocation also failed.";
        }
      } catch (e) {
        console.error(e);
      }
    }
  );
}
</script>

<input type="text" id="lat" name="lat" hidden readonly>
<input type="text" id="lon" name="lon" hidden readonly>

<button onclick="getLocation()" style="padding: 10px; font-size: 16px;">📍 Get Current Location</button>
<p id="status" style="color: green;"></p>
"""

html(location_html, height=200)

latitude = st.text_input("Latitude", key="lat_input", disabled=True)
longitude = st.text_input("Longitude", key="lon_input", disabled=True)

# --- CAMERA INPUT (MOBILE FRIENDLY) ---
st.subheader("📸 Take a Clear Selfie")

uploaded_file = st.file_uploader("📷 Upload your selfie", type=["jpg", "jpeg", "png"], label_visibility="visible")

if uploaded_file:
    st.image(uploaded_file, caption="🖼️ Preview of your selfie", use_column_width=True)

# --- SUBMIT BUTTON ---
if st.button("✅ Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lat_val = st.session_state.get("lat", "")
    lon_val = st.session_state.get("lon", "")

    st.success("✔️ Submission Successful!")

    st.markdown("### 📝 Submitted Details")
    st.markdown(f"**Section:** {section}")
    st.markdown(f"**Center Code:** `{center_code}`")
    st.markdown(f"**Timestamp:** {timestamp}")
    st.markdown(f"**Latitude:** {latitude}")
    st.markdown(f"**Longitude:** {longitude}")

    if uploaded_file:
        st.image(uploaded_file, caption="📷 Submitted Selfie", use_column_width=True)

# --- Footer Note ---
st.markdown("---")
st.markdown("🔒 _Photo and location data are only used for verification purposes._")

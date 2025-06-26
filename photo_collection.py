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



















import streamlit as st
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval

# --- App Config ---
st.set_page_config(page_title="Exam Day Photo", page_icon="📸", layout="centered")

st.markdown("<h1 style='text-align: center;'>📸 Exam Day Photo Capture</h1>", unsafe_allow_html=True)
st.markdown("#### Select section, enter center code, capture selfie & auto-capture your location")
st.divider()

# --- Form Inputs ---
col1, col2 = st.columns(2)
with col1:
    section = st.selectbox("🗂️ Select Photo Section", ["Mock", "Examday Morning Selfie", "CSR", "Exit Selfie"])
with col2:
    center_code = st.text_input("🏷️ Enter Center Code")

# --- Get GeoLocation (automatically) ---
coords = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition", key="get_position", timeout=10)
geo_success = False

if coords and "coords" in coords:
    lat = coords['coords']['latitude']
    lon = coords['coords']['longitude']
    geo_success = True
else:
    lat, lon = "", ""

# --- Webcam Input ---
st.markdown("### 📷 Capture Your Selfie")
image = st.camera_input("")

# --- Preview & Confirmation ---
if image:
    st.markdown("### 🖼️ Photo Preview")
    st.image(image, caption="✅ Your Captured Photo", use_container_width=True)
    st.divider()

    col3, col4 = st.columns([1, 2])
    with col3:
        confirm = st.button("✅ Confirm & Submit", use_container_width=True)
    with col4:
        retake = st.button("🔁 Retake Photo", use_container_width=True)

    if confirm:
        if not center_code:
            st.error("🚫 Please enter the center code.")
        elif not geo_success:
            st.error("📍 Location access failed or was denied.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.success("✅ Photo confirmed successfully!")
            st.markdown(f"""
            **📄 Section:** `{section}`  
            **🏷️ Center Code:** `{center_code}`  
            **🕒 Time:** `{timestamp}`  
            **📍 Latitude:** `{lat}`  
            **📍 Longitude:** `{lon}`
            """)
    if retake:
        st.experimental_rerun()
else:
    st.info("📸 Please take a selfie using the camera above.")

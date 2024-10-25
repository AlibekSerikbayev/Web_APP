# # import streamlit as st
# # import pathlib
# # import plotly.express as px

# # # Try to import fastai
# # try:
# #     from fastai.vision.all import *
# # except ImportError:
# #     st.error("The 'fastai' library is not installed. Please install it using 'pip install fastai'.")
# #     st.stop()

# # # Fix for Windows path issue
# # temp = pathlib.PosixPath
# # pathlib.PosixPath = pathlib.WindowsPath

# # # Add instructions for running the app
# # st.set_page_config(page_title="Transport Image Classifier")
# # st.title("Transport Image Classifier")
# # st.write("To run this app, use the command: `streamlit run app.py` in your terminal.")

# # # Modelni yuklash (Load the model)
# # @st.cache_resource
# # def load_model():
# #     return load_learner("transport_model.pkl")

# # try:
# #     learner = load_model()
# # except FileNotFoundError:
# #     st.error("Model file 'transport_model.pkl' not found. Please make sure it's in the same directory as this script.")
# #     st.stop()

# # # Rasm yuklash (Upload image)
# # uploaded_file = st.file_uploader("Rasm yuklang", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     # Yuklangan rasmni o'qish (Read uploaded image)
# #     img = PILImage.create(uploaded_file)

# #     # Rasmni aniqlash (Predict image)
# #     try:
# #         pred, pred_idx, probs = learner.predict(img)
        
# #         # Natijani ko'rsatish (Show results)
# #         st.image(img, caption='Yuklangan rasm', use_column_width=True)
# #         st.write(f"Bu rasm: {pred} (Ishonch: {probs[pred_idx]:.2f})")
# #     except Exception as e:
# #         st.error(f"Rasmni aniqlashda xato: {e}")


# import streamlit as st
# import pathlib
# import plotly.express as px

# # Add instructions for running the app
# st.set_page_config(page_title="Transport Image Classifier")

# # Try to import fastai and check version
# try:
#     from fastai.vision.all import *
#     import fastai
#     st.sidebar.info(f"Using fastai version: {fastai.__version__}")
# except ImportError:
#     st.error("The 'fastai' library is not installed. Please install it using 'pip install fastai'.")
#     st.stop()

# # Fix for Windows path issue
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

# st.title("Transport Image Classifier")
# st.write("To run this app, use the command: `streamlit run app.py` in your terminal.")

# # Modelni yuklash (Load the model)
# @st.cache_resource
# def load_model():
#     try:
#         learn = load_learner("transport_model.pkl")
#         # TrainEvalCallback ni o'chirish
#         learn.remove_cb(TrainEvalCallback)
#         return learn
#     except Exception as e:
#         st.error(f"Error loading model: {e}")
#         st.info("Try updating fastai or recreating the model with the current version.")
#         return None

# # Update the model loading section
# try:
#     learner = load_model()
#     if learner is None:
#         st.stop()
# except FileNotFoundError:
#     st.error("Model file 'model1.pkl' not found. Please make sure it's in the same directory as this script.")
#     st.stop()

# # Add a sidebar for additional information
# st.sidebar.title("About")
# st.sidebar.info("This app classifies images of various modes of transportation.")
# st.sidebar.info("Upload an image to see the prediction.")

# # Rasm yuklash (Upload image)
# uploaded_file = st.file_uploader("Rasm yuklang (Upload an image)", type=["jpg", "jpeg", "png"])

# # ... existing code ...

# if uploaded_file is not None:
#     # Yuklangan rasmni o'qish (Read uploaded image)
#     img = PILImage.create(uploaded_file)

#     # Debugging: Check the type of learner
#     st.write(f"Type of learner: {type(learner)}")

#     # Rasmni aniqlash (Predict image)
#     try:
#         # Ensure learner is a valid Learner object
#         if isinstance(learner, Learner):
#             pred, pred_idx, probs = learner.predict(img)
            
#             # Natijani ko'rsatish (Show results)
#             st.image(img, caption='Yuklangan rasm', use_column_width=True)
#             st.write(f"Bu rasm: {pred} (Ishonch: {probs[pred_idx]:.2f})")

#             # Add a bar chart to visualize probabilities
#             top_probs, top_labels = learner.get_preds(dl=[(img,)])[0][0].topk(k=5)
#             prob_dict = {learner.dls.vocab[i]: float(p) for i, p in zip(top_labels, top_probs)}
            
#             fig = px.bar(x=list(prob_dict.keys()), y=list(prob_dict.values()), 
#                          labels={'x': 'Class', 'y': 'Probability'},
#                          title='Top 5 Predictions')
#             st.plotly_chart(fig)
#         else:
#             st.error("Invalid learner object. Please check the model loading process.")
#     except Exception as e:
#         st.error(f"Rasmni aniqlashda xato: {e}")

# # ... rest of the existing code ...



# # if uploaded_file is not None:
# #     # Yuklangan rasmni o'qish (Read uploaded image)
# #     img = PILImage.create(uploaded_file)

# #     # Rasmni aniqlash (Predict image)
# #     try:
# #         pred, pred_idx, probs = learner.predict(img)
        
# #         # Natijani ko'rsatish (Show results)
# #         st.image(img, caption='Yuklangan rasm', use_column_width=True)
# #         st.write(f"Bu rasm: {pred} (Ishonch: {probs[pred_idx]:.2f})")

# #         # Add a bar chart to visualize probabilities
# #         top_probs, top_labels = learner.get_preds(dl=[(img,)])[0][0].topk(k=5)
# #         prob_dict = {learner.dls.vocab[i]: float(p) for i, p in zip(top_labels, top_probs)}
        
# #         fig = px.bar(x=list(prob_dict.keys()), y=list(prob_dict.values()), 
# #                      labels={'x': 'Class', 'y': 'Probability'},
# #                      title='Top 5 Predictions')
# #         st.plotly_chart(fig)

# #     except Exception as e:
# #         st.error(f"Rasmni aniqlashda xato: {e}")






# import streamlit as st
# import pathlib
# import plotly.express as px

# # Add instructions for running the app
# st.set_page_config(page_title="Transport Image Classifier")

# # Try to import fastai and check version
# try:
#     from fastai.vision.all import *
#     import fastai
#     st.sidebar.info(f"Using fastai version: {fastai.__version__}")
# except ImportError:
#     st.error("The 'fastai' library is not installed. Please install it using 'pip install fastai'.")
#     st.stop()

# # Fix for Windows path issue
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

# st.title("Transport Image Classifier")
# st.write("To run this app, use the command: `streamlit run app.py` in your terminal.")

# # Modelni yuklash (Load the model)
# @st.cache_resource
# def load_model():
#     try:
#         learn = load_learner("model1.pkl")
#         # TrainEvalCallback ni o'chirish
#         learn.remove_cb(TrainEvalCallback)
#         return learn
#     except Exception as e:
#         st.error(f"Error loading model: {e}")
#         st.info("Try updating fastai or recreating the model with the current version.")
#         return None

# # Update the model loading section
# try:
#     learner = load_model()
#     if learner is None:
#         st.stop()
# except FileNotFoundError:
#     st.error("Model file 'transport_model.pkl' not found. Please make sure it's in the same directory as this script.")
#     st.stop()

# # Add a sidebar for additional information
# st.sidebar.title("About")
# st.sidebar.info("This app classifies images of various modes of transportation.")
# st.sidebar.info("Upload an image to see the prediction.")

# # Rasm yuklash (Upload image)
# uploaded_file = st.file_uploader("Rasm yuklang (Upload an image)", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Yuklangan rasmni o'qish (Read uploaded image)
#     img = PILImage.create(uploaded_file)

#     # Debugging: Check the type of learner
#     st.write(f"Type of learner: {type(learner)}")

#     # Rasmni aniqlash (Predict image)
#     try:
#         # Ensure learner is a valid Learner object
#         if isinstance(learner, Learner):
#             pred, pred_idx, probs = learner.predict(img)
            
#             # Natijani ko'rsatish (Show results)
#             st.image(img, caption='Yuklangan rasm', use_column_width=True)
#             st.write(f"Bu rasm: {pred} (Ishonch: {probs[pred_idx]:.2f})")

#             # Add a bar chart to visualize probabilities
#             preds = learner.get_preds(dl=[(img,)], with_decoded=True)
#             top_probs, top_labels = preds[0][0].topk(k=5)
#             prob_dict = {learner.dls.vocab[i]: float(p) for i, p in zip(top_labels, top_probs)}
            
#             fig = px.bar(x=list(prob_dict.keys()), y=list(prob_dict.values()), 
#                          labels={'x': 'Class', 'y': 'Probability'},
#                          title='Top 5 Predictions')
#             st.plotly_chart(fig)
#         else:
#             st.error("Invalid learner object. Please check the model loading process.")
#     except Exception as e:
#         st.error(f"Rasmni aniqlashda xato: {e}")








import streamlit as st
from fastai.vision.all import *
import pathlib
import plotly.express as px

# Fix for Windows path issue
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Set page configuration
st.set_page_config(page_title="Transport Image Classifier")

# Add a sidebar for additional information
st.sidebar.title("About")
st.sidebar.info("This app classifies images of various modes of transportation.")
st.sidebar.info("Upload an image to see the prediction.")

# Try to import fastai and check version
try:
    import fastai
    st.sidebar.info(f"Using fastai version: {fastai.__version__}")
except ImportError:
    st.error("The 'fastai' library is not installed. Please install it using 'pip install fastai'.")
    st.stop()

# Modelni yuklash (Load the model)
@st.cache_resource
def load_model():
    try:
        learn = load_learner("transport_model.pkl")
        # Remove TrainEvalCallback if it exists
        learn.cbs = [cb for cb in learn.cbs if not isinstance(cb, TrainEvalCallback)]
        return learn
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Try updating fastai or recreating the model with the current version.")
        return None

# Load the model
try:
    learner = load_model()
    if learner is None:
        st.stop()
except FileNotFoundError:
    st.error("Model file 'transport_model.pkl' not found. Please make sure it's in the same directory as this script.")
    st.stop()

# Rasm yuklash (Upload image)
uploaded_file = st.file_uploader("Rasm yuklang (Upload an image)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Yuklangan rasmni o'qish (Read uploaded image)
    img = PILImage.create(uploaded_file)
    
    # Debugging: Learner turini tekshirish (Check the type of learner)
    st.write(f"Learner turi: {type(learner)}")

    # Rasmni aniqlash (Predict image)
    try:
        # Ensure learner is a valid Learner object
        if isinstance(learner, Learner):
            pred, pred_idx, probs = learner.predict(img)
            
            # Natijani ko'rsatish (Show results)
            st.image(img, caption='Yuklangan rasm', use_column_width=True)
            st.write(f"Bu rasm: {pred} (Ishonch: {probs[pred_idx]:.2f})")

            # Add a bar chart to visualize probabilities
            preds = learner.get_preds(dl=[(img,)], with_decoded=True)
            top_probs, top_labels = preds[0][0].topk(k=5)
            prob_dict = {learner.dls.vocab[i]: float(p) for i, p in zip(top_labels, top_probs)}
            
            fig = px.bar(x=list(prob_dict.keys()), y=list(prob_dict.values()), 
                         labels={'x': 'Class', 'y': 'Probability'},
                         title='Top 5 Predictions')
            st.plotly_chart(fig)
        else:
            st.error("Learner obyektida xato. Model yuklash jarayonini tekshiring.")
    except Exception as e:
        st.error(f"Rasmni aniqlashda xato: {e}")
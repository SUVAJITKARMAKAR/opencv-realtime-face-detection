import streamlit as stream
import pandas as panda
import shutil
import time
import os


# PAGE CONFIGURATION
stream.set_page_config(page_title="RECORDS", page_icon=":eye", layout="wide")

#FUNCTION DEFINITION 
def save_uploaded_files(uploaded_files):
      for uploaded_file in uploaded_files:
            with open(os.path.join("records", uploaded_file.name), "wb") as save:
                  save.write(uploaded_file.getbuffer())

def display_excel_table(file_path):
      dframe = panda.read_excel(file_path)
      stream.write(dframe)


def delete_uploaded_files():
      folder = "records"
      for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            try:
                  if os.path.isfile(file_path):
                        os.unlink(file_path)
            except Exception as e:
                  stream.error(f"ERROR DELETING {file_path}: {e}")


def main():
      stream.header("STUDENT RECORDS")

      #CREATING A DIRECTORY FOR UPLOADED RECORD FILES 
      if not os.path.exists("records"):
            os.mkdir("records")

      #CREATING A FILE UPLOADER
      uploaded_files = stream.file_uploader("UPLOAD THE STUDENT RECORDS FILE", type=["xlsx"], accept_multiple_files=True)

      #CHECK 
      if uploaded_files:
            save_uploaded_files(uploaded_files)

            #DISPLAYING THE UPLOADED FILES 
            success_message = stream.success("RECORDS UPLOADED SUCCESSFULLY")
            time.sleep(3)
            success_message.empty()


      #SELECTING THE RECORD TO DISPLAY
      selected_file = stream.selectbox("SELECT A RECORD : ", os.listdir("records"))

      if selected_file:
            stream.markdown("### TABLE : ")
            display_excel_table(os.path.join("records", selected_file))

      #DELETE BUTTON TO DELETE THE FOLDER STRUCTURE
      if stream.button("DELETE ALL RECORDS"):
            delete_uploaded_files()
            deleted_warning__message = stream.warning("ALL UPLOADED FILES DELETED SUCCESSFULLY")
            time.sleep(3)
            deleted_warning__message.empty()

if __name__ == '__main__':
      main()
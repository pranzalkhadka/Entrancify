import streamlit as st

eligibility_img_path = "/home/pranjal/Downloads/Entrancify/Images/eligibility.png"
admission_img_path = "/home/pranjal/Downloads/Entrancify/Images/admission.png"
image_path1 = "/home/pranjal/Downloads/Entrancify/Images/1.png"
image_path2 = "/home/pranjal/Downloads/Entrancify/Images/2.png"
image_path3 = "/home/pranjal/Downloads/Entrancify/Images/3.png"
image_path4 = "/home/pranjal/Downloads/Entrancify/Images/Reserved.png"

class Overview:

    def program_overview():
        
        st.title("About the Course")
        st.write("""BSc CSIT (Bachelor of Science in Computer Science and Information Technology) 
             is an extensive four-year undergraduate program, spanning eight semesters, offered by Tribhuvan University (TU). 
             This curriculum is designed to provide students with a comprehensive grasp of various IT disciplines, 
             ranging from Networking, Artificial Intelligence, and Database Management to Software Development, Programming, Computing, 
             and Data Structures & Algorithms.
             The mission of the B.Sc. CSIT course is to prepare the students to pursue career advancement in the field of information technology.
              At the completion of this degree, a student will be able to design the real world e-media products or create technical solutions to
              hardware and software problems, depending on the chosen area of specialization and electives.""")

        st.title("Eligibility")
        st.image(eligibility_img_path, use_column_width=True)

        st.title("Admission Criteria")
        st.image(admission_img_path, use_column_width=True)

        st.title("Seating Capacities in Different Colleges")
        st.image(image_path1, caption="List1", use_column_width=True)
        st.image(image_path2, caption="List2", use_column_width=True)
        st.image(image_path3, caption="List3", use_column_width=True)

        st.title("Distribution of Reserved Seats")
        st.image(image_path4, caption="reserved seats", use_column_width=True)
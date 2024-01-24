import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utility.utils import topPerformers, cutoff_rank, cutoff_rank_analysis

patan_img_path = "/home/pranjal/Downloads/final_project/Images/patan_college.jpeg"

patan_2080_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2080/first_list/patan_2080_first.csv")
patan_2080_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2080/second_list/patan_2080_second.csv")
patan_2079_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2079/first_list/patan_2079_first.csv")
patan_2079_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2079/second_list/patan_2079_second.csv")
patan_2078_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2078/first_list/patan_2078_first.csv")
patan_2078_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2078/second_list/patan_2078_second.csv")
patan_2077_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2077/first_list/patan_2077_first.csv")
patan_2077_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2077/second_list/patan_2077_second.csv")


class Patan:
    def patan_analysis():
            st.sidebar.header("Patan Multiple Campus")
            st.title("About")
            st.write("""Patan Multiple Campus was established on 2nd September 1954 AD under the Ministry of Education of Nepal.
             Patan Multiple Campus was founded with the name “Patan Inter College” and later renamed to Patan Multiple Campus
              after the implementation of the National Education System in 2030 BS (1973 AD).
             In 1973 AD, the Campus was added to Tribhuvan University as a constituent campus.
              The campus occupies about 27,296 sq. m area.
              Patan Multiple Campus is well facilitated with sufficient classrooms with spacious premises 
             that fit all the required infrastructures of the faculties.
             """)
            st.image(patan_img_path, use_column_width=True)

            years = [2077, 2078, 2079, 2080]
            selected_year = st.sidebar.selectbox("Select Year",years)

            merit_list = ["first", "second"]
            selected_list = st.sidebar.selectbox("Select Merit List",merit_list)


            if selected_year == 2080 and selected_list == "first":
                top_performers_data = topPerformers(patan_2080_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2080_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_first, patan_2078_first, patan_2079_first, patan_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())


            elif selected_year == 2080 and selected_list == "second":
                top_performers_data = topPerformers(patan_2080_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2080_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_second, patan_2078_second, patan_2079_second, patan_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())


            elif selected_year == 2079 and selected_list == "first":
                top_performers_data = topPerformers(patan_2079_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2079_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_first, patan_2078_first, patan_2079_first, patan_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())

    
            elif selected_year == 2079 and selected_list == "second":
                top_performers_data = topPerformers(patan_2079_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2079_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_second, patan_2078_second, patan_2079_second, patan_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())


            elif selected_year == 2078 and selected_list == "first":
                top_performers_data = topPerformers(patan_2078_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2078_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_first, patan_2078_first, patan_2079_first, patan_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())

    
            elif selected_year == 2078 and selected_list == "second":
                top_performers_data = topPerformers(patan_2078_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2078_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_second, patan_2078_second, patan_2079_second, patan_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())

    
            elif selected_year == 2077 and selected_list == "first":
                top_performers_data = topPerformers(patan_2077_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2077_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_first, patan_2078_first, patan_2079_first, patan_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())

    
            elif selected_year == 2077 and selected_list == "second":
                top_performers_data = topPerformers(patan_2077_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(patan_2077_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(patan_2077_second, patan_2078_second, patan_2079_second, patan_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')

                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))

                st.pyplot(plt.gcf())
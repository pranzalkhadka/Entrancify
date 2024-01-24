import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utility.utils import topPerformers, cutoff_rank, cutoff_rank_analysis, statistics, common_merit_lists

bhaktapur_img_path = "/home/pranjal/Downloads/final_project/Images/bhaktapur_college.jpg"

college_website_url = "https://bkmc.tu.edu.np"

bhaktapur_2080_first = pd.read_csv("/home/pranjal/Downloads/final_project/2080/first_list/bhaktapur_2080_first.csv")
bhaktapur_2080_second = pd.read_csv("/home/pranjal/Downloads/final_project/2080/second_list/bhaktapur_2080_second.csv")
bhaktapur_2079_first = pd.read_csv("/home/pranjal/Downloads/final_project/2079/first_list/bhaktapur_2079_first.csv")
bhaktapur_2079_second = pd.read_csv("/home/pranjal/Downloads/final_project/2079/second_list/bhaktapur_2079_second.csv")
bhaktapur_2078_first = pd.read_csv("/home/pranjal/Downloads/final_project/2078/first_list/bhaktapur_2078_first.csv")
bhaktapur_2078_second = pd.read_csv("/home/pranjal/Downloads/final_project/2078/second_list/bhaktapur_2078_second.csv")
bhaktapur_2077_first = pd.read_csv("/home/pranjal/Downloads/final_project/2077/first_list/bhaktapur_2077_first.csv")
bhaktapur_2077_second = pd.read_csv("/home/pranjal/Downloads/final_project/2077/second_list/bhaktapur_2077_second.csv")


class Bhaktapur:

    def bhaktapur_analysis():
            
            st.sidebar.header("Bhaktapur Multiple Campus")
            st.title("About")
            st.write("""Bhaktapur Multiple Campus (BKMC), was established in 1959 in Bhaktapur, 
             situated at the heart of Bhaktapur Municipality, Bhaktapur, Bagmati Province, as an educational institute 
             to educate young Nepalese women and men entering the field of Information Technology, Science, Humanities and Management.
              Bhaktapur Multiple Campus is the pioneer constituent campus of Tribhuvan University (TU)
              which has become one of the pioneer educational organizations in Nepal since its establishment. 
             Within Five decades, the campus gradually expanded its academic program from PCL to Master in Humanities and Management.
              Bhaktapur Multiple Campus is an academic center of excellence through the foundation of integrated subjects 
             with its specialization in Information technology, Finance, Accounting, Management, 
             Banking, Physics, Chemistry, Biology and Mathematics Sociology and Rural Development. 
             """)
            
            st.image(bhaktapur_img_path, use_column_width=True)

            st.subheader("Find more here...")
            st.markdown(college_website_url)

            years = [2077, 2078, 2079, 2080]
            selected_year = st.sidebar.selectbox("Select Year",years)

            merit_list = ["first", "second"]
            selected_list = st.sidebar.selectbox("Select Merit List",merit_list)


            if selected_year == 2080 and selected_list == "first":
                top_performers_data = topPerformers(bhaktapur_2080_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2080_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_first, bhaktapur_2078_first, bhaktapur_2079_first, bhaktapur_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2080_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2080_first, bhaktapur_2080_second))


            elif selected_year == 2080 and selected_list == "second":
                top_performers_data = topPerformers(bhaktapur_2080_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2080_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_second, bhaktapur_2078_second, bhaktapur_2079_second, bhaktapur_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2080_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2080_first, bhaktapur_2080_second))


            elif selected_year == 2079 and selected_list == "first":
                top_performers_data = topPerformers(bhaktapur_2079_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2079_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_first, bhaktapur_2078_first, bhaktapur_2079_first, bhaktapur_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2079_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2079_first, bhaktapur_2079_second))

    
            elif selected_year == 2079 and selected_list == "second":
                top_performers_data = topPerformers(bhaktapur_2079_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2079_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_second, bhaktapur_2078_second, bhaktapur_2079_second, bhaktapur_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2079_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2079_first, bhaktapur_2079_second))

    
            elif selected_year == 2078 and selected_list == "first":
                top_performers_data = topPerformers(bhaktapur_2078_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2078_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_first, bhaktapur_2078_first, bhaktapur_2079_first, bhaktapur_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2078_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2078_first, bhaktapur_2078_second))

    
            elif selected_year == 2078 and selected_list == "second":
                top_performers_data = topPerformers(bhaktapur_2078_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2078_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_second, bhaktapur_2078_second, bhaktapur_2079_second, bhaktapur_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2078_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2078_first, bhaktapur_2078_second))


            elif selected_year == 2077 and selected_list == "first":
                top_performers_data = topPerformers(bhaktapur_2077_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2077_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_first, bhaktapur_2078_first, bhaktapur_2079_first, bhaktapur_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2077_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2077_first, bhaktapur_2077_second))

    
            elif selected_year == 2077 and selected_list == "second":
                top_performers_data = topPerformers(bhaktapur_2077_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(bhaktapur_2077_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(bhaktapur_2077_second, bhaktapur_2078_second, bhaktapur_2079_second, bhaktapur_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(bhaktapur_2077_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(bhaktapur_2077_first, bhaktapur_2077_second))
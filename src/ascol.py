import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utility.utils import topPerformers, cutoff_rank, cutoff_rank_analysis, statistics, common_merit_lists

ascol_img_path = "https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/Images/amrit_college.jpg"

college_website_url = "https://ac.tu.edu.np"

# ascol_2080_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2080/first_list/ascol_2080_first.csv")
# ascol_2080_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2080/second_list/ascol_2080_second.csv")
# ascol_2079_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2079/first_list/ascol_2079_first.csv")
# ascol_2079_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2079/second_list/ascol_2079_second.csv")
# ascol_2078_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2078/first_list/ascol_2078_first.csv")
# ascol_2078_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2078/second_list/ascol_2078_second.csv")
# ascol_2077_first = pd.read_csv("/home/pranjal/Downloads/Entrancify/2077/first_list/ascol_2077_first.csv")
# ascol_2077_second = pd.read_csv("/home/pranjal/Downloads/Entrancify/2077/second_list/ascol_2077_second.csv")


ascol_2080_first = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2080/first_list/ascol_2080_first.csv", index_col=0)
ascol_2080_second = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2080/second_list/ascol_2080_second.csv", index_col=0)
ascol_2079_first = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2079/first_list/ascol_2079_first.csv", index_col=0)
ascol_2079_second = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2079/second_list/ascol_2079_second.csv", index_col=0)
ascol_2078_first = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2078/first_list/ascol_2078_first.csv", index_col=0)
ascol_2078_second = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2078/second_list/ascol_2078_second.csv", index_col=0)
ascol_2077_first = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2077/first_list/ascol_2077_first.csv", index_col=0)
ascol_2077_second = pd.read_csv("https://raw.githubusercontent.com/pranzalkhadka/Entrancify/main/Data/2077/second_list/ascol_2077_second.csv", index_col=0)


class Ascol:

    def ascol_analysis():
            
            st.sidebar.header("Amrit Science Campus")
            st.title("About")
            st.write("""Amrit Campus is the first science campus of Nepal, located in Lainchaur, Kathmandu.
             It was formerly known as Public Science College (PUSCOL).
             ASCOL situated in the heart of Kathmandu Valley-Thamel, is one of the few pure science campus of the country.
             The campus is a governmental institution and is affiliated to Tribhuvan University.
             """)
            
            st.image(ascol_img_path, use_column_width=True)

            st.subheader("Find more here...")
            st.markdown(college_website_url)

            years = [2077, 2078, 2079, 2080]
            selected_year = st.sidebar.selectbox("Select Year",years)

            merit_list = ["first", "second"]
            selected_list = st.sidebar.selectbox("Select Merit List",merit_list)


            if selected_year == 2080 and selected_list == "first":
                top_performers_data = topPerformers(ascol_2080_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2080_first)
                st.title("Cutoff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_first, ascol_2078_first, ascol_2079_first, ascol_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2080_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2080_first, ascol_2080_second))


            elif selected_year == 2080 and selected_list == "second":
                top_performers_data = topPerformers(ascol_2080_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2080_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_second, ascol_2078_second, ascol_2079_second, ascol_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2080_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2080_first, ascol_2080_second))


            elif selected_year == 2079 and selected_list == "first":
                top_performers_data = topPerformers(ascol_2079_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2079_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_first, ascol_2078_first, ascol_2079_first, ascol_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2079_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2079_first, ascol_2079_second))

    
            elif selected_year == 2079 and selected_list == "second":
                top_performers_data = topPerformers(ascol_2079_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2079_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_second, ascol_2078_second, ascol_2079_second, ascol_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2079_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2079_first, ascol_2079_second))


            elif selected_year == 2078 and selected_list == "first":
                top_performers_data = topPerformers(ascol_2078_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2078_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_first, ascol_2078_first, ascol_2079_first, ascol_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2078_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2078_first, ascol_2078_second))

    
            elif selected_year == 2078 and selected_list == "second":
                top_performers_data = topPerformers(ascol_2078_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2078_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_second, ascol_2078_second, ascol_2079_second, ascol_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2078_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2078_first, ascol_2078_second))

    
            elif selected_year == 2077 and selected_list == "first":
                top_performers_data = topPerformers(ascol_2077_first)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2077_first)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_first, ascol_2078_first, ascol_2079_first, ascol_2080_first)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2077_first))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2077_first, ascol_2077_second))

    
            elif selected_year == 2077 and selected_list == "second":
                top_performers_data = topPerformers(ascol_2077_second)
                st.title(f"Top 10 Performers")
                st.table(top_performers_data)

                cutoff = cutoff_rank(ascol_2077_second)
                st.title("CutOff Rank Analysis")
                st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

                cutoff_rank_df = cutoff_rank_analysis(ascol_2077_second, ascol_2078_second, ascol_2079_second, ascol_2080_second)

                plt.figure(figsize=(10, 6))
                plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
                plt.title('Cutoff Rank Trend')
                plt.xlabel('Year')
                plt.ylabel('Rank')
                plt.grid(True)
                plt.xticks(cutoff_rank_df['Year'].astype(int))
                st.pyplot(plt.gcf())

                st.title(f"Statistical Breakdown")
                st.table(statistics(ascol_2077_second))

                st.title(f"Applicants in both First and Second Merit List")
                st.table(common_merit_lists(ascol_2077_first, ascol_2077_second))
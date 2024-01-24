import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utility.utils import topPerformers, cutoff_rank, cutoff_rank_analysis2, statistics, common_merit_lists

st_xavier_img_path = "/home/pranjal/Downloads/final_project/Images/st_xavier_college.jpeg"

college_website_url = "https://www.sxc.edu.np/"

st_xavier_2080_first = pd.read_csv("/home/pranjal/Downloads/final_project/2080/first_list/st_xavier_2080_first.csv")
st_xavier_2080_second = pd.read_csv("/home/pranjal/Downloads/final_project/2080/second_list/st_xavier_2080_second.csv")
st_xavier_2079_first = pd.read_csv("/home/pranjal/Downloads/final_project/2079/first_list/st_xavier_2079_first.csv")
st_xavier_2079_second = pd.read_csv("/home/pranjal/Downloads/final_project/2079/second_list/st_xavier_2079_second.csv")
st_xavier_2078_first = pd.read_csv("/home/pranjal/Downloads/final_project/2078/first_list/st_xavier_2078_first.csv")
st_xavier_2078_second = pd.read_csv("/home/pranjal/Downloads/final_project/2078/second_list/st_xavier_2078_second.csv")


class StXavier:

    def stxavier_analysis():
        
        st.sidebar.header("St. Xavier's College")
        st.title("About")
        st.write("""St. Xavier's College, Maitighar is a private, Jesuit, co-educational secondary and tertiary educational institution 
             run by the Nepal Region of the Society of Jesus in Kathmandu, Nepal. It was founded by the Jesuits in 1988 AD. 
             Since its very inception the college has been offering quality education and has contributed to the development of the nation 
             through the production of highly qualified human resources.
             """)
        
        st.image(st_xavier_img_path, use_column_width = True)

        st.subheader("Find more here...")
        st.markdown(college_website_url)

        years = [2078, 2079, 2080]
        selected_year = st.sidebar.selectbox("Select Year",years)

        merit_list = ["first", "second"]
        selected_list = st.sidebar.selectbox("Select Merit List",merit_list)


        if selected_year == 2080 and selected_list == "first":
            top_performers_data = topPerformers(st_xavier_2080_first)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2080_first)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_first, st_xavier_2079_first, st_xavier_2080_first)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2080_first))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2080_first, st_xavier_2080_second))


        elif selected_year == 2080 and selected_list == "second":
            top_performers_data = topPerformers(st_xavier_2080_second)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2080_second)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_second, st_xavier_2079_second, st_xavier_2080_second)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2080_second))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2080_first, st_xavier_2080_second))


        elif selected_year == 2079 and selected_list == "first":
            top_performers_data = topPerformers(st_xavier_2079_first)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2079_first)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_first, st_xavier_2079_first, st_xavier_2080_first)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2079_first))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2079_first, st_xavier_2079_second))

    
        elif selected_year == 2079 and selected_list == "second":
            top_performers_data = topPerformers(st_xavier_2079_second)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2079_second)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_second, st_xavier_2079_second, st_xavier_2080_second)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2079_second))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2079_first, st_xavier_2079_second))


        elif selected_year == 2078 and selected_list == "first":
            top_performers_data = topPerformers(st_xavier_2078_first)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2078_first)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_first, st_xavier_2079_first, st_xavier_2080_first)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2078_first))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2078_first, st_xavier_2078_second))

    
        elif selected_year == 2078 and selected_list == "second":
            top_performers_data = topPerformers(st_xavier_2078_second)
            st.title(f"Top 10 Performers")
            st.table(top_performers_data)

            cutoff = cutoff_rank(st_xavier_2078_second)
            st.title("CutOff Rank Analysis")
            st.subheader(f"Cutoff Rank for the year {selected_year} : {cutoff}")

            cutoff_rank_df = cutoff_rank_analysis2(st_xavier_2078_second, st_xavier_2079_second, st_xavier_2080_second)

            plt.figure(figsize=(10, 6))
            plt.plot(cutoff_rank_df['Year'], cutoff_rank_df['Cutoff_Rank'], marker='o', linestyle='-', color='b')
            plt.title('Cutoff Rank Trend')
            plt.xlabel('Year')
            plt.ylabel('Rank')
            plt.grid(True)
            plt.xticks(cutoff_rank_df['Year'].astype(int))
            st.pyplot(plt.gcf())

            st.title(f"Statistical Breakdown")
            st.table(statistics(st_xavier_2078_second))

            st.title(f"Applicants in both First and Second Merit List")
            st.table(common_merit_lists(st_xavier_2078_first, st_xavier_2078_second))
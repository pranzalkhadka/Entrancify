import pandas as pd


def topPerformers(df):


    df = df[['Roll No', 'Rank']]
    df_sorted = df.sort_values(by='Rank')
    top_10_performers = df_sorted.head(10)

    return top_10_performers



def cutoff_rank(df):
    

    df = df.drop(["S.No."],axis =1)
    if 'Remarks' in df.columns:
        df = df.drop(columns=['Remarks'])
    cutoff_rank = df['Rank'].max()

    return cutoff_rank



def cutoff_rank_analysis(df_2077, df_2078, df_2079, df_2080):


    data = {
    'Year': [2077, 2078, 2079, 2080],  
    'Cutoff_Rank': [cutoff_rank(df_2077), cutoff_rank(df_2078), cutoff_rank(df_2079), cutoff_rank(df_2080)] 
}

    cutoff_rank_df = pd.DataFrame(data)

    return cutoff_rank_df



def cutoff_rank_analysis2(df_2078, df_2079, df_2080):


    data = {
    'Year': [2078, 2079, 2080],  
    'Cutoff_Rank': [cutoff_rank(df_2078), cutoff_rank(df_2079), cutoff_rank(df_2080)] 
}

    cutoff_rank_df = pd.DataFrame(data)

    return cutoff_rank_df


def statistics(df):


    df_rank = df["Rank"].describe()
    df_rank = df_rank.astype(int)

    return df_rank


def common_merit_lists(df_first_list, df_second_list):


    common_rows_df = df_first_list[df_first_list['Roll No'].isin(df_second_list['Roll No'])]
    common_subset = common_rows_df[['Roll No', 'Rank']]

    return common_subset
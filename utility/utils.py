import pandas as pd


def topPerformers(df):

    df = df.drop(["S.No."],axis =1)
    df = df.drop(["Name"],axis =1)
    if 'Darta No' in df.columns:
        df = df.drop(columns=['Darta No'])
    if 'Remarks' in df.columns:
        df = df.drop(columns=['Remarks'])
    if 'Score' in df.columns:
        df = df.drop(columns=['Score'])
    df_sorted = df.sort_values(by='Rank')
    top_10_performers = df_sorted.head(10)
    top_10_performers =  top_10_performers[['Rank', 'Roll No']].reset_index(drop=True)
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
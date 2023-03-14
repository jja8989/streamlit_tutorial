import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Plot")

st.markdown("---")


with st.echo():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.line_chart(chart_data)
    st.area_chart(chart_data)
    st.bar_chart(chart_data)
st.markdown("---")

with st.echo():
    fig = sns.boxplot(data=chart_data)
    st.pyplot(fig)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    def __init__(self):
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def create_pie_chart(self, data, category_column, amount_column, title="Expense Distribution"):
        """
        Create a pie chart from dataframe
        """
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            data_grouped = data.groupby(category_column)[amount_column].sum()
            ax.pie(data_grouped, labels=data_grouped.index, autopct='%1.1f%%', startangle=90)
            ax.set_title(title, fontsize=16, fontweight='bold')
            st.pyplot(fig)
            return True
        except Exception as e:
            st.error(f"❌ Error creating pie chart: {str(e)}")
            return False
    
    def create_bar_chart(self, data, x_column, y_column, title="Category Summary"):
        """
        Create a bar chart from dataframe
        """
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            data_grouped = data.groupby(x_column)[y_column].sum().sort_values(ascending=False)
            data_grouped.plot(kind='bar', ax=ax, color='steelblue')
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel(x_column, fontsize=12)
            ax.set_ylabel(y_column, fontsize=12)
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
            return True
        except Exception as e:
            st.error(f"❌ Error creating bar chart: {str(e)}")
            return False
    
    def create_line_chart(self, data, x_column, y_column, title="Trend Over Time"):
        """
        Create a line chart from dataframe
        """
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            data_sorted = data.sort_values(x_column)
            ax.plot(data_sorted[x_column], data_sorted[y_column], marker='o', linewidth=2, color='darkblue')
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel(x_column, fontsize=12)
            ax.set_ylabel(y_column, fontsize=12)
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
            return True
        except Exception as e:
            st.error(f"❌ Error creating line chart: {str(e)}")
            return False
    
    def create_dashboard(self, data):
        """
        Create a comprehensive dashboard from dataframe
        """
        try:
            st.subheader("📊 Financial Dashboard")
            
            # Display summary statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Expenses", f"${data['Amount'].sum():.2f}")
            with col2:
                st.metric("Average Expense", f"${data['Amount'].mean():.2f}")
            with col3:
                st.metric("Transaction Count", len(data))
            
            # Display data table
            st.subheader("📋 Data Table")
            st.dataframe(data, use_container_width=True)
            
            return True
        except Exception as e:
            st.error(f"❌ Error creating dashboard: {str(e)}")
            return False

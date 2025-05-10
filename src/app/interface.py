import streamlit as st


def course_information_form():
    """Creates a Streamlit form for collecting course information."""
    with st.form(key="keyword_generator_form"):
        st.subheader("📚 Course Information")
        course_name = st.text_input(
            "Course Name/Topic",
            placeholder="e.g., Python Programming, Data Science, Machine Learning",
            help="Enter the main subject or topic of the course you want to search for",
        )

        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input(
                "Company Name",
                placeholder="e.g., Acme Corporation",
                help="Your company or organization name",
            )
        with col2:
            country_name = st.text_input(
                "Country",
                placeholder="e.g., United States, India, Germany",
                help="Target country for search results",
            )

        st.subheader("🌐 Learning Platforms")
        websites_list = st.multiselect(
            "Select Learning Platforms",
            options=[
                "Udemy",
                "Coursera",
                "edX",
                "Pluralsight",
                "LinkedIn Learning",
                "Skillshare",
                "Codecademy",
                "DataCamp",
                "Udacity",
                "FutureLearn",
                "Khan Academy",
                "Other",
            ],
            default=["Udemy", "Coursera", "edX"],
            help="Select the platforms you want to include in your search",
        )

        with st.expander("⚙️ Advanced Settings", expanded=False):
            language = st.selectbox(
                "Search Language",
                options=[
                    "English",
                    "Spanish",
                    "French",
                    "German",
                    "Chinese",
                    "Japanese",
                    "Arabic",
                    "Russian",
                    "Portuguese",
                    "Hindi",
                ],
                help="Select the language for your search queries",
            )

            col1, col2 = st.columns(2)
            with col1:
                no_keywords = st.slider(
                    "Number of Search Queries to Generate",
                    min_value=5,
                    max_value=50,
                    value=10,
                    help="How many different search queries should be generated",
                )
            with col2:
                top_recommendations_no = st.slider(
                    "Number of Top Recommendations",
                    min_value=3,
                    max_value=20,
                    value=5,
                    help="How many top recommendations to display in results",
                )

            score_th = st.slider(
                "Confidence Score Threshold (%)",
                min_value=50,
                max_value=100,
                value=70,
                help="Minimum confidence score for including a recommendation",
            )

        submit_button = st.form_submit_button(
            "🚀 Generate Keywords", use_container_width=True, type="primary"
        )

    return submit_button, {
        "course_name": course_name,
        "websites_list": websites_list,
        "country_name": country_name,
        "language": language,
        "no_keywords": no_keywords,
        "score_th": score_th,
        "top_recommendations_no": top_recommendations_no,
        "company_name": company_name,
    }

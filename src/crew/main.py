from src.app.interface import course_information_form
from src.constants.constant import INPUTS
from crewai import Crew, Process
from src.schemas.schema import *
from src.crew.define import *
import streamlit as st


def run_crew(inputs):
    NN_CREW = Crew(
        agents=[
            search_query_agent,
            search_engine_agent,
            scraping_agent,
            reporter_agent,
        ],
        tasks=[
            search_queries_task,
            search_engine_task,
            scraping_task,
            reporter_task,
        ],
        process=Process.sequential,
    )

    results_placeholder = st.empty()

    for task in NN_CREW.tasks:
        if task.agent == reporter_agent:
            task.output = lambda output, task: results_placeholder.markdown(output)
            break

    NN_CREW.kickoff(inputs=inputs)

    st.success("Recommendation generation complete!")


def main():
    """Main function to run the Streamlit app and CrewAI."""

    submit_button, inputs = course_information_form()

    if submit_button:
        if not all(
            inputs[key] for key in ["course_name", "country_name", "company_name"]
        ):
            st.error(
                "Please fill in all required fields: Course Name, Country, and Company Name."
            )
        else:
            with st.spinner("Generating recommendations..."):
                run_crew(inputs)


if __name__ == "__main__":
    main()

import streamlit as st

def activities_and_books_page():
    st.title(":art: :violet[Fun Activities and Book Recommendations for ASD]")

    st.write("---")

    # Section 1: Fun Activities
    st.header(":violet[Fun Activities for Autism]")

    st.write("Engaging in fun and sensory-friendly activities can be beneficial for individuals with Autism. Here are some ideas:")

    activities_list = [
        "1. Sensory-friendly art and craft projects",
        "2. Nature walks and exploration",
        "3. Music therapy and dance",
        "4. Sensory bins with different textures",
        "5. Yoga and mindfulness exercises",
        "6. Movie or cartoon time with sensory-friendly settings",
        "7. Interactive games and puzzles",
        "8. Building activities with blocks or legos",
        "9. Water play and watercolor painting",
        "10. Visiting a sensory-friendly space or playground"
    ]

    for activity in activities_list:
        st.write("- " + activity)

    st.write("---")

    # Section 2: Book Recommendations
    st.header(":violet[Book Recommendations]")

    st.write("Reading can be a wonderful and calming activity. Here are some recommended books for individuals with Autism:")

    books_list = [
        "1. 'The Reason I Jump' by Naoki Higashida",
        "2. 'NeuroTribes: The Legacy of Autism and the Future of Neurodiversity' by Steve Silberman",
        "3. 'Thinking in Pictures' by Temple Grandin",
        "4. 'The Curious Incident of the Dog in the Night-Time' by Mark Haddon",
        "5. 'Uniquely Human: A Different Way of Seeing Autism' by Barry M. Prizant",
        "6. 'An Early Start for Your Child with Autism' by Sally J. Rogers, Geraldine Dawson, and Laurie A. Vismara",
        "7. 'Carly's Voice: Breaking Through Autism' by Arthur Fleischmann",
        "8. 'The Out-of-Sync Child' by Carol Stock Kranowitz",
        "9. 'Different...Not Less: Inspiring Stories of Achievement and Successful Employment from Adults with Autism' by Temple Grandin",
        "10. 'The Autism Acceptance Book: Being a Friend to Someone with Autism' by Ellen Sabin"
    ]

    for book in books_list:
        st.write("- " + book)

if __name__ == "__main__":
    activities_and_books_page()

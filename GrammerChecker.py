import streamlit as st
from spellchecker import SpellChecker

def main():
    # Set the app title and description
    st.set_page_config(page_title="Spell Checker", page_icon=":pencil2:")
    st.title("Spell Checker")
    st.write("Enter some text below to check for spelling mistakes.")

    # Create a SpellChecker object
    spell = SpellChecker()

    # Get the user input
    text = st.text_area("Enter your text here:", height=150)

    # Add a button to check spelling
    if st.button("Check Spelling"):
        # Split the text into words and get the misspelled words
        words = text.split()
        misspelled = spell.unknown(words)

        # Show the misspelled words and their suggested corrections
        if len(misspelled) > 0:
            st.write("Misspelled words:")
            for word in misspelled:
                suggested = spell.correction(word)
                context = " ".join([w if w in spell.known([word]) else f"**{w}**" for w in words])
                st.write(f"- {word} -> {suggested} (context: {context})")
        else:
            st.write("No spelling mistakes found.")

if __name__ == "__main__":
    main()

import streamlit as st

## Uses of markdown 

## Heading
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")
st.markdown("#### Heading 4")


## Bold Text
st.markdown("**bold text**")
## Italic
st.markdown("*Italic*")


st.markdown("> blockquote")

## Item List
st.markdown("1. First Item\n2. Second Item\n3. Third Item\n")

## code
st.markdown("`print()`")

## Horizontal
st.markdown("---")

## Link
st.markdown("[google](https://www.google.com)")

## Table
st.markdown(
"""
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |
"""
)


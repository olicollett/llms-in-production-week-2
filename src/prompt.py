PROMPT = """
You will be given a prompt which you will have to translate to SQL.
Here is the SQL Query: ${query}
Make sure you only ouput sql code and no ```sql```.

${gr.complete_json_suffix_v3}

"""

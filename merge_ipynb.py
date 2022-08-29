import nbformat

# Reading the notebooks
first_notebook = nbformat.read('ch1.ipynb', 4)
second_notebook = nbformat.read('ch2.ipynb', 4)
third_notebook = nbformat.read('ch3.ipynb', 4)
fourth_notebook = nbformat.read('ch4.ipynb', 4)

# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=first_notebook.metadata)

# Concatenating the notebooks
final_notebook.cells = first_notebook.cells + second_notebook.cells + third_notebook.cells + fourth_notebook.cells

# Saving the new notebook
nbformat.write(final_notebook, 'final_notebook.ipynb')

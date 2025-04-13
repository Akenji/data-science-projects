import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# so this loads the iris dataset from the seaborn library
iris = sns.load_dataset('iris')

#this print statement is just to uhm, understand the iris structure
print(iris.head())

# Create a color palette for different species. Works if you want random colors to be assigned.
#palette = sns.color_palette("husl", n_colors=3)  # Use 'husl' for distinct colors

# Specify the colors for each species by yourself
species_colors = {
    'setosa': '#330066',       
    'versicolor': '#490648',  
    'virginica': '#0000FF'  
}

# Calculate the average sepal length by species, to be used for pie chart visualization
avg_sepal_length = iris.groupby('species')['sepal_length'].mean()

# Bar chart visualization of average sepal length by species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='sepal_length', data=iris, estimator=lambda x: sum(x)/len(x), palette=species_colors)
plt.title('Average Sepal Length by Species')

# pie chart visualization
plt.figure(figsize=(8, 8))
plt.pie(avg_sepal_length, labels=avg_sepal_length.index, colors=[species_colors[species] for species in avg_sepal_length.index], autopct='%1.1f%%')
plt.title('Average Sepal Length Distribution by Species')

plt.show()

# OkCupid Profiles Analysis

This repository contains Python code to perform an analysis on the OkCupid Profiles dataset using the Pandas, Matplotlib, and Seaborn libraries. The analysis focuses on various aspects of user profiles, including age, height, wealth, diet preferences, and more.

## Getting Started

1. Clone the repository to your local machine.
2. Make sure you have Python and the required libraries (Pandas, Matplotlib, Seaborn) installed.

## Usage

1. Place the `okcupid_profiles.csv` dataset file in the same directory as the code.
2. Run the code using a Python interpreter (e.g., `python analyze_profiles.py`).

## Analysis Steps

### Data Cleaning

- Identify and handle missing data by removing entries with missing values.

### Analysis

#### 1. Average Age and Age Distribution

- Calculate the average age of users.
- Visualize the distribution of age using a histogram.

#### 2. Average Height and Height Distribution

- Calculate the average height of users.
- Visualize the distribution of height using a histogram.

#### 3. Relationship between Wealth and Height

- Define "wealthy" users as those with income above a threshold.
- Calculate the average height of wealthy users.
- Visualize the relationship between wealth (income) and height using a scatter plot.

#### 4. Relationship between Age and Height

- Calculate statistics for shorter and taller users separately.
- Visualize the relationship between age and height using a box plot.

#### 5. Percentage of Vegetarian and Vegan Users

- Calculate the percentage of vegetarian and vegan users.
- Visualize the percentage of diet preferences using a pie chart.

...

## Conclusion

The analysis of the OkCupid Profiles dataset revealed insights about user demographics, preferences, and relationships between different attributes. The findings can be valuable for understanding user behavior and making informed decisions based on user profiles.

## Results

- Cleaned dataset: `okcupid_profiles_cleaned.csv`
- Visualizations: Saved as image files (e.g., `age_distribution.png`, `height_distribution.png`)

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or pull request.

## License

This project is licensed under the [MIT License](LICENSE).

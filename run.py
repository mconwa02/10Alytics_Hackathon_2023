from components.data_files.data_config import EXCEL_FILE_NAMES
from components.data_files.raw_data import reading_csv
from components.preprocessing import format_columns

african_country_gdp_df = reading_csv(EXCEL_FILE_NAMES[0])
country_code_df = reading_csv(EXCEL_FILE_NAMES[1])
population_dist_df = reading_csv(EXCEL_FILE_NAMES[2])
life_expectancy_df = reading_csv(EXCEL_FILE_NAMES[3])


african_country_gdp_df = african_country_gdp_df.pipe(format_columns)
country_code_df = country_code_df.pipe(format_columns)
population_dist_df = population_dist_df.pipe(format_columns)
life_expectancy_df = life_expectancy_df.pipe(format_columns)

df = country_code_df.merge(
    african_country_gdp_df, left_on="country_code", right_on="african_country_code"
)

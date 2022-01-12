import pandas as pd
from bokeh.io import output_file, output_notebook,curdoc

vaccine_country = pd.read_csv('country_vaccinations.csv')

vaccine_country.head()

vaccine_country.iso_code.unique()

# Indonesia ==> IDN
# Malaysia  ==> MYS
# Thailand  ==> THA
# Singapura ==> SGP
# Filipina  ==> PHL
# Brunei D  ==> BRN
# Vietnam   ==> VNM
# Laos      ==> LAO
# Myanmar   ==> MMR
# Kamboja   ==> KHM

condition = (vaccine_country['iso_code'] == 'IDN') | (vaccine_country['iso_code'] == 'MYS') | (vaccine_country['iso_code'] == 'THA') | (vaccine_country['iso_code'] == 'SGP') | (vaccine_country['iso_code'] == 'PHL') | (vaccine_country['iso_code'] == 'BRN') | (vaccine_country['iso_code'] == 'VNM') | (vaccine_country['iso_code'] == 'LAO') | (vaccine_country['iso_code'] == 'MMR') | (vaccine_country['iso_code'] == 'KHM')
asean = vaccine_country[condition]
asean = asean.loc[:, ['date', 'iso_code', 'daily_vaccinations']]
asean = asean.sort_values(['iso_code','date'])
asean['date'] = pd.to_datetime(asean['date'], format='%Y-%m-%d')
asean.head()

asean.shape

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output to file
output_notebook()

# Create a ColumnDataSource
asean_cds = ColumnDataSource(asean)

# Create views for each team
IDN_view = CDSView(source=asean_cds,
                       filters=[GroupFilter(column_name='iso_code', group='IDN')])
MYS_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='MYS')])
THA_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='THA')])
SGP_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='SGP')])
PHL_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='PHL')])
BRN_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='BRN')])
VNM_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='VNM')])
LAO_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='LAO')])
MMR_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='MMR')])
KHM_view = CDSView(source=asean_cds,
                        filters=[GroupFilter(column_name='iso_code', group='KHM')])

# Create and configure the figure
asean_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Daily Vaccinations in South East Asia Nations',
                  x_axis_label='date', y_axis_label='daily_vaccinations')

# Render the race as step lines
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=IDN_view,
              color='#e6194b', legend_label='Indonesia', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=MYS_view,
              color='#3cb44b', legend_label='Malaysia', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=THA_view,
              color='#ffe119', legend_label='Thailand', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=SGP_view,
              color='#4363d8', legend_label='Singapura', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=PHL_view,
              color='#f58231', legend_label='Filipina', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=BRN_view,
              color='#911eb4', legend_label='Brunei D.', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=VNM_view,
              color='#46f0f0', legend_label='Vietnam', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=LAO_view,
              color='#f032e6', legend_label='Laos', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=MMR_view,
              color='#bcf60c', legend_label='Myanmar', muted_alpha=0.1)
asean_fig.step('date', 'daily_vaccinations',
              source=asean_cds, view=KHM_view,
              color='#fabebe', legend_label='Kamboja', muted_alpha=0.1)

# Move the legend to the right outside the plot
asean_fig.add_layout(asean_fig.legend[0], 'right')
asean_fig.legend.click_policy = 'mute'

# Show the plot
curdoc().add_root(asean_fig)




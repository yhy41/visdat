
# import libraries
import pandas as pd

from bokeh.plotting import figure, show

from bokeh.io import output_notebook
from bokeh.io import output_file
from bokeh.io import curdoc
from bokeh.io import show,curdoc

from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import Slider, Select
from bokeh.models import Column
from bokeh.models.widgets import Tabs, Panel

from bokeh.layouts import widgetbox, row, gridplot


# membaca dataset file csv
vaccine_country = pd.read_csv('country_vaccinations.csv')

# menampilkan lima data pertama dataset
vaccine_country.head()

# menampilkan kode iso dari tiap negara
vaccine_country.iso_code.unique()

# filter untuk mendapatkan negara-negara ASEAN
asean_condition = (vaccine_country['iso_code'] == 'IDN') | (vaccine_country['iso_code'] == 'MYS') | (vaccine_country['iso_code'] == 'THA') | (vaccine_country['iso_code'] == 'SGP') | (vaccine_country['iso_code'] == 'PHL') | (vaccine_country['iso_code'] == 'BRN') | (vaccine_country['iso_code'] == 'VNM') | (vaccine_country['iso_code'] == 'LAO') | (vaccine_country['iso_code'] == 'MMR') | (vaccine_country['iso_code'] == 'KHM')

# mengambil dari dataset berdasarkan filter negara ASEAN
asean = vaccine_country[asean_condition]

# menyeleksi kolom yang akan digunakan
asean = asean.loc[:, ['date', 'iso_code', 'daily_vaccinations']]

# mengurutkan berdasarkan kode iso dan tanggal
asean = asean.sort_values(['iso_code','date'])

# mengubah kolom tanggal menjadi tipe data datetime
asean['date'] = pd.to_datetime(asean['date'], format='%Y-%m-%d')

asean.head()

# membuat ColumnDataSource untuk data negara ASEAN
asean_cds = ColumnDataSource(asean)

# membuat CDSView untuk tiap negara
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

# membuat dan mengonfigurasi figure yang akan digunakan
asean_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Daily Vaccinations in South East Asia Nations',
                  x_axis_label='date', y_axis_label='daily_vaccinations')

# memasukkan CDSView tiap negara ke dalam figure
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

# memindahkan legend ke sebelah kanan dari luar plot
asean_fig.add_layout(asean_fig.legend[0], 'right')

# fitur interaksi mute plot pada legend
asean_fig.legend.click_policy = 'mute'

# menampilkan hasil figure
curdoc().add_root(asean_fig)

# filter untuk mendapatkan negara Indonesia berdasarkan kode iso
IDN_condition = (vaccine_country['iso_code'] == 'IDN')

# mengambil dari dataset berdasarkan filter negara Indonesia
idn_data = vaccine_country[IDN_condition]

# menyeleksi kolom yang akan digunakan
idn_data = idn_data.loc[:, ['date', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations']]

# mengurutkan berdasarkan kolom tanggal
idn_data = idn_data.sort_values(['date'])

# mengubah kolom tanggal menjadi tipe data datetime
idn_data['date'] = pd.to_datetime(idn_data['date'], format='%Y-%m-%d')

# me-set kolom tanggal menjadi index
idn_data.set_index('date', inplace=True)

# membuat kolom baru untuk menyimpan tanggal (sama seperti index)
idn_data['date_str'] = idn_data.index

# mengubah tipe data kolom tanggal baru menjadi string
idn_data['date_str'] = idn_data['date_str'].astype(str)

# mengambil seratus data terakhir
idn_data = idn_data.tail(100)

idn_data.head()

# membuat inisiasi HoverTool yang akan digunakan
tooltips = [
            ('Total Vaccination', '@total'),
            ('Daily Vaccination', '@daily'),
            ('People Vaccinated', '@people'),
            ('People Fully Vaccinated', '@fully'),
            ('Date', '@date')
           ]

# membuat ColumnDataSource untuk data negara Indonesia
source = ColumnDataSource(data={
    'x'     : idn_data.total_vaccinations,
    'y'     : idn_data.people_vaccinated,
    'total' : idn_data.total_vaccinations,
    'daily' : idn_data.daily_vaccinations,
    'people': idn_data.people_vaccinated,
    'fully' : idn_data.people_fully_vaccinated,
    'date'  : idn_data.date_str
})

# membuat dan mengonfigurasi figure yang akan digunakan
IDN_plot = figure(title='Data Vaccinations in Indonesia', x_axis_label='total_vaccinations', y_axis_label='people_vaccinated',
           plot_height=400, plot_width=700, tools=[HoverTool(tooltips=tooltips)])

# mem-plot berdasarkan ColumnDataSource dengan bentuk lingkaran
IDN_plot.circle(x='x', y='y', source=source, fill_alpha=0.8)

# fungsi untuk meng-update plot setelah interaksi
def update_plot(attr, old, new):
    # mengubah nilai x berdasarkan x_select
    x = x_select.value

    # mengubah nilai y berdasarkan y_select
    y = y_select.value

    # mengubah label x dan y
    IDN_plot.xaxis.axis_label = x
    IDN_plot.yaxis.axis_label = y
    
  # inisiasii data baru
    new_data = {
    'x'       : idn_data[x],
    'y'       : idn_data[y],
    'total'   : idn_data.total_vaccinations,
    'daily'   : idn_data.daily_vaccinations,
    'people'  : idn_data.people_vaccinated,
    'fully'   : idn_data.people_fully_vaccinated,
    'date'    : idn_data.date_str
    }

    # mengganti data dalam CDS
    source.data = new_data
    
    # menambahkan judul pada plot
    IDN_plot.title.text = 'Vaccinations in Indonesia'

# fitur interaksi dropdown menu
# membuat dropdown untuk data x
x_select = Select(
    options=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations'],
    value='total_vaccinations',
    title='x-axis data'
)
# menjalankan fungsi update_plot untuk hasil dari dropdown x
x_select.on_change('value', update_plot)

# membuat dropdown untuk data y
y_select = Select(
    options=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations'],
    value='people_vaccinated',
    title='y-axis data'
)
# menjalankan fungsi update_plot untuk hasil dari dropdown y
y_select.on_change('value', update_plot)

# membuat layout dan menambahkan pada curdoc
layout = row(Column(x_select, y_select), IDN_plot)
curdoc().add_root(layout)


# menyamakan lebar dari fugure dan layout
asean_fig.plot_width = layout.width = 800

# membuat dua panel untuk figure dan layout
asean_panel = Panel(child=asean_fig, title='ASEAN Panel')
IDN_panel = Panel(child=layout, title='Indonesia Panel')

# Assign the panels to Tabs
tabs = Tabs(tabs=[asean_panel, IDN_panel])

# Show the tabbed layout
curdoc().add_root(tabs)

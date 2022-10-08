import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
import plotly
import plotly.express as px

import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from iso_data import get_world_iso


df_2015 = pd.read_csv("data/2015.csv")
df_2016 = pd.read_csv("data/2016.csv")
df_2017 = pd.read_csv("data/2017.csv")
df_2018 = pd.read_csv("data/2018.csv")
df_2019 = pd.read_csv("data/2019.csv")
df_2020 = pd.read_csv("data/2020.csv")
df_2021 = pd.read_csv("data/2021.csv")


regions_df = df_2015[['Country','Region']]

adding_index1 = range(1,len(df_2020)+1)
df_2020.sort_values('Ladder score')
df_2020['Happiness_Rank'] = adding_index1
df_2020.head()

adding_index2 = range(1,len(df_2021)+1)
df_2021.sort_values('Ladder score')
df_2021['Happiness_Rank'] = adding_index2
df_2021.head()

data_2015 = df_2015[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']]
data_2016 = df_2016[['Country','Happiness Rank','Happiness Score','Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']]
data_2017 = df_2017[['Country','Happiness.Rank','Happiness.Score','Economy..GDP.per.Capita.','Family', 'Health..Life.Expectancy.', 'Freedom', 'Trust..Government.Corruption.','Generosity']]
data_2018 = df_2018[['Country or region','Overall rank','Score','GDP per capita','Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption','Generosity']]
data_2019 = df_2019[['Country or region','Overall rank','Score','GDP per capita','Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption','Generosity']]
data_2020 = df_2020[['Country name','Happiness_Rank','Ladder score','Explained by: Log GDP per capita','Explained by: Social support', 'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Perceptions of corruption','Explained by: Generosity']]
data_2021 = df_2021[['Country name','Happiness_Rank','Ladder score','Explained by: Log GDP per capita','Explained by: Social support', 'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Perceptions of corruption','Explained by: Generosity']]

data_2015 = data_2015.rename(columns = {'Economy (GDP per Capita)': 'GDP_per_Capita','Family': 'Social_support','Health (Life Expectancy)':'Life_Expectancy','Trust (Government Corruption)': 'Trust_in_Government','Happiness Rank':'Happiness_Rank','Happiness Score':'Happiness_Score'})
data_2015[['year']]= '2015'
data_2015.head()

data_2016 = data_2016.rename(columns = {'Economy (GDP per Capita)': 'GDP_per_Capita','Family': 'Social_support','Health (Life Expectancy)':'Life_Expectancy','Trust (Government Corruption)': 'Trust_in_Government','Happiness Rank':'Happiness_Rank','Happiness Score':'Happiness_Score'})
data_2016[['year']]= '2016'
data_2016.head()

data_2016 = data_2016.rename(columns = {'Economy (GDP per Capita)': 'GDP_per_Capita','Family': 'Social_support','Health (Life Expectancy)':'Life_Expectancy','Trust (Government Corruption)': 'Trust_in_Government','Happiness Rank':'Happiness_Rank','Happiness Score':'Happiness_Score'})
data_2016[['year']]= '2016'
data_2016.head()

data_2017 = data_2017.rename(columns = {'Economy..GDP.per.Capita.': 'GDP_per_Capita','Family': 'Social_support','Health..Life.Expectancy.':'Life_Expectancy','Trust..Government.Corruption.': 'Trust_in_Government','Happiness.Rank':'Happiness_Rank','Happiness.Score':'Happiness_Score'})
data_2017[['year']]= '2017'
data_2017.head()

data_2018 = data_2018.rename(columns = {'Country or region':'Country', 'GDP per capita': 'GDP_per_Capita','Social support': 'Social_support', 'Healthy life expectancy':'Life_Expectancy', 'Freedom to make life choices':'Freedom', 'Perceptions of corruption': 'Trust_in_Government','Overall rank':'Happiness_Rank','Score':'Happiness_Score'})
data_2018[['year']]= '2018'
data_2018.head()

data_2019 = data_2019.rename(columns = {'Country or region':'Country', 'GDP per capita': 'GDP_per_Capita','Social support': 'Social_support', 'Healthy life expectancy':'Life_Expectancy', 'Freedom to make life choices':'Freedom', 'Perceptions of corruption': 'Trust_in_Government','Overall rank':'Happiness_Rank','Score':'Happiness_Score'})
data_2019[['year']]= '2019'
data_2019.head()

data_2020 = data_2020.rename(columns = {'Country name':'Country', 'Explained by: Log GDP per capita': 'GDP_per_Capita','Explained by: Social support': 'Social_support','Explained by: Healthy life expectancy':'Life_Expectancy', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Perceptions of corruption': 'Trust_in_Government', 'Ladder score':'Happiness_Score', 'Explained by: Generosity':'Generosity'})
data_2020[['year']]= '2020'
data_2020.head()

data_2021 = data_2021.rename(columns = {'Country name':'Country', 'Explained by: Log GDP per capita': 'GDP_per_Capita','Explained by: Social support': 'Social_support','Explained by: Healthy life expectancy':'Life_Expectancy', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Perceptions of corruption': 'Trust_in_Government', 'Ladder score':'Happiness_Score', 'Explained by: Generosity':'Generosity'})
data_2021[['year']]= '2021'
data_2021.head()


## Let us filter out the countries for which we have data available for all 5 years
tmp = pd.merge(data_2015[['Country','year']], data_2016[['Country','year']], on='Country', how='inner', suffixes=('_2015', '_2016'))
tmp = pd.merge(tmp, data_2017[['Country','year']], on='Country', how='inner', suffixes=('', '_2017'))
tmp = pd.merge(tmp, data_2018[['Country','year']], on='Country', how='inner', suffixes=('', '_2018'))
tmp = pd.merge(tmp, data_2019[['Country','year']], on='Country', how='inner', suffixes=('', '_2019'))
tmp = pd.merge(tmp, data_2020[['Country','year']], on='Country', how='inner', suffixes=('', '_2020'))
tmp = pd.merge(tmp, data_2021[['Country','year']], on='Country', how='inner', suffixes=('', '_2021'))
country_list = tmp.Country.unique().tolist()


#concatenate all datasets
happiness_index_df = data_2015.append(data_2016)
happiness_index_df = happiness_index_df.append(data_2017)
happiness_index_df = happiness_index_df.append(data_2018)
happiness_index_df = happiness_index_df.append(data_2019)
happiness_index_df = happiness_index_df.append(data_2020)
happiness_index_df = happiness_index_df.append(data_2021)
#happiness_index_df.head()

happiness_index_df = happiness_index_df.merge(regions_df,left_on='Country',right_on='Country')
happiness_index_df = happiness_index_df[happiness_index_df.Country.isin(country_list)==True]
#happiness_index_df.info()

happiness_index_df['Trust_in_Government'] = happiness_index_df['Trust_in_Government'].fillna(happiness_index_df['Trust_in_Government'].mean())

## Calculate mean feature scores by country across the 7 years

mean_index_df = happiness_index_df.groupby(['Country'])[['Happiness_Score', 'GDP_per_Capita','Social_support','Life_Expectancy','Freedom','Trust_in_Government','Generosity']].mean().reset_index()

iso_dict = get_world_iso()
iso_df = pd.DataFrame.from_dict(iso_dict,  orient='index', columns=['iso']).reset_index()
iso_df.columns= ['Country', 'iso']

happiness_index_df = happiness_index_df.merge(iso_df, how='inner', on='Country')

df = mean_index_df.merge(iso_df, how='inner', on='Country')

country_region = happiness_index_df[['Country', 'Region']]. drop_duplicates()
df = df.merge(country_region , how='left', on='Country')
df.groupby(['Region']).mean().reset_index().sort_values('Happiness_Score', ascending=False).iloc[0,0]

app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB])

#app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])
#rgb_text = "rgb(153, 0, 0)"
#rgb_text = "rgb(51, 102, 153)"
rgb_text = 'Black'
rgb_color = 'Black'
temp='presentation'
#temp = 'plotly_white'
#light_grey= 'rgb(242, 242, 242)'
#darker_grey = 'rgb(230, 230, 230)'

#light_grey = 'rgb(255, 255, 204)' #yellow
#darker_grey = 'rgb(255, 255, 179)'

light_grey = 'rgb(230, 242, 255)' #blue
darker_grey= 'rgb(204, 229, 255)'

#temp='plotly'
happiest_country = df.sort_values('Happiness_Score', ascending=False).iloc[0,0]
happiest_region = df.groupby(['Region']).mean().reset_index().sort_values('Happiness_Score', ascending=False).iloc[0,0]

life_fig = px.scatter(df, y='Life_Expectancy', x='Happiness_Score', color='Region', size='Happiness_Score', hover_name='Country',template= temp)
support_fig = px.scatter(df, x='Social_support', y='Happiness_Score', color='Region', size='Happiness_Score', hover_name='Country', template = temp)


years_filter = ['ALL', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
app.layout = html.Div([
    html.Div(
        [
            html.H2("Happiness Level Across The World", className="display-3"
                    , style={'textAlign':'center', 'fontcolor':rgb_text, 'background-color':light_grey}),
        ],
        className="h-70 p-5 text-dark rounded-3",style={'fontcolor':rgb_text, 'background-color':light_grey}
    ),
    html.Div([
            dbc.Row([
                
                dbc.Row([
                    #html.Hr(className="my-2"),
                    dbc.Col([
                            html.Div([
                                
                                        html.Div([
                                                    html.H2(""" Select year to filter by """,
                                                            style={"fontcolor":rgb_text, 'fontsize':60, 'margin-left':'50px'
                                                                   , 'margin-top':'30px', 'margin-right':'20px' })
                                                ]),
                            dcc.Dropdown(years_filter, 'ALL', id='years_filter',
                                         style={'width':'150px','textAlign':'left', 
                                                'verticalAlign':"center", 'font-size':20, 
                                                'margin-top':'15px', 'margin-bottom':'15px'}),
                                      
                            ],style=dict(display='flex'))
                
                        ],md=4, align='center'),
                    
                    dbc.Col(
                                html.Div(
                                    [
                                        #html.H6(f"Happiest country on average {happiest_country}", id='happy_country', className="display-6", style={'fontsize':5}),
                                        html.H2([dbc.Badge("New", className="ms-1")], id='happy_country'
                                                ,style={'color':rgb_text,'background-color':darker_grey})
                                    ],
                                    className="h-100 p-10 text-dark bg-white rounded-6",
                                ),
                                md=3, align='center'
                            ),
                    dbc.Col(
                                html.Div(
                                    [
                                        html.H2([dbc.Badge("New", className="ms-1")], id='happy_cont'
                                                 ,style={'color':rgb_text,'background-color':darker_grey})
                                    ],
                                    className="h-100 p-10 text-dark bg-white rounded-6",
                                ),
                                md=5, align='center'
                            )
                        
                ], style={'background-color':darker_grey}),
                #html.Hr(className="my-2"),
                    dbc.Col( [
                        dbc.Row([
                            html.Div([dcc.Graph(id='map_fig')])
                                ],className="g-0"),
                        #html.Hr(className="my-2"),
                        dbc.Row([
                            dbc.Col(html.Div( dcc.Graph(id='life_year')),className="g-0",md=5, width={"offset": 1}),
                            dbc.Col(html.Div(dcc.Graph(id='family_year')),className="g-0",md=5)
                                ])
                             ],className="g-0",md=6, width=True),
                    dbc.Col([
                        html.Br(),
                        html.Br(),
                        dbc.Row([html.Div(dcc.Graph(figure=support_fig, id='support_graph'))],className="g-0",align="start"),
                        #html.Hr(className="my-2"),
                        dbc.Row([html.Div(dcc.Graph(figure=life_fig, id='life_graph'))],className="g-0",align="start")
                            ],className="g-0",md=6, width=True)
                    ],className="g-0"),
                ]),
                    
                    
        
])
support_fig.update_layout(font={"size":14, "color":rgb_color},margin=dict(t=30, r=40))
life_fig.update_layout(font={"size":14, "color":rgb_color},margin=dict(t=0, r=40))

@app.callback(
    Output('map_fig', 'figure'),
    Output("happy_country", "children"),
    Output("happy_cont", "children"),
    Output('support_graph','figure'),
    Output('life_graph','figure'),
    Input('years_filter', 'value')
)
def update_output(value):

    fig = px.choropleth(df, locations="iso", color="Happiness_Score", hover_name="Country")
    if value != 'ALL':
        fig_df = happiness_index_df.copy()
        fig_df = fig_df[fig_df['year'] == value]
        fig = px.choropleth(fig_df, locations="iso", color="Happiness_Score", hover_name="Country")
        happiest_country = fig_df.sort_values('Happiness_Score', ascending=False).iloc[0,0]
        happiest_region = fig_df.groupby(['Region']).mean().reset_index().sort_values('Happiness_Score', ascending=False).iloc[0,0]
        text1 = f"Happiest country in {value} is {happiest_country}"
        text2 = f"Happiest region in {value} is {happiest_region}"
        life_fig = px.scatter(fig_df, y='Life_Expectancy', x='Happiness_Score', color='Region', 
                              size='Happiness_Score', hover_name='Country',template=temp)
        support_fig = px.scatter(fig_df, x='Social_support', y='Happiness_Score', color='Region', 
                                 size='Happiness_Score', hover_name='Country',template=temp)
        
    else:
        happiest_country = df.sort_values('Happiness_Score', ascending=False).iloc[0,0]
        happiest_region = df.groupby(['Region']).mean().reset_index().sort_values('Happiness_Score', ascending=False).iloc[0,0]
        text1 = f"Happiest country overall is {happiest_country}"
        text2 = f"Happiest region overall is {happiest_region}"
        life_fig = px.scatter(df, y='Life_Expectancy', x='Happiness_Score', color='Region',
                              size='Happiness_Score', hover_name='Country',template=temp)
        support_fig = px.scatter(df, x='Social_support', y='Happiness_Score', color='Region', 
                                 size='Happiness_Score', hover_name='Country',template=temp)
        
    fig.update_layout(title="Happiness level across the world",margin=dict(t=80, b=0),title_y=0.9,
                      title_x = 0.5,font={"size":18, "color":rgb_color})
    
    
    return fig, text1, text2, life_fig, support_fig

@app.callback(
    Output('life_year', 'figure'),
    Output('family_year', 'figure'),
    Input('map_fig', 'hoverData')
)

def update_single_fig(hoverData):
    #country = 'Egypt'
    if not hoverData:
        country = 'Egypt'
    else:
        country = hoverData["points"][0]["hovertext"]
    fig_df = happiness_index_df.copy()
    fig_df = fig_df[fig_df['Country'] == country]
    fig1 = px.line(fig_df, x="year", y="Life_Expectancy", title=f"Life expectancy in {country}",template= temp)
    fig1.update_layout(title_x= 0.5, title_y=0.85, margin=dict(t=100, r=40) , title_font_color= rgb_color, font={"size":16, "color":rgb_color})
    fig2 = px.line(fig_df, x="year", y="Social_support", title=f"Family Support in {country}",template= temp)
    fig2.update_layout(title_x= 0.5, title_y=0.85, margin=dict(t=100,r=40), title_font_color= rgb_color, font={"size":16, "color":rgb_color})
    
    return fig1, fig2

if __name__=='__main__':
    app.run_server(host='0.0.0.0', debug=False, port=8050)
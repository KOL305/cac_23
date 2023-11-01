import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

def generate_line(df, x_col, y_col_s, y_col_e, title,colors=None,y_range=None):
    if (y_col_e == None):
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:], title=title,
                             color_discrete_sequence=colors)
    else:
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:y_col_e], title=title,
                            color_discrete_sequence=colors)
    plotly_fig.update_traces(line=dict(width=2.2))
    plotly_fig.update_layout(
        plot_bgcolor='rgba(36,37,45,255)',
        paper_bgcolor='rgba(36,37,45,255)',
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white",
        yaxis_title="Energy in kW",
        
        yaxis_range=y_range
    )
    plotly_fig.update_xaxes(
        ticks='inside',
        gridcolor='#39353d'
    )  
    plotly_fig.update_yaxes(
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='#39353d'
    )
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

def generate_pie(df,colors = None):
    fig=(go.Figure(
        data=go.Pie(
            labels=df['appliance'],
            title="Distribution of Consumption <br> by Appliance",
            titlefont={'size':100},
            values=df['values'],
            hole=0.5,
            
            ) 
        ))
    fig.update_traces(
            hoverinfo='label+value',
            textinfo='label+percent',
            textfont_size=12,
            marker=dict(colors=colors, 
                        line=dict(color='rgba(36,37,45,255)', width=2))
    )
    fig.update_layout(plot_bgcolor='rgba(36,37,45,255)',paper_bgcolor='rgba(36,37,45,255)',
                    font_color="white",
                    title_font_color="white",
                    legend_title_font_color="white",
                    margin=dict(t=0.2, b=0.2, l=0.2, r=0.2))
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
def generate_bar(df, x_col, y_col_s, y_col_e, title, log=False):
    fig = px.bar(df, x=df.columns[x_col], y=df.columns[y_col_s:],
             labels={'pop':'population of Canada'},barmode="overlay",log_y=log)
    fig.update_layout(
        plot_bgcolor='rgba(36,37,45,255)',
        paper_bgcolor='rgba(36,37,45,255)',
        font_color="white",
        title_font_color="white",
        legend_title_font_color="white",
    )
    fig.update_xaxes(
        ticks='inside',
        gridcolor='#39353d'
    )  
    fig.update_yaxes(
        ticks='inside',
        showline=True,
        linecolor='white',
        gridcolor='#39353d'
    )
    fig.update_traces(
        marker_line_width = 0,
    )
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div
    
  
def generate_heatmap(df,colors=None):
    fig = go.Figure(data=go.Heatmap(
                z=df.to_numpy().round(2),
                x=list(df.index.values),
                y=list(df.columns.values),       
                xgap=5, ygap=5,
                zmin=-1, zmax=1,
                colorscale=colors,
                colorbar_thickness=30,
                colorbar_ticklen=3,
    ))
    fig.update_layout(
                title_text='Correlation Matrix (cont. features)',
                title_x=0.5,
                titlefont={'size': 24},
                width=550, height=550,
                xaxis_showgrid=False,
                xaxis={'side': 'bottom'},
                yaxis_showgrid=False,
                yaxis_autorange='reversed',                   
                plot_bgcolor='rgba(36,37,45,255)',
                paper_bgcolor='rgba(36,37,45,255)',
                font_color="white",
                title_font_color="white",
                legend_title_font_color="white"
    )
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

    
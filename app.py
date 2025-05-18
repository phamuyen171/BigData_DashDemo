from dash import Dash, dcc, html, Input, Output
import numpy as np 
import pandas as pd

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Demo Dash framework cho dataset phân tích thói quen học tập'),
    html.Div('Chọn các biến để vẽ biểu đồ phân tán'),
    dcc.Dropdown(
        id="dropdown",
        options=['study_hours_per_day', 'social_media_hours', 'netflix_hours', 'attendance_percentage', 'sleep_hours', 'mental_health_rating' ],
        value=['study_hours_per_day', 'social_media_hours'],
        multi=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(dims):
    data = pd.read_csv('student_habits_performance.csv')
    data["exam_quality"] = data["exam_score"].apply(lambda x: 
                                                "Outstanding" if x >= 90
                                                else "Excellent" if x >= 80 
                                                else "Good" if x >= 70 
                                                else "Average" if x >= 60
                                                else "Pass" if x >= 50 
                                                else "Fail")

    fig = px.scatter_matrix(
        data, dimensions=dims, color="exam_quality",
        height=1000)
    return fig


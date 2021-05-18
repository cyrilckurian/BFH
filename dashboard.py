#==========MODULES=========#
import plotly.graph_objs as go
import dash_html_components as html
import dash
import dash_auth
#===========================#

if __name__ == '__main__':
    try:
        fh = open('tweets.txt','r')
    except:
        print("File Doesnt Exist!")
        exit()
    tweets = []
    html_tags = []
    for line in fh:
        tweets.append(line)
    """
    for tweet in tweets:
        print(tweet)
    """
    # To set up the Dashboard
    app = dash.Dash()

    # Authentication to the Dashboard
    auth = dash_auth.BasicAuth(
        app,
        {"USERNAME-GOES-HERE" : "PASSWORD-GOES-HERE" }
    )


    # Lot to work on this segment
    app.layout = html.Div([html.Div("Welcome To The Dashboard",style= {
                                                        "color": "orange",
                                                        "text-align": "center",
                                                        "border-style" : "outset",
                                                        "background-image": "images/background.jpg"
                                                     }),
                           html.Div(" ".join(tweets),style= {
                                        "background-color": "lightblue",
                                        "text-align": "center"
                                        })
                          ])
    # Run the server
    app.run_server()

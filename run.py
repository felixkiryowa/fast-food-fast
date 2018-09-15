"""
This Module runs flask application
"""
# from instance import APP
from update_status_of_a_specific_order.instance import app


# from instance.views import GetApiUrls

# from update_status_of_a_specific_order.instance.views import GetApiUrls

from update_status_of_a_specific_order.instance.views import GetApiUrls


app.env = 'development'
app.testing = True
GetApiUrls.get_all_urls(app)

if __name__ == '__main__':
    app.run(debug=True)

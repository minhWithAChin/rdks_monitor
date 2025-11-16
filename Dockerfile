FROM python:3.12-slim

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every important content from the local file to the image
COPY . /app/


# FROM nginx:latest
# #COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./index.html /usr/share/nginx/html/index.html
# COPY ./rdks_testdaten.json /usr/share/nginx/html/rdks-testdaten.json


# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["api_test_0.py" ]
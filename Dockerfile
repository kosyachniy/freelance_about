# Pull base image
FROM python:3.9.1

# Set work directory
WORKDIR .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Settings
ARG PROTOCOL HOST PORT TG_TOKEN
RUN rm -f sets.json keys.json
RUN echo '{ \n\
    "tg": { \n\
        "server": "'$PROTOCOL'://'$HOST':'$PORT'/" \n\
    } \n\
} \n\
' >> sets.json
RUN echo '{ \n\
    "tg": { \n\
        "token": "'$TG_TOKEN'" \n\
    } \n\
} \n\
' >> keys.json

# Run
CMD python main.py

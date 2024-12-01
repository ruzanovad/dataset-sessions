FROM continuumio/miniconda3:24.7.1-0

WORKDIR /app

ADD environment.yml /tmp/environment.yml
ADD database.env database.env

RUN apt-get update && \
    apt-get install -y gcc libpq-dev unzip

SHELL ["/bin/bash", "-c"]

RUN conda env create -f /tmp/environment.yml \
    && echo "source activate mlflow_env" > ~/.bashrc
ENV PATH /opt/conda/envs/mlflow_env/bin:$PATH 

EXPOSE 5000 8888
# Expose Jupyter Notebook port


# Copy startup script into the container
COPY start_services.sh /usr/local/bin/start_services.sh
RUN chmod +x /usr/local/bin/start_services.sh

# Command to run the startup script
CMD ["/usr/local/bin/start_services.sh"]
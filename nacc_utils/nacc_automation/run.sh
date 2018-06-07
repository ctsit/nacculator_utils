Xvfb :99 -nolisten tcp -fbdir /var/run &
sed -i "s/<username>/$USERNAME/" packet_config_example.ini
sed -i "s/<password>/$PASSWORD/" packet_config_example.ini
sed -i "s/<gator_name>/$SMTP_USER/" smtp_config_example.ini  
sed -i "s/<gator_password>/$SMTP_PASSWORD/" smtp_config_example.ini
sed -i "s/<recipients>/$RECIPIENTS/" smtp_config_example.ini
python sel.py "report"

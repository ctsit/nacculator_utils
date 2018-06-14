DATE=`date +%Y-%m-%d`
RUNPATH=run_$DATE

Xvfb :99 -nolisten tcp -fbdir /var/run &
sed -i "s|<username>|$NACC_USERNAME|" packet_config_example.ini
sed -i "s|<password>|$NACC_PASSWORD|" packet_config_example.ini
sed -i "s|<email_id>|$NACC_EMAIL|" packet_config_example.ini
sed -i "s|<upload_file_path>|$NACC_UPLOAD_PATH|" packet_config_example.ini
sed -i "s|<your_redcap_token>|$REDCAP_TOKEN|" nacculator_cfg.ini.example
sed -i "s|<your_redcap_server>|$REDCAP_SERVER|" nacculator_cfg.ini.example
sed -i "s|<path/to/current-subjects.csv>|$SUBJECT_FILE_PATH|" nacculator_cfg.ini.example
sed -i "s|<path/to/current-subjects.csv>|$SUBJECT_FILE_PATH|" nacculator_cfg.ini.example

python sel.py "getdata"
python run_filters.py "nacculator_cfg.ini.example" $RUNPATH
echo "Splitting into Initial and Followup files"
bash split_ivp_fvp.sh ./runs/$RUNPATH/final_update.csv
echo "Running NACCulator on initial visits"
redcap2nacc -ivp < ./initial_visits.csv > ./runs/$RUNPATH/iv_nacc_complete.txt 2>./runs/$RUNPATH/ivp_errors.txt
echo "Running NACCulator on followup visits"
redcap2nacc -fvp < ./followup_visits.csv > ./runs/$RUNPATH/fv_nacc_complete.txt 2>./runs/$RUNPATH/fvp_errors.txt

#Super lazy to prevent having to recode some of the selenium tools:
cp ./runs/$RUNPATH/iv_nacc_complete.txt $NACC_UPLOAD_PATH
cat ./runs/$RUNPATH/fv_nacc_complete.txt >> $NACC_UPLOAD_PATH

echo "Attempting to upload file"
python sel.py upload


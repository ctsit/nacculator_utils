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
#header filters
sed -i '19i a1lang: langa1' nacculator_cfg.ini.example
sed -i '20i a2lang: langa2' nacculator_cfg.ini.example
sed -i '21i a2sub_095a3b: a2sub' nacculator_cfg.ini.example
sed -i '22i a2not_21e87d: a2not' nacculator_cfg.ini.example
sed -i '23i a3lang: langa3' nacculator_cfg.ini.example
sed -i '24i a3sub_2b0d69: a3sub' nacculator_cfg.ini.example
sed -i '25i a3not_c7cb57: a3not' nacculator_cfg.ini.example
sed -i '26i a4lang: langa4' nacculator_cfg.ini.example
sed -i '27i a4sub_2c437c: a4sub' nacculator_cfg.ini.example
sed -i '28i a4not_c4e53e: a4not' nacculator_cfg.ini.example
sed -i '29i a5lang: langa5' nacculator_cfg.ini.example
sed -i '30i b1lang: langb1' nacculator_cfg.ini.example
sed -i '31i b1sub_3c9b3b: b1sub' nacculator_cfg.ini.example
sed -i '32i b1not_8b7733: b1not' nacculator_cfg.ini.example
sed -i '33i b4lang: langb4' nacculator_cfg.ini.example
sed -i '34i b5lang: langb5' nacculator_cfg.ini.example
sed -i '35i b5sub_712f66: b5sub' nacculator_cfg.ini.example
sed -i '36i b5not_a4b779: b5not' nacculator_cfg.ini.example
sed -i '37i b6lang: langb6' nacculator_cfg.ini.example
sed -i '38i b6sub_35db4c: b6sub' nacculator_cfg.ini.example
sed -i '39i b6not_06dff0: b6not' nacculator_cfg.ini.example
sed -i '40i b7lang: langb7' nacculator_cfg.ini.example
sed -i '41i b7sub_7e2220: b7sub' nacculator_cfg.ini.example
sed -i '42i b7not_2dfac5: b7not' nacculator_cfg.ini.example
sed -i '43i b8lang: langb8' nacculator_cfg.ini.example
sed -i '44i b9lang: langb9' nacculator_cfg.ini.example
sed -i '45i c2lang: langc2' nacculator_cfg.ini.example
sed -i '46i d1lang: langd1' nacculator_cfg.ini.example
sed -i '47i d2lang: langd2' nacculator_cfg.ini.example
sed -i '48i a3alang: langa3a' nacculator_cfg.ini.example
sed -i '49i a3asubmitted: ftda3afs' nacculator_cfg.ini.example
sed -i '50i a3anot: ftda3afr' nacculator_cfg.ini.example
sed -i '51i b3flang: langb3f' nacculator_cfg.ini.example
sed -i '52i b9flang: langb9f' nacculator_cfg.ini.example
sed -i '53i c1flang: langc1f' nacculator_cfg.ini.example
sed -i '54i c2flang: langc2f' nacculator_cfg.ini.example
sed -i '55i c3flang: langc3f' nacculator_cfg.ini.example
sed -i '56i c4flang: langc4f' nacculator_cfg.ini.example
sed -i '57i c4fsubmitted: ftdc4fs' nacculator_cfg.ini.example
sed -i '58i c4fnot: ftdc4fr' nacculator_cfg.ini.example
sed -i '59i c5fsubmitted: ftdc5fs' nacculator_cfg.ini.example
sed -i '60i c5fnot: ftdc5fr' nacculator_cfg.ini.example
sed -i '61i c6fsubmitted: ftdc6fs' nacculator_cfg.ini.example
sed -i '62i c6fnot: ftdc6fr' nacculator_cfg.ini.example
sed -i '63i e2flang: lange2f' nacculator_cfg.ini.example
sed -i '64i e3flang: lange3f' nacculator_cfg.ini.example
sed -i '65i clslang: langcls' nacculator_cfg.ini.example
sed -i '66i clssubmitted: clssub' nacculator_cfg.ini.example
sed -i '67i fu_a1lang: fu_langa1' nacculator_cfg.ini.example
sed -i '68i fu_a2lang: fu_langa2' nacculator_cfg.ini.example
sed -i '69i fu_a2sub_73fdc7: fu_a2sub' nacculator_cfg.ini.example
sed -i '70i fu_a2not_fd65a7: fu_a2not' nacculator_cfg.ini.example
sed -i '71i fu_a3lang: fu_langa3' nacculator_cfg.ini.example
sed -i '72i fu_a3sub_c2a68b: fu_a3sub' nacculator_cfg.ini.example
sed -i '73i fu_a3not_f7c411: fu_a3not' nacculator_cfg.ini.example
sed -i '74i fu_a4lang: fu_langa4' nacculator_cfg.ini.example
sed -i '75i fu_a4sub_143f22: fu_a4sub' nacculator_cfg.ini.example
sed -i '76i fu_a4not_b95e64: fu_a4not' nacculator_cfg.ini.example
sed -i '77i fu_a5lang: fu_langa5' nacculator_cfg.ini.example
sed -i '78i fu_b1lang: fu_langb1' nacculator_cfg.ini.example
sed -i '79i fu_b1sub_c03500: fu_b1sub' nacculator_cfg.ini.example
sed -i '80i fu_b1not_0a7e9f: fu_b1not' nacculator_cfg.ini.example
sed -i '81i fu_b4lang: fu_langb4' nacculator_cfg.ini.example
sed -i '82i fu_b5lang: fu_langb5' nacculator_cfg.ini.example
sed -i '83i fu_b5sub_51a694: fu_b5sub' nacculator_cfg.ini.example
sed -i '84i b5not_fvpz1x: fu_b5not' nacculator_cfg.ini.example
sed -i '85i fu_b6lang: fu_langb6' nacculator_cfg.ini.example
sed -i '86i fu_b6sub_db439d: fu_b6sub' nacculator_cfg.ini.example
sed -i '87i fu_b6not_310244: fu_b6not' nacculator_cfg.ini.example
sed -i '88i fu_b7lang: fu_langb7' nacculator_cfg.ini.example
sed -i '89i fu_b7sub_21a95f: fu_b7sub' nacculator_cfg.ini.example
sed -i '90i fu_b7not_dccb30: fu_b7not' nacculator_cfg.ini.example
sed -i '91i fu_b8lang: fu_langb8' nacculator_cfg.ini.example
sed -i '92i fu_b9lang: fu_langb9' nacculator_cfg.ini.example
sed -i '93i fu_c2lang: fu_langc2' nacculator_cfg.ini.example
sed -i '94i fu_d1lang: fu_langd1' nacculator_cfg.ini.example
sed -i '95i fu_d2lang: fu_langd2' nacculator_cfg.ini.example
sed -i '96i fu_a3alang: fu_langa3a' nacculator_cfg.ini.example
sed -i '97i fu_a3asubmitted: fu_ftda3afs' nacculator_cfg.ini.example
sed -i '98i fu_a3anot: fu_ftda3afr' nacculator_cfg.ini.example
sed -i '99i fu_b3flang: fu_langb3f' nacculator_cfg.ini.example
sed -i '100i fu_b9flang: fu_langb9f' nacculator_cfg.ini.example
sed -i '101i fu_c1flang: fu_langc1f' nacculator_cfg.ini.example
sed -i '102i fu_c2flang: fu_langc2f' nacculator_cfg.ini.example
sed -i '103i fu_c3flang: fu_langc3f' nacculator_cfg.ini.example
sed -i '104i fu_c4flang: fu_langc4f' nacculator_cfg.ini.example
sed -i '105i fu_c4fsubmitted: fu_ftdc4fs' nacculator_cfg.ini.example
sed -i '106i fu_c4fnot: fu_ftdc4fr' nacculator_cfg.ini.example
sed -i '107i fu_c5fsubmitted: fu_ftdc5fs' nacculator_cfg.ini.example
sed -i '108i fu_c5fnot: fu_ftdc5fr' nacculator_cfg.ini.example
sed -i '109i fu_c6fsubmitted: fu_ftdc6fs' nacculator_cfg.ini.example
sed -i '110i fu_c6fnot: fu_ftdc6fr' nacculator_cfg.ini.example
sed -i '111i fu_e2flang: fu_lange2f' nacculator_cfg.ini.example
sed -i '112i fu_e3flang: fu_lange3f' nacculator_cfg.ini.example
sed -i '113i fu_clslang: fu_langcls' nacculator_cfg.ini.example
sed -i '114i fu_clssubmitted: fu_clssub' nacculator_cfg.ini.example
#SMTP
sed -i "s|<smtp host>|$SMTP_HOST|" smtp_config_example.ini
sed -i "s|<smtp port>|$SMTP_PORT|" smtp_config_example.ini
sed -i "s|<from address>|$SMTP_FROM|" smtp_config_example.ini
sed -i "s|<send list>|$SMTP_TO|" smtp_config_example.ini

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

echo "Collecting files for email"
tar -czf nacc_upload_$DATE.tar.gz $NACC_UPLOAD_PATH ./*_visits.csv ./runs/$RUNPATH/*_errors.txt
python send_email.py "NACC Upload $DATE" "NACCulator has completed a run, please see attached" nacc_upload_$DATE.tar.gz

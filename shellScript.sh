echo 'l_english:'  > out.txt
echo " idea_settings.10" >> out.txt
echo " idea_settings.11" >> out.txt
printf '\xEF\xBB\xBF' | cat  - out.txt  > out1.txt
rm out.txt

echo "Top 10 processes in descending order are:" 
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head 
echo "Processes with highest memory usage are:"
ps aux | sort -nk +4 | tail -n  10           
echo "current logged in users and logname are:"              
logname                
echo "current shell is:"               
echo $SHELL                 
echo "home directory is:"
$HOME                
echo "Current path is:"               
echo $PATH                
echo  "current working directory is"           
pwd                
echo  "current OS version, release number, kernel version are:"                
uname -a


# ------------OUTPUT-----------

# Top 10 processes in descending order are:
#   PID  PPID CMD                         %MEM %CPU
#  2657  1720 /usr/lib/firefox/firefox     3.4  4.4
#  3812  3774 /usr/share/code/code --type  3.0 12.0
#  1603  1599 kded5 [kdeinit5]             2.9  0.2
#  1658     1 /usr/bin/plasmashell         2.9  3.1
#  2306  1720 /opt/google/chrome/chrome    2.5  3.6
#  1720  1599 /usr/bin/latte-dock -sessio  2.5  6.2
#  1652  1620 kwin_x11 -session 101be1431  2.1  5.4
#  2846  2657 /usr/lib/firefox/firefox -c  2.1  5.3
#  2710  2657 /usr/lib/firefox/firefox -c  1.7  0.4
# Processes with highest memory usage are:
# therexo+  2710  0.4  1.7 2605920 141252 ?      Sl   12:54   0:03 /usr/lib/firefox/firefox -contentproc -childID 1 -isForBrowser -prefsLen 1 -prefMapSize 211045 -parentBuildID 20200117190643 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 2657 true tab
# therexo+  2760  0.4  1.7 27804072 136620 ?     Sl   12:54   0:03 /usr/lib/firefox/firefox -contentproc -childID 2 -isForBrowser -prefsLen 6202 -prefMapSize 211045 -parentBuildID 20200117190643 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 2657 true tab
# therexo+  1652  5.4  2.1 3525916 174696 ?      Sl   12:50   0:49 kwin_x11 -session 101be143181166000157409372600000015570005_1578034108_987326
# therexo+  2846  5.3  2.1 2725864 171956 ?      Sl   12:54   0:36 /usr/lib/firefox/firefox -contentproc -childID 4 -isForBrowser -prefsLen 7091 -prefMapSize 211045 -parentBuildID 20200117190643 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 2657 true tab
# therexo+  1720  6.2  2.5 1470108 201900 ?      Sl   12:50   0:56 /usr/bin/latte-dock -session 101be143181166000157409372700000015570008_1578034108_969788
# therexo+  2306  3.6  2.5 911244 202116 ?       Sl   12:51   0:30 /opt/google/chrome/chrome
# therexo+  1603  0.2  2.9 1605584 237044 ?      Sl   12:50   0:02 kded5 [kdeinit5]
# therexo+  1658  3.1  2.9 3972992 232924 ?      Sl   12:50   0:28 /usr/bin/plasmashell
# therexo+  3812 12.0  3.0 1095180 247548 ?      Sl   12:57   1:01 /usr/share/code/code --type=renderer --disable-color-correct-rendering --no-sandbox --field-trial-handle=13506221397633274078,2502593822593649668,131072 --disable-features=LayoutNG,SpareRendererForSitePerProcess --lang=en-GB --standard-schemes --secure-schemes=vscode-resource --bypasscsp-schemes --cors-schemes=vscode-resource --fetch-schemes=vscode-resource --service-worker-schemes --app-path=/usr/share/code/resources/app --node-integration --webview-tag --no-sandbox --no-zygote --background-color=#1e1e1e --num-raster-threads=2 --enable-main-frame-before-activation --service-request-channel-token=8850398559723391324 --renderer-client-id=4 --no-v8-untrusted-code-mitigations --shared-files=v8_context_snapshot_data:100,v8_natives_data:101
# therexo+  2657  4.4  3.4 2944300 273740 ?      Sl   12:54   0:30 /usr/lib/firefox/firefox
# current logged in users and logname are:
# therexone
# current shell is:
# /bin/bash
# home directory is:
# ./script-f.sh: line 10: /home/therexone: Is a directory
# Current path is:
# /home/therexone/.rvm/gems/ruby-2.6.3/bin:/home/therexone/.rvm/gems/ruby-2.6.3@global/bin:/home/therexone/.rvm/rubies/ruby-2.6.3/bin:/home/therexone/.nvm/versions/node/v12.13.1/bin:/home/therexone/.local/bin:/home/therexone/.rvm/gems/ruby-2.6.3/bin:/home/therexone/.rvm/gems/ruby-2.6.3@global/bin:/home/therexone/.rvm/rubies/ruby-2.6.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/share/rvm/bin:/home/therexone/.rvm/bin:/home/therexone/.rvm/bin
# current working directory is
# /home/therexone/Desktop/workspace/sem4-uni/OSL
# current OS version, release number, kernel version are:
# Linux therexone-X556UQK 5.3.0-28-generic #30~18.04.1-Ubuntu SMP Fri Jan 17 06:14:09 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

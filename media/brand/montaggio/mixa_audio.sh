set -e
S="0 3.361 7.602 11.883 15.444 20.125 26.366 34.687"; TOT=38.338
i=0; inputs=""; filt=""; labs=""
for s in $S; do i=$((i+1)); n=$(printf "%02d" $i); ms=$(python3 -c "print(int($s*1000))")
 inputs="$inputs -i src/F$n.wav"; filt="$filt[$((i-1)):a]aresample=48000,adelay=${ms}|${ms}[v$i];"; labs="$labs[v$i]"; done
ffmpeg -y -loglevel error $inputs -filter_complex "${filt}${labs}amix=inputs=8:normalize=0,apad,atrim=0:$TOT,loudnorm=I=-16:TP=-2:LRA=11[v]" -map "[v]" -ac 2 -ar 48000 voce3.wav
VOL="if(lt(t,20.125),0.16*min(t/0.4,1),if(lt(t,26.366),0.16+0.08*(t-20.125)/6.241,if(lt(t,34.0),0.16,if(lt(t,34.6),0.16*(34.6-t)/0.6,if(lt(t,37.2),0,if(lt(t,38.0),0.25*min((t-37.2)/0.3,1),0.25*max((38.338-t)/0.338,0)))))))"
ffmpeg -y -loglevel error -i src/musica.mp3 -filter_complex "[0:a]atrim=0:$TOT,aresample=48000,loudnorm=I=-16:TP=-2,volume='$VOL':eval=frame[m]" -map "[m]" -ac 2 musica3.wav
ffmpeg -y -loglevel error -i voce3.wav -i musica3.wav -filter_complex "[0:a][1:a]amix=inputs=2:normalize=0,alimiter=limit=0.89[a]" -map "[a]" -ar 48000 mix3.wav
ffmpeg -y -loglevel error -i video_muto_v4.mp4 -i mix3.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart 2026-11_C01_auriga-inside-out_v4.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 2026-11_C01_auriga-inside-out_v4.mp4

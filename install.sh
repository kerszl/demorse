#/bin/bash
CMD="chmod +x demorse.py"
$($CMD)
echo $CMD

CMD="cp demorse.py /usr/local/bin/"
$($CMD)
echo $CMD

CMD="ln -f -s /usr/local/bin/demorse.py /usr/local/bin/demorse"
$($CMD)
echo $CMD

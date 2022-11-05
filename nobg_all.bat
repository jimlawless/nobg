@echo off
for %%x in (*.j*) do python nobg.py -infile %%x -outfile %%~nx.png

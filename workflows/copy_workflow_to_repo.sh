
#  zkopiruje workflow soubor do nadrazeneho repozitare
#  Predpoklada se, ze tento repozitar je jako submodul
#  a je umisten v `/doc/assets`
#

mkdir -p ../../../.github/workflows
cp kicad_outputs.yml ../../../.github/workflows/kicad_outputs.yml

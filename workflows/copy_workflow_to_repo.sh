
#  zkopiruje workflow soubor do nadrazeneho repozitare
#  Predpoklada se, ze tento repozitar je jako submodul
#  a je umisten v `/doc/assets`
#

mkdir -p ../../../.github/workflows

if [ "$(find ../../../hw -name '*kicad_pro'  2>/dev/null)" ]
then
	echo "KiCAD project is detected"
	cp kicad_outputs.yml ../../../.github/workflows/kicad_outputs.yml
else
   rm ../../../.github/workflows/kicad_outputs.yml 2>/dev/null || true
   echo "KiCAD project not found"
fi
cp update_actions.yml ../../../.github/workflows/update_actions.yml
cp metadata_updater.yml ../../../.github/workflows/metadata_updater.yml


#  zkopiruje workflow soubor do nadrazeneho repozitare
#  Predpoklada se, ze tento repozitar je jako submodul
#  a je umisten v `/doc/assets`
#

mkdir -p ../../../.github/workflows
if [ -n "$(find ../../../ -name *kicad_*  2>/dev/null)" ]
then
        cp kicad_outputs.yml ../../../.github/workflows/kicad_outputs.yml
else
        echo "Kicad nenalezen"
fi
cp update_actions.yml ../../../.github/workflows/update_actions.yml
cp metadata_updater.yml ../../../.github/workflows/metadata_updater.yml

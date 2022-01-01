BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

printf "${BLUE}Installing ${YELLOW}Required ${BLUE}Mod${YELLOW}ules${BLUE}... ${NC}\n"
pip install -r requirements.txt

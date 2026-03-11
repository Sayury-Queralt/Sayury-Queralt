DIR="$(cd "$(dirname "$0")" && pwd)"

while true; do
    hostname > "$DIR/hostname.txt"
    date +"%H:%M:%S" > "$DIR/hora.txt"
    sleep 1
done

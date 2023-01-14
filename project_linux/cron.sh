# verify if this package is installed 
folderPath="$(pwd)"


# array of packages to check
check_dependencies () {
	# checks if dependencies are present
	for dep; do
		if ! command -v "$dep" >/dev/null ; then
			echo "Program \"$dep\" not found. Please install it. \n Type \"scoop install $dep\" if you're using windows or type apt-get install $dep"
			if command -v "apt-get" >/dev/null ; then
                sudo apt-get install $dep
                echo "Program \"$dep\" installed"
            fi
						
		fi
	done
}


check_dependencies "python"  "crontab"

# check if crontab is running if not start it
if ! crontab -l > /dev/null 2>&1; then
    echo "Crontab is not running, starting it..."
    # export EDITOR=nvim # set nano of vim 
    crontab -e
fi
# run trailer.js script every hour

if ! crontab -l | grep -q "views.py"; then
  echo "Adding cron job to crontab... services.py"
  (crontab -l) | { cat; echo "0 1 * * * cd $folderPath/ && python3 services.py"; } | crontab -
fi


# added cron job to crontab
echo "Cron job added to crontab" 
crontab -l
# Artistic Style Transfer using a webcam

## Installation

### Required:
* [git](https://git-scm.com/downloads)
* [python](https://www.python.org/downloads/)

### Quick start
`git clone https://github.com/mrzetti/style-transfer`  
`pip install -r requirements.txt`

## Usage


`python style_transfer.py [-h] [--style STYLE] [--size SIZE]`

	options:
	-h, --help show this help message and exit

	--style STYLE Choose style: [Available styles] Default: van_gogh_starry_night

	--size SIZE Choose the size of the video. Default: 512

### Available styles

* `kanagawa_great_wave`
* `kandinsky_composition_7`
* `hubble_pillars_of_creation`
* `van_gogh_starry_night`
* `turner_nantes`
* `munch_scream`
* `picasso_demoiselles_avignon`
* `picasso_violin`
* `picasso_bottle_of_rum`
* `fire`
* `derkovits_woman_head`
* `amadeo_style_life`
* `derkovtis_talig`
* `amadeo_cardoso`

## TODO:

* fix `frame_size` - Only DEFAULT / 512 works
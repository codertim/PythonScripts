
import glob
import os

NEW_IMAGE_WIDTH    = 800
ORIGINALS_DIR_NAME = "Originals"
RESIZED_DIR_NAME   = "Resized"

print "\nStarting ...\n\n"

image_magick_result = os.system("which convert")
if image_magick_result != 0:
  print "Image magick NOT found"


image_files = glob.glob("*.jpg") + glob.glob("*.JPG")
print "Filenames: ", image_files


if not image_files:
  print "Cannot find any images"
  exit(0)


# ensure original images backup directory exists
if os.path.isdir("./" + ORIGINALS_DIR_NAME):
  print "Originals directory exists"
else:
  print "Creating originals directory"
  os.makedirs(ORIGINALS_DIR_NAME)


# create backup of original images and place in new directory just in case anything goes wrong
for image in image_files:
  new_filename = "./" + ORIGINALS_DIR_NAME + "/orig_" + image
  copy_command = "cp %s %s" % (image, new_filename)
  os.system(copy_command)


# ensure image resizing directory exists
if os.path.isdir("./" + RESIZED_DIR_NAME):
  print "Resized directory exists"
else:
  print "Creating resized directory"
  os.makedirs(RESIZED_DIR_NAME)


for image in image_files:
  new_filename = "./" + RESIZED_DIR_NAME
  image_name_parts = image.split(".")
  resized_image_name = image_name_parts[0] + "_w" + str(NEW_IMAGE_WIDTH) + "." + image_name_parts[1]
  # print "  resized image name: %s" % resized_image_name
  shrink_command = "convert %s -resize %d %s" % (image, NEW_IMAGE_WIDTH, "./" + RESIZED_DIR_NAME + "/" + resized_image_name)
  print "  Running command: " + shrink_command
  os.system(shrink_command)


print "\nDone.\n\n"





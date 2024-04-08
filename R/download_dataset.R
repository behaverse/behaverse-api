#' Download a Behaverse dataset
#' @param url URL of the dataset to download
#' @param dest The destination file to save the dataset
#' @export
download_dataset <- function(url, dest) {

  parent_dir <- dirname(dest)

  if (!dir.exists(parent_dir)) {
    dir.create(parent_dir, recursive = TRUE)
  }

  if (!file.exists(dest)) {
    download.file(url, dest)
    print(paste("Dataset downloaded to", dest))
  }

  untar(dest, exdir = parent_dir)
  print(paste("Dataset extracted to", parent_dir))
}

#' Load a Behaverse dataset
#' 
#' @param name The name of the dataset to load
#' @export 
load_dataset <- function(name) {
  paste0("Loading ", name, " dataset...")
}

#' Download a Behaverse dataset
#' 
#' @param name The name of the dataset to download
#' @param dest The destination directory to save the dataset
#' @export
download_dataset <- function(name, dest = NULL) {
  paste0("Downloading ", name, " dataset...")
}

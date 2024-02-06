library(leaflet)
library(dplyr)
library(htmlwidgets)
library(webshot)

setwd("/Users/khiroyuki/src/github.com/kromiii/sento/map")
df <- read.csv("zahyo.csv")

create_map <- function(df, i) {
  m <- leaflet(df %>% filter(section == i)) %>%
    addTiles()
  m <- m %>% addPopups(~lng, ~lat, popup = ~ as.character(name))
  return(m)
}

for (i in unique(df$section)) {
  m <- create_map(df, i)
  saveWidget(m, paste0(i, ".html"), selfcontained = FALSE)
  webshot(paste0(i, ".html"),
    file = paste0(i, ".png"),
    cliprect = "viewport"
  )
  # remove html file
  file.remove(paste0(i, ".html"))
  # remove tmp files
  unlink(paste0(i, "_files"), recursive = TRUE)
}

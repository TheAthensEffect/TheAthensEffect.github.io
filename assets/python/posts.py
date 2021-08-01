
def minipost():
  print(" ")
  print("<article class='mini-post'>")
  print(" <header>")
  print("   <h3><a href='" + link + "'>" + title + "</a></h3>")
  print("   <time class='published' datetime=" + date1 + ">" + date2 + "</time>")
  print("   <a href='#' class='author'><img src=a alt='" + auimage + "' /></a>")
  print(" </header>")
  print(" <a href='" + link + "' class='image'><img src='" + image + "' alt=''/></a>")
  print("</article>")

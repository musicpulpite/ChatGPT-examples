Sure! Here's a basic example of what the home page of a Substack blog website clone might look like:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Substack Blog Clone</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Posts</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
      <h1>Substack Blog Clone</h1>
      <p>A simple blogging platform for individuals and organizations.</p>
    </header>

    <main>
      <div class="posts-list">
        <article>
          <h2><a href="#">Post Title Here</a></h2>
          <p class="posted-on">Posted on January 1, 2021</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet, risus eget lacinia hendrerit, massa nibh tincidunt quam, vel vulputate sapien felis sit amet lacus.</p>
        </article>

        <article>
          <h2><a href="#">Another Post Title Here</a></h2>
          <p class="posted-on">Posted on February 14, 2021</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet, risus eget lacinia hendrerit, massa nibh tincidunt quam, vel vulputate sapien felis sit amet lacus.</p>
        </article>

        <article>
          <h2><a href="#">Third Post Title Here</a></h2>
          <p class="posted-on">Posted on March 23, 2021</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet, risus eget lacinia hendrerit, massa nibh tincidunt quam, vel vulputate sapien felis sit amet lacus.</p>
        </article>
      </div>

      <aside>
        <h2>About Us</h2>
        <p>Learn more about our platform and how it can work for you.</p>
        <a href="#">Read More</a>

        <h2>Featured Posts</h2>
        <ul>
          <li><a href="#">Post Title Here</a></li>
          <li><a href="#">Another Post Title Here</a></li>
          <li><a href="#">Third Post Title Here</a></li>
        </ul>

        <h2>Subscribe</h2>
        <form>
          <label for="email">Enter your email to receive new posts:</label>
          <input type="email" id="email" name="email" required>
          <button type="submit">Subscribe</button>
        </form>
      </aside>
    </main>

    <footer>
      <p>&copy;2021 Substack Blog Clone. All rights reserved.</p>
    </footer>
  </body>
</html>
```

And here is the accompanying `styles.css` stylesheet:

```
/* Global styles */

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
}

body {
  background-color: #F9F9F9;
  color: #333;
  margin: 0;
}

a {
  color: #333;
  text-decoration: none;
}

a:hover {
  color: #007AFF;
  text-decoration: underline;
}

ul {
  list-style: none;
}

/* Page header */

header {
  background-color: #007AFF;
  color: #FFF;
  padding: 1rem;
}

header nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

header nav ul {
  display: flex;
}

header nav ul li {
  margin-right: 1rem;
}

header nav ul li:last-child {
  margin-right: 0;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

header p {
  font-size: 1.2rem;
}

/* Main content */

main {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 1rem;
  margin: 1rem auto;
  max-width: 1200px;
}

.posts-list article {
  margin-bottom: 1rem;
}

.posts-list article h2 {
  font-size: 1.5rem;
}

.posts-list article .posted-on {
  font-size: 0.8rem;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.posts-list article p {
  font-size: 1.2rem;
}

aside {
  flex-basis: 30%;
  margin-left: 2rem;
}

aside h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

aside p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

aside ul li {
  margin-bottom: 0.5rem;
}

aside a {
  display: inline-block;
  background-color: #007AFF;
  color: #FFF;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  margin-top: 1rem;
}

aside form {
  margin-top: 1rem;
}

aside label {
  display: block;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

aside input[type=email] {
  display: block;
  width: 100%;
  font-size: 1.2rem;
  padding: 0.5rem;
  border-radius: 5px;
  border: 2px solid #CCC;
  margin-bottom: 0.5rem;
}

aside button[type=submit] {
  display: block;
  background-color: #006CEC;
  color: #FFF;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  cursor: pointer;
}

footer {
  background-color: #EEE;
  color: #333;
  text-align: center;
  padding: 1rem;
}
```

I hope this is helpful! Let me know if you have any questions or need further assistance.
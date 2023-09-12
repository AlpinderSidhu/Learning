// No need to import http as it comes along with Node
const http = require("http");
const port = 8001;

const server = http.Server((req, res) => {
  const url = req.url;
  // Routing Request Example
  // User will be routed to the /message upon hitting submit button
  if (url === "/") {
    res.write(`<html>
        <title>IF Block</title>
        <body>
          <form action="/message" method="POST">
            <input type="text" name="message" />
            <button type="submit">Send</button>
          </form>
        </body>
      </html>`);
    return res.end();
  }

  res.setHeader("Content-Type", "text/html");
  res.write(`
  <html>
    <title>Outside IF Block</title>
    <body>
      <h1>Hello, How are you?</h1>
    </body>
  </html>`);
  res.end();
});

server.listen(port);

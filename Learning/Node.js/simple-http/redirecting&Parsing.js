const http = require("http");
const fs = require("fs");

const server = http.Server((req, res) => {
  const url = req.url;
  const method = req.method;
  // Redirecting Request Example
  // User will be redirected to the / upon hitting submit button
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
  if (url === "/message" && method === "POST") {
    // Parsing Start
    const body = [];

    // Parsing End
    fs.writeFileSync("redirecting.txt", "Dummy message");
    res.statusCode = 302;
    res.setHeader("Location", "/");
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

server.listen(8001);

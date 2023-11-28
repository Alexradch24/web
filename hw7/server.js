const express = require('express');
const webpush = require('web-push');
const bodyParser = require('body-parser');
const path = require('path');
const redis = require('redis')

const app = express();
const cl = redis.createClient({
    host: '127.0.0.1', 
    port: 6379
  });

const { expressCspHeader, INLINE, NONE, SELF } = require('express-csp-header');
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, "client")))


app.use(expressCspHeader({ 
    policies: { 
        'default-src': [expressCspHeader.NONE], 
        'img-src': [expressCspHeader.SELF], 
    } 
})); 

const vapidKeys = webpush.generateVAPIDKeys();

cl.set('publicVAPIDKeys', vapidKeys.publicKey);
cl.set('privateVAPIDKeys', vapidKeys.privateKey);

app.get('/getPublicKey', (req, res) => {
    cl.get('publicVAPIDKeys', (err, publicVAPIDKey) => {
      if (err) {
        console.error('Ошибка при получении публичного ключа из Redis:', err);
        res.status(500).json({ error: 'Ошибка сервера' });
      } else {
        res.json({ publicKey: publicVAPIDKey });
      }
    });
  });

app.post('/subscribe', (req, res) => {
    const subscription = req.body;
    res.status(201).json({});
    const payload = JSON.stringify({ title: "Hello", body: "This is push notification" });
    webpush.sendNotification(subscription, payload).catch(console.log);
})

const PORT = 3000;

app.listen(PORT, () => {
    console.log("Сервер слушает порт " + PORT);
})
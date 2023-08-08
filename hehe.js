const fs = require('fs');
const http = require('http');
const colors = require('colors');
const path = require('path');

process.on('uncaughtException', function (er) {
    console.log(er);
});
process.on('unhandledRejection', function (er) {
    console.log(er);
});


const args = {
    fromFile: process.argv[2],
    resultFile: process.argv[3],
    timeout: parseInt(process.argv[4])
}

const scriptName = path.basename(__filename);

function log(string) {
    let d = new Date();
    let hours = (d.getHours() < 10 ? '0' : '') + d.getHours();
    let minutes = (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();
    let seconds = (d.getSeconds() < 10 ? '0' : '') + d.getSeconds();
    console.log(`[${hours}:${minutes}:${seconds}]`.white + ` - ${string}`);
}


if (process.argv.length < 5) {
    log('['.gray + 'Sentry'.brightMagenta + 'API'.white + ']  '.gray + 'Incorrect usage!'.brightMagenta);
    log('['.gray + 'Sentry'.brightMagenta + 'API'.white + ']  '.gray + 'Usage: '.brightMagenta + `node ${scriptName} [From File] [Result File] [Timeout]`.white)
    log('['.gray + 'Sentry'.brightMagenta + 'API'.white + ']  '.gray + 'Example: '.brightMagenta + `node ${scriptName} http.txt proxy.txt 15000`.white)
    process.exit();
}


fs.writeFile(args.resultFile, '', (err) => {});

const proxies = fs.readFileSync(args.fromFile).toString().split('\n');

let aliveProxies = 0;

const checkProxy = (proxy) => {
    const [ip, port] = proxy.split(':');
    const startTime = new Date().getTime();
    return new Promise((resolve, reject) => {
        const req = http.request(
            {
                host: ip,
                port: port,
                method: 'GET',
                path: 'http://www.google.com',
                timeout: args.timeout,
            },
            (res) => {
                const endTime = new Date().getTime();
                if (endTime - startTime <= args.timeout) {
                    aliveProxies++;
                    log('['.gray + 'SUCCESS'.brightGreen + ']  '.gray + `${ip}:${port}`.white + ` - `.gray + `[` + `${endTime - startTime} ms`.blue + `]` + ` - `.gray + `[` + `${aliveProxies}/${proxies.length}`.blue + `]`);
                    fs.appendFileSync(args.resultFile, `${ip}:${port}\n`);
                }
                if (aliveProxies === proxies.filter(Boolean).length && proxies.length > 0) {
                    process.exit();
                }
                resolve();
            }
        );

        req.on('error', (err) => {
            resolve();
        });

        req.end();
    });
};

(async () => {
    const promises = proxies.map((proxy) => checkProxy(proxy.trim()));
    await Promise.all(promises);
})();

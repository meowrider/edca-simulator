const https = require('https');
const fs = require('fs');

async function fetchBinanceData() {
    let allData = [];
    let endTime = Date.now();
    const limit = 1000;
    
    console.log("Fetching historical daily data from Binance...");
    
    for(let i=0; i<4; i++) {
        const url = `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&endTime=${endTime}&limit=${limit}`;
        try {
            const data = await new Promise((resolve, reject) => {
                https.get(url, (res) => {
                    let body = '';
                    res.on('data', chunk => body += chunk);
                    res.on('end', () => {
                        try { resolve(JSON.parse(body)); } 
                        catch(e) { reject(e); }
                    });
                }).on('error', reject);
            });
            
            if(!Array.isArray(data) || data.length === 0) break;
            allData = data.concat(allData);
            endTime = data[0][0] - 1; 
        } catch (error) {
            console.error("Error fetching chunk", i, error);
            break;
        }
    }
    
    // Deduplicate and sort
    let uniqueMap = new Map();
    allData.forEach(d => uniqueMap.set(d[0], parseFloat(d[4])));
    
    let cleanData = Array.from(uniqueMap.entries()).sort((a,b) => a[0] - b[0]);
    
    const outputPath = '/Users/meowmini/.openclaw/workspace/dev_projects/edca_simulator/btc_data.js';
    fs.writeFileSync(outputPath, 'window.btcDailyData = ' + JSON.stringify(cleanData) + ';');
    console.log("Data fetched successfully: " + cleanData.length + " days saved to " + outputPath);
}

fetchBinanceData();
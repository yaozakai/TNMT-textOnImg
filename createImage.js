import fs from 'fs';
import { createCanvas, loadImage, registerFont } from 'canvas';
import open from 'open';
import path from 'path';
// import type { NextApiRequest, NextApiResponse } from 'next';

export default async function createImage() {
    try {
        const filePath = path.join(process.cwd(), 'src', 'pages', 'lib', 'pickData.json');
        const bracketData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        const imagePath = path.join(process.cwd(), 'src', 'pages', 'api', 'wide.png');
        const fontPath = path.join(process.cwd(), 'src', 'pages', 'api', 'Poppins-Regular.ttf');
        
        // Load the wide.png image
        const img = await loadImage(imagePath);
        const canvas = createCanvas(img.width, img.height);
        const ctx = canvas.getContext('2d');

        // Draw the wide.png image on the canvas
        ctx.drawImage(img, 0, 0, img.width, img.height);

        // Register font
        registerFont(fontPath, { family: 'Poppins' });
        ctx.font = '18px Poppins'; // Set the font size to 24 pixels


        // Set initial coordinates
        let xCoord = 0
        let yCoord = 0;

        for (const region in bracketData) {
            switch (region) {
                case 'South':
                    yCoord = 34;
                    xCoord = 20;
                    break;
                case 'East':
                    yCoord = 563;
                    xCoord = 20;
                    break;
                case 'MidWest':
                    yCoord = 34;
                    xCoord = 1760;
                    break;
                default:
                    yCoord = 563;
                    xCoord = 1765;
                    break;
            }

            for (const gameRound of bracketData[region]) {
                let first = true;
                let maxLength = 0;

                if (region === 'West' || region === 'MidWest') {
                    for (const matchUp of gameRound.games) {
                        const lengthA = ctx.measureText(matchUp.teamA).width;
                        const lengthB = ctx.measureText(matchUp.teamB).width;
                        const length = Math.max(lengthA, lengthB);
                        if (length > maxLength) {
                            maxLength = length;
                        }
                    }
                }

                for (const matchUp of gameRound.games) {
                    if (gameRound.round === 1) {
                        if (region === 'South' || region === 'East') {
                            ctx.fillText(matchUp.teamA, xCoord, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;

                        } else {
                            const lengthA = ctx.measureText(matchUp.teamA).width;
                            const lengthB = ctx.measureText(matchUp.teamB).width;
                            ctx.fillText(matchUp.teamA, xCoord + maxLength - lengthA, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord + maxLength - lengthB, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                        }
                    } else if (gameRound.round === 2) {
                        if (region === 'South' || region === 'East') {
                            xCoord = 235;
                        } else {
                            xCoord = 1585;
                        }
                    
                        if (first) {
                            yCoord = (region === 'South' || region === 'West') ? 68 : 598;
                            first = false;
                        }
                    
                        if (region === 'South' || region === 'East') {
                            ctx.fillText(matchUp.teamA, xCoord, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 99;

                        } else {
                            const lengthA = ctx.measureText(matchUp.teamA).width;
                            const lengthB = ctx.measureText(matchUp.teamB).width;
                            ctx.fillText(matchUp.teamA, xCoord + maxLength - lengthA, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord + maxLength - lengthB, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 99;
                        }
                    } else if (gameRound.round === 3) {
                        if (region === 'South' || region === 'East') {
                            xCoord = 444;
                        } else {
                            xCoord = 1375;
                        }
                    
                        if (first) {
                            if (region === 'South') {
                                yCoord = 138;
                            } else if (region === 'West') {
                                yCoord = 132;
                            } else if (region === 'MidWest') {
                                yCoord = 662;
                            } else {
                                yCoord = 668;  // Adjust this value as needed for proper alignment
                            }
                            first = false;
                        }
                    
                        if (region === 'South' || region === 'East') {
                            ctx.fillText(matchUp.teamA, xCoord, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 230;

                        } else {
                            const lengthA = ctx.measureText(matchUp.teamA).width;
                            const lengthB = ctx.measureText(matchUp.teamB).width;
                            ctx.fillText(matchUp.teamA, xCoord + maxLength - lengthA, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord + maxLength - lengthB, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 230;
                        }
                    
                    } else if (gameRound.round === 4) {
                        if (region === 'South' || region === 'East') {
                            xCoord = 634;
                        } else {
                            xCoord = 1190;
                        }
                    
                        if (first) {
                            yCoord = (region === 'South' || region === 'West') ? 268 : 795;
                            first = false;
                        }
                    
                        if (region === 'South' || region === 'East') {
                            ctx.fillText(matchUp.teamA, xCoord, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 230;

                        } else {
                            const lengthA = ctx.measureText(matchUp.teamA).width;
                            const lengthB = ctx.measureText(matchUp.teamB).width;
                            ctx.fillText(matchUp.teamA, xCoord + maxLength - lengthA, yCoord);
                            let textMetrics = ctx.measureText(matchUp.teamA);
                            yCoord += textMetrics.actualBoundingBoxAscent + 20;
                            ctx.fillText(matchUp.teamB, xCoord + maxLength - lengthB, yCoord);
                            textMetrics = ctx.measureText(matchUp.teamB);
                            yCoord += 230;
                        }
                    }
                }
            }
        }

        // Save the modified image
        const out = fs.createWriteStream(path.resolve(__dirname, 'output.png'));
        const stream = canvas.createPNGStream();
        stream.pipe(out);
        out.on('finish', async () => {
            // console.log('The PNG file was created.');
            open(path.resolve(path.resolve(__dirname), 'output.png'), { wait: true });
            // console.log('Image opened with the default viewer.');
        });
        res.status(200).json({ message: 'Image created successfully!' });

    } catch (error) {
        console.error('An error occurred:', error);
        res.status(500).json({ error: 'Internal Server Error' }); 
    }
}

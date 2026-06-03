# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T00:22:23.005770+00:00`
- Price records: `672`
- Market context records: `2713`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_24h` score `10.9603` n `111` status `ready` deltaP `16.3523` edge `1.1537` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6139` n `111` status `ready` deltaP `16.9576` edge `0.6376` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8322` n `143` status `ready` deltaP `5.9441` edge `0.1347` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.4514` n `111` status `ready` deltaP `6.5175` edge `0.7707` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2617` n `143` status `ready` deltaP `12.0758` edge `0.0372` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1215` n `143` status `ready` deltaP `3.6494` edge `0.0095` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2638` n `143` status `ready` deltaP `2.3` edge `0.0355` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.3913` n `143` status `ready` deltaP `1.1495` edge `0.0041` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.4033` n `143` status `ready` deltaP `16.2108` edge `0.2924` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.4426` n `143` status `ready` deltaP `6.7439` edge `0.0743` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.4665` n `143` status `ready` deltaP `1.8488` edge `0.0032` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6866` n `143` status `ready` deltaP `-0.6512` edge `0.0009` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.7929` n `111` status `ready` deltaP `4.3966` edge `-0.0082` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.896` n `143` status `ready` deltaP `-1.049` edge `0.0102` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.912` n `143` status `ready` deltaP `3.797` edge `0.0447` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1876` n `143` status `ready` deltaP `3.0382` edge `0.0195` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.1912` n `143` status `ready` deltaP `-4.1863` edge `0.0125` maxDD `-2.7085`
- `market_context_high->commodity_24h` score `-1.256` n `111` status `ready` deltaP `4.8377` edge `0.1161` maxDD `-12.4171`
- `market_context_high->index_24h` score `-1.5815` n `111` status `ready` deltaP `0.7179` edge `-0.0385` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9681` n `143` status `ready` deltaP `-0.7291` edge `-0.0187` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T00:37:19.060891+00:00`
- Price records: `672`
- Market context records: `2714`
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

- `market_context_high->crypto_alt_24h` score `10.9999` n `111` status `ready` deltaP `16.3523` edge `1.157` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6091` n `111` status `ready` deltaP `16.9576` edge `0.6372` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.7973` n `143` status `ready` deltaP `5.7917` edge `0.1328` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.5029` n `111` status `ready` deltaP `6.5175` edge `0.7773` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2491` n `143` status `ready` deltaP `11.9233` edge `0.0366` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1339` n `143` status `ready` deltaP `3.4997` edge `0.0089` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.271` n `143` status `ready` deltaP `2.3` edge `0.0349` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.4045` n `143` status `ready` deltaP `0.9998` edge `0.004` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.4105` n `143` status `ready` deltaP `16.2108` edge `0.2918` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.4574` n `143` status `ready` deltaP `6.7439` edge `0.0724` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.465` n `143` status `ready` deltaP `1.8488` edge `0.0034` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7021` n `143` status `ready` deltaP `-0.8009` edge `-0.0001` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.8092` n `111` status `ready` deltaP `4.223` edge `-0.0084` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.8972` n `143` status `ready` deltaP `-1.049` edge `0.0101` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9245` n `143` status `ready` deltaP `3.797` edge `0.0431` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.208` n `143` status `ready` deltaP `-4.336` edge `0.0121` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2088` n `143` status `ready` deltaP `2.8857` edge `0.0178` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.2846` n `111` status `ready` deltaP `4.6641` edge `0.1136` maxDD `-12.4171`
- `market_context_high->index_24h` score `-1.641` n `111` status `ready` deltaP `0.5443` edge `-0.0423` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9693` n `143` status `ready` deltaP `-0.7291` edge `-0.0188` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

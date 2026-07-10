# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T07:52:33.564830+00:00`
- Price records: `672`
- Market context records: `6263`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11096`

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

- `news_risk_high->crypto_alt_24h` score `14.8038` n `32` status `ready` deltaP `42.7191` edge `0.9636` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9618` n `32` status `ready` deltaP `50.6873` edge `0.1589` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1805` n `32` status `ready` deltaP `43.8262` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.7506` n `32` status `ready` deltaP `16.1405` edge `0.4512` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4575` n `32` status `ready` deltaP `25.9558` edge `0.0523` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.1437` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1783` n `194` status `ready` deltaP `2.3752` edge `0.2665` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.3843` n `192` status `ready` deltaP `-1.2322` edge `0.3768` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3649` n `32` status `ready` deltaP `14.128` edge `0.1275` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7912` n `32` status `ready` deltaP `10.5726` edge `0.0771` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1526` n `32` status `ready` deltaP `9.3428` edge `0.0053` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.2179` n `192` status `ready` deltaP `4.3445` edge `0.0446` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2638` n `194` status `ready` deltaP `1.5973` edge `0.0001` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3076` n `192` status `ready` deltaP `17.8211` edge `0.0986` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5143` n `192` status `ready` deltaP `3.9762` edge `0.0263` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5612` n `194` status `ready` deltaP `-0.6652` edge `0.0023` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7029` n `32` status `ready` deltaP `-2.3952` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7909` n `194` status `ready` deltaP `2.244` edge `-0.001` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8469` n `194` status `ready` deltaP `5.3213` edge `0.0312` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9701` n `194` status `ready` deltaP `3.6576` edge `0.028` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

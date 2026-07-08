# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T22:52:32.494618+00:00`
- Price records: `672`
- Market context records: `6133`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.6119` n `30` status `ready` deltaP `39.3402` edge `0.6368` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7704` n `30` status `ready` deltaP `68.75` edge `0.1892` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3335` n `32` status `ready` deltaP `45.1982` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3787` n `32` status `ready` deltaP `28.5928` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.3855` n `195` status `ready` deltaP `0.5052` edge `0.2129` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2215` n `32` status `ready` deltaP `13.3795` edge `0.1141` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.619` n `32` status `ready` deltaP `8.4768` edge `0.069` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4503` n `195` status `ready` deltaP `4.2073` edge `0.1012` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1246` n `30` status `ready` deltaP `8.368` edge `0.0154` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.284` n `195` status `ready` deltaP `1.2851` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3449` n `195` status `ready` deltaP `-2.6118` edge `0.2419` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5647` n `30` status `ready` deltaP `14.0973` edge `-0.1205` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6808` n `195` status `ready` deltaP `3.0848` edge `0.0109` maxDD `-3.4996`
- `news_risk_high->crypto_major_24h` score `-0.7338` n `30` status `ready` deltaP `9.6875` edge `-0.0807` maxDD `-4.2368`
- `market_context_high->commodity_1h` score `-0.7715` n `195` status `ready` deltaP `-2.2885` edge `-0.0044` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8042` n `32` status `ready` deltaP `-3.4431` edge `-0.0304` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.8126` n `195` status `ready` deltaP `-0.7086` edge `0.0121` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8715` n `195` status `ready` deltaP `1.9415` edge `-0.0057` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9569` n `195` status `ready` deltaP `3.4608` edge `0.0295` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9765` n `195` status `ready` deltaP `4.1648` edge `0.0238` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

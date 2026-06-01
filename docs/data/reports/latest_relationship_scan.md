# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T16:37:30.442208+00:00`
- Price records: `672`
- Market context records: `2578`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `6.2479` n `146` status `ready` deltaP `26.8731` edge `0.6094` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.7542` n `121` status `ready` deltaP `19.0413` edge `0.3854` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.3872` n `146` status `ready` deltaP `18.2697` edge `0.4248` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1959` n `121` status `ready` deltaP `10.5946` edge `0.5297` maxDD `-25.3874`
- `market_context_high->crypto_alt_1h` score `1.5727` n `146` status `ready` deltaP `12.1791` edge `0.1686` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.2814` n `146` status `ready` deltaP `9.8187` edge `0.1463` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0937` n `146` status `ready` deltaP `10.9589` edge `0.1375` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.8638` n `121` status `ready` deltaP `18.0756` edge `0.0185` maxDD `-2.3615`
- `market_context_high->index_24h` score `0.6527` n `121` status `ready` deltaP `6.9846` edge `0.1059` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.4561` n `121` status `ready` deltaP `0.7949` edge `0.691` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.3362` n `146` status `ready` deltaP `9.28` edge `0.0503` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1575` n `146` status `ready` deltaP `3.642` edge `0.012` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4212` n `146` status `ready` deltaP `1.8005` edge `0.0192` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4458` n `146` status `ready` deltaP `5.3523` edge `0.015` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5328` n `146` status `ready` deltaP `4.807` edge `0.0623` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6245` n `146` status `ready` deltaP `-0.3855` edge `0.004` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.6272` n `146` status `ready` deltaP `1.1115` edge `0.0151` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.8133` n `146` status `ready` deltaP `-0.3773` edge `0.0186` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8256` n `146` status `ready` deltaP `0.5367` edge `0.0134` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-1.0997` n `121` status `ready` deltaP `0.8436` edge `0.0021` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

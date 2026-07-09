# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T16:37:07.767099+00:00`
- Price records: `672`
- Market context records: `6198`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.7322` n `32` status `ready` deltaP `42.2194` edge `0.7943` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.8027` n `32` status `ready` deltaP `59.3537` edge `0.1712` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0597` n `32` status `ready` deltaP `42.3754` edge `0.0604` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3368` n `32` status `ready` deltaP `28.1437` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1513` n `32` status `ready` deltaP `15.625` edge `0.2496` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8177` n `192` status `ready` deltaP `1.0635` edge `0.2452` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4398` n `32` status `ready` deltaP `14.5771` edge `0.1341` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7858` n `32` status `ready` deltaP `9.8241` edge `0.0814` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.3909` n `32` status `ready` deltaP `17.5383` edge `-0.0638` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.2408` n `192` status `ready` deltaP `-2.6708` edge `0.2911` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0068` n `192` status `ready` deltaP `19.8023` edge `0.1257` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.224` n `32` status `ready` deltaP `9.1412` edge `-0.0025` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.298` n `192` status `ready` deltaP `1.0604` edge `-0.0007` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.6781` n `192` status `ready` deltaP `-1.7964` edge `0.0001` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7106` n `192` status `ready` deltaP `2.842` edge `0.0087` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.807` n `192` status `ready` deltaP `0.7753` edge `0.0193` maxDD `-2.671`
- `news_risk_high->metal_1h` score `-0.8119` n `32` status `ready` deltaP `-3.8922` edge `-0.0284` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.8599` n `192` status `ready` deltaP `4.6813` edge `0.0353` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8779` n `192` status `ready` deltaP `4.0949` edge `0.0354` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9084` n `192` status `ready` deltaP `1.3161` edge `-0.0046` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

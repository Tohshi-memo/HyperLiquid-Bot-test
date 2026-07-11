# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T06:37:38.771439+00:00`
- Price records: `672`
- Market context records: `6364`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `14.7182` n `32` status `ready` deltaP `40.1042` edge `0.9739` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3064` n `32` status `ready` deltaP `52.4306` edge `0.176` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4167` n `32` status `ready` deltaP `17.5347` edge `0.5273` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0644` n `32` status `ready` deltaP `42.1494` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.9373` n `32` status `ready` deltaP `34.0278` edge `0.1218` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3368` n `32` status `ready` deltaP `28.1437` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5466` n `32` status `ready` deltaP `15.0262` edge `0.1448` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9299` n `32` status `ready` deltaP `11.6205` edge `0.0879` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5201` n `209` status `ready` deltaP `15.6049` edge `0.0423` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1563` n `220` status `ready` deltaP `-6.9243` edge `0.16` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1161` n `209` status `ready` deltaP `8.2966` edge `0.022` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.4269` n `220` status `ready` deltaP `3.0648` edge `0.0026` maxDD `-1.8877`
- `news_risk_high->unknown_1h` score `-0.4455` n `32` status `ready` deltaP `5.6325` edge `-0.0402` maxDD `-0.7581`
- `market_context_high->commodity_24h` score `-0.4909` n `130` status `ready` deltaP `-3.4241` edge `0.1463` maxDD `-6.2457`
- `market_context_high->metal_24h` score `-0.5934` n `130` status `ready` deltaP `15.5796` edge `0.0769` maxDD `-11.8809`
- `market_context_high->index_1h` score `-0.616` n `220` status `ready` deltaP `-1.5024` edge `0.003` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6993` n `220` status `ready` deltaP `-0.4927` edge `-0.0016` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7089` n `32` status `ready` deltaP `0.5208` edge `-0.0072` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7333` n `32` status `ready` deltaP `-2.8443` edge `-0.0253` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.9592` n `220` status `ready` deltaP `5.4273` edge `0.0161` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

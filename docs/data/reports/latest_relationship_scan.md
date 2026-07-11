# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T22:07:24.844142+00:00`
- Price records: `672`
- Market context records: `6435`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.7473` n `32` status `ready` deltaP `30.2083` edge `0.7923` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.4597` n `146` status `ready` deltaP `21.3304` edge `0.8928` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4741` n `32` status `ready` deltaP `54.1667` edge `0.1784` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1206` n `32` status `ready` deltaP `42.9116` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1113` n `32` status `ready` deltaP `35.2431` edge `0.1282` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2912` n `32` status `ready` deltaP `11.8056` edge `0.4212` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4566` n `32` status `ready` deltaP `29.6407` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4516` n `32` status `ready` deltaP `13.5292` edge `0.1426` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3551` n `193` status `ready` deltaP `-5.0952` edge `0.237` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8287` n `32` status `ready` deltaP `9.6744` edge `0.0879` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0675` n `192` status `ready` deltaP `7.5838` edge `0.0227` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.1166` n `192` status `ready` deltaP `8.1809` edge `0.0404` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2298` n `32` status `ready` deltaP `7.1295` edge `-0.0322` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4978` n `146` status `ready` deltaP `15.0186` edge `0.0929` maxDD `-11.8809`
- `market_context_high->unknown_4h` score `-0.5308` n `192` status `ready` deltaP `-14.9644` edge `0.2961` maxDD `-10.5788`
- `news_risk_high->metal_1h` score `-0.5636` n `32` status `ready` deltaP `0.2994` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5642` n `193` status `ready` deltaP `0.5585` edge `0.0017` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6042` n `193` status `ready` deltaP `-1.0882` edge `-0.0019` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.6307` n `192` status `ready` deltaP `6.4533` edge `0.046` maxDD `-8.2573`
- `market_context_high->index_1h` score `-0.703` n `193` status `ready` deltaP `-3.1608` edge `0.0029` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

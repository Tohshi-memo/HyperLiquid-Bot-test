# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T17:22:34.389345+00:00`
- Price records: `672`
- Market context records: `4537`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `54.401` n `176` status `ready` deltaP `7.6144` edge `4.5327` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.5071` n `174` status `ready` deltaP `8.4823` edge `2.6423` maxDD `-7.5275`
- `market_context_high->commodity_1h` score `-0.539` n `176` status `ready` deltaP `1.1125` edge `0.0154` maxDD `-3.0206`
- `market_context_high->fx_4h` score `-0.5403` n `174` status `ready` deltaP `5.6052` edge `0.0016` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6453` n `176` status `ready` deltaP `0.7519` edge `-0.0029` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-0.9959` n `174` status `ready` deltaP `4.2946` edge `0.0653` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.015` n `176` status `ready` deltaP `-2.8443` edge `-0.0103` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0872` n `176` status `ready` deltaP `-1.6501` edge `0.0191` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.2423` n `174` status `ready` deltaP `-0.3977` edge `-0.011` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.5725` n `174` status `ready` deltaP `0.9128` edge `0.0178` maxDD `-10.3725`
- `market_context_high->unknown_24h` score `-2.6713` n `174` status `ready` deltaP `2.1492` edge `-0.1446` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4568` n `176` status `ready` deltaP `-4.6339` edge `-0.0726` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.366` n `176` status `ready` deltaP `-3.5009` edge `-0.0951` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5337` n `174` status `ready` deltaP `-13.9967` edge `-0.0166` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6965` n `174` status `ready` deltaP `-8.4351` edge `-0.1366` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2257` n `176` status `ready` deltaP `-4.2188` edge `-0.1154` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3407` n `174` status `ready` deltaP `4.4421` edge `0.0161` maxDD `-46.5954`
- `market_context_high->crypto_alt_4h` score `-13.272` n `174` status `ready` deltaP `-1.6768` edge `-0.2291` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.5825` n `174` status `ready` deltaP `-0.7483` edge `-0.2684` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.4905` n `174` status `ready` deltaP `-7.4362` edge `-0.3064` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

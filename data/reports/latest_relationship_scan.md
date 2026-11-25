# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T15:22:29.496082+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32192.0473` n `45` status `ready` deltaP `2.3153` edge `2682.6646` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21904.7579` n `45` status `ready` deltaP `3.0251` edge `1825.3902` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `957.0923` n `31` status `ready` deltaP `2.5304` edge `79.7584` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `651.8104` n `31` status `ready` deltaP `4.2437` edge `54.2949` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `468.3731` n `31` status `ready` deltaP `5.7292` edge `38.9929` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.3261` n `31` status `ready` deltaP `51.0417` edge `3.4369` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.9879` n `31` status `ready` deltaP `52.6042` edge `3.1483` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.5435` n `31` status `ready` deltaP `55.2083` edge `2.8439` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9585` n `31` status `ready` deltaP `27.3701` edge `0.9011` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.9414` n `31` status `ready` deltaP `41.2355` edge `0.7477` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.3435` n `31` status `ready` deltaP `37.9869` edge `0.7401` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5166` n `31` status `ready` deltaP `19.0647` edge `0.9783` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.2289` n `31` status `ready` deltaP `51.7361` edge `0.2575` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3492` n `31` status `ready` deltaP `45.7045` edge `0.1539` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0445` n `31` status `ready` deltaP `20.8856` edge `0.2165` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4316` n `31` status `ready` deltaP `36.4625` edge `0.0689` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7331` n `31` status `ready` deltaP `11.6573` edge `0.3188` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7214` n `31` status `ready` deltaP `31.9925` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4834` n `31` status `ready` deltaP `13.4537` edge `0.2644` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.47` n `45` status `ready` deltaP `30.2405` edge `0.0327` maxDD `-0.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

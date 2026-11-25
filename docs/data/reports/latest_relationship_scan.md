# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T21:37:33.342241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3720`

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

- `market_context_high->unknown_1h` score `32156.0162` n `45` status `ready` deltaP `1.4171` edge `2679.668` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21827.6326` n `45` status `ready` deltaP `1.958` edge `1818.9702` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `921.0613` n `31` status `ready` deltaP `1.6322` edge `76.7618` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `574.6851` n `31` status `ready` deltaP `3.1766` edge `47.8749` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `294.9503` n `31` status `ready` deltaP `5.7292` edge `24.541` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.1535` n `31` status `ready` deltaP `52.0833` edge `3.4989` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.24` n `31` status `ready` deltaP `53.8194` edge `3.1612` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.8399` n `31` status `ready` deltaP `53.2986` edge `2.798` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.7758` n `31` status `ready` deltaP `40.0202` edge `0.742` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9167` n `31` status `ready` deltaP `26.3031` edge `0.8214` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.5033` n `31` status `ready` deltaP `37.8344` edge `0.6711` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4703` n `31` status `ready` deltaP `53.2986` edge `0.2672` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7502` n `31` status `ready` deltaP `17.5403` edge `0.8902` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3492` n `31` status `ready` deltaP `45.7045` edge `0.1539` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6019` n `31` status `ready` deltaP `19.8377` edge `0.1866` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3414` n `31` status `ready` deltaP `36.31` edge `0.0624` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6411` n `31` status `ready` deltaP `31.3937` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3994` n `31` status `ready` deltaP `9.7112` edge `0.289` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3327` n `45` status `ready` deltaP `28.8685` edge `0.0304` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2167` n `31` status `ready` deltaP `12.4058` edge `0.2372` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

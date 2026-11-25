# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T12:07:26.484419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32216.3893` n `45` status `ready` deltaP `2.0159` edge `2684.6951` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21956.0077` n `45` status `ready` deltaP `3.1776` edge `1829.66` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `981.4344` n `31` status `ready` deltaP `2.231` edge `81.7889` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `703.0602` n `31` status `ready` deltaP `4.3962` edge `58.5647` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `621.7187` n `31` status `ready` deltaP `5.7292` edge `51.7717` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.2556` n `31` status `ready` deltaP `48.7847` edge `3.2794` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.772` n `31` status `ready` deltaP `50.6944` edge `3.0597` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.598` n `31` status `ready` deltaP `53.125` edge `2.779` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8469` n `31` status `ready` deltaP `27.3701` edge `0.8918` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.6762` n `31` status `ready` deltaP `41.2355` edge `0.7256` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2099` n `31` status `ready` deltaP `37.682` edge `0.731` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5313` n `31` status `ready` deltaP `18.9123` edge `0.9812` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.8299` n `31` status `ready` deltaP `49.4792` edge `0.2393` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1809` n `31` status `ready` deltaP `43.7948` edge `0.1526` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0134` n `31` status `ready` deltaP `20.7359` edge `0.2149` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.382` n `31` status `ready` deltaP `36.1576` edge `0.0668` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7658` n `31` status `ready` deltaP `11.9567` edge `0.321` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7214` n `31` status `ready` deltaP `31.9925` edge `0.022` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5894` n `45` status `ready` deltaP `31.6124` edge `0.0335` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4678` n `31` status `ready` deltaP `13.304` edge `0.2634` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

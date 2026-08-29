# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T15:52:25.973817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11300`

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

- `news_risk_high->unknown_24h` score `44.1179` n `62` status `ready` deltaP `10.2095` edge `3.7058` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `19.5996` n `62` status `ready` deltaP `30.3708` edge `1.7684` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `9.1108` n `104` status `ready` deltaP `20.2591` edge `0.6974` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.406` n `80` status `ready` deltaP `11.5854` edge `0.5156` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.5667` n `104` status `ready` deltaP `33.0261` edge `0.2623` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6092` n `80` status `ready` deltaP `5.2246` edge `0.2183` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5487` n `120` status `ready` deltaP `18.2521` edge `0.1339` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.5314` n `80` status `ready` deltaP `36.4939` edge `0.0226` maxDD `-0.3953`
- `news_risk_high->equity_24h` score `1.0725` n `62` status `ready` deltaP `19.1308` edge `0.2942` maxDD `-18.7388`
- `market_context_high->unknown_1h` score `1.0347` n `132` status `ready` deltaP `9.6943` edge `0.0697` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7723` n `80` status `ready` deltaP `14.6407` edge `0.0056` maxDD `-0.108`
- `risk_on_high->crypto_alt_1h` score `0.7148` n `32` status `ready` deltaP `13.2298` edge `0.051` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.7148` n `32` status `ready` deltaP `13.2298` edge `0.051` maxDD `-2.1381`
- `risk_on_high->metal_1h` score `0.6954` n `32` status `ready` deltaP `10.5539` edge `0.009` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.6954` n `32` status `ready` deltaP `10.5539` edge `0.009` maxDD `-0.0463`
- `news_risk_high->metal_24h` score `0.5289` n `62` status `ready` deltaP `31.2892` edge `0.0036` maxDD `-7.5508`
- `news_risk_high->commodity_1h` score `0.4167` n `80` status `ready` deltaP `12.0509` edge `0.0051` maxDD `-0.5618`
- `news_risk_high->index_24h` score `0.2218` n `62` status `ready` deltaP `15.0649` edge `0.0093` maxDD `-2.1707`
- `market_context_high->crypto_major_4h` score `0.213` n `120` status `ready` deltaP `19.3089` edge `0.2341` maxDD `-20.9394`
- `news_risk_high->crypto_major_24h` score `0.0947` n `62` status `ready` deltaP `15.485` edge `0.2843` maxDD `-25.3651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T04:52:24.687614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3221.0365` n `31` status `ready` deltaP `1.6322` edge `268.4264` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.7106` n `31` status `ready` deltaP `3.7864` edge `265.9563` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.7594` n `31` status `ready` deltaP `32.8125` edge `1.7612` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.2085` n `31` status `ready` deltaP `32.2917` edge `1.5521` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.0968` n `31` status `ready` deltaP `31.9444` edge `1.2951` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2342` n `31` status `ready` deltaP `23.4067` edge `0.7005` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.4638` n `31` status `ready` deltaP `33.2612` edge `0.4483` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9943` n `31` status `ready` deltaP `16.4732` edge `0.8004` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.8063` n `31` status `ready` deltaP `19.8813` edge `0.3788` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.7721` n `31` status `ready` deltaP `39.9754` edge `0.144` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.7523` n `31` status `ready` deltaP `33.8542` edge `0.087` maxDD `0.0`
- `news_risk_high->index_4h` score `2.734` n `31` status `ready` deltaP `31.432` edge `0.0443` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.7024` n `31` status `ready` deltaP `16.5443` edge `0.1336` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3847` n `31` status `ready` deltaP `28.8488` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0729` n `31` status `ready` deltaP `6.8669` edge `0.2661` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8598` n `31` status `ready` deltaP `10.0106` edge `0.2074` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1776` n `31` status `ready` deltaP `25.5408` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4779` n `31` status `ready` deltaP `12.5098` edge `0.0336` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0341` n `31` status `ready` deltaP `6.9974` edge `-0.0025` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6108` n `31` status `ready` deltaP `-4.4572` edge `0.005` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

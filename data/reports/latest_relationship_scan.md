# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T06:22:29.881428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3222.3361` n `31` status `ready` deltaP `1.6322` edge `268.5347` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.529` n `31` status `ready` deltaP `3.7864` edge `265.2745` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.2745` n `31` status `ready` deltaP `31.7708` edge `1.6444` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.9936` n `31` status `ready` deltaP `31.25` edge `1.4578` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8926` n `31` status `ready` deltaP `30.9028` edge `1.2017` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0968` n `31` status `ready` deltaP `22.9494` edge `0.6921` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.0584` n `31` status `ready` deltaP `32.499` edge `0.4196` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.8229` n `31` status `ready` deltaP `15.8635` edge `0.7825` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.6176` n `31` status `ready` deltaP `19.1869` edge `0.3677` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.678` n `31` status `ready` deltaP `38.9337` edge `0.1431` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.561` n `31` status `ready` deltaP `32.8125` edge `0.078` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6746` n `31` status `ready` deltaP `30.9747` edge `0.0424` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6017` n `31` status `ready` deltaP `16.0952` edge `0.1282` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3715` n `31` status `ready` deltaP `28.6991` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0815` n `31` status `ready` deltaP `6.8669` edge `0.2672` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8473` n `31` status `ready` deltaP `9.5615` edge `0.2088` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1652` n `31` status `ready` deltaP `25.2414` edge `0.009` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.449` n `31` status `ready` deltaP `12.5098` edge `0.0299` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.061` n `31` status `ready` deltaP `6.0828` edge `-0.0086` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6551` n `31` status `ready` deltaP `-4.9063` edge `0.0043` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

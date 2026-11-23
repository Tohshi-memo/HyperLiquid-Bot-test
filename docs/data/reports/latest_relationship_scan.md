# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T21:52:31.486029+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4572`

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

- `market_context_high->unknown_1h` score `32435.8945` n `45` status `ready` deltaP `2.7644` edge `2702.9822` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22262.5578` n `45` status `ready` deltaP `3.4824` edge `1855.2038` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1226.3651` n `31` status `ready` deltaP `2.9795` edge `102.1948` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1027.2046` n `31` status `ready` deltaP `4.701` edge `85.5747` maxDD `-0.119`
- `news_risk_high->equity_24h` score `39.1047` n `31` status `ready` deltaP `43.9236` edge `2.9659` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.0191` n `31` status `ready` deltaP `45.8333` edge `2.6127` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9211` n `31` status `ready` deltaP `45.8333` edge `2.2712` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.4224` n `31` status `ready` deltaP `45.4021` edge `0.76` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.1954` n `31` status `ready` deltaP `22.4921` edge `0.7867` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6599` n `31` status `ready` deltaP `30.8222` edge `0.5644` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.4604` n `31` status `ready` deltaP `55.0795` edge `0.184` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2794` n `31` status `ready` deltaP `12.3574` edge `0.8644` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0407` n `31` status `ready` deltaP `42.0139` edge `0.2233` maxDD `0.0`
- `market_context_high->fx_4h` score `3.2793` n `45` status `ready` deltaP `39.082` edge `0.0412` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2313` n `31` status `ready` deltaP `18.0413` edge `0.1677` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9393` n `31` status `ready` deltaP `32.499` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5177` n `31` status `ready` deltaP `30.0464` edge `0.018` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4999` n `31` status `ready` deltaP `11.0585` edge `0.2929` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1296` n `31` status `ready` deltaP `10.4597` edge `0.239` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5539` n `31` status `ready` deltaP `30.0318` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

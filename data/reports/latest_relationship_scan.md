# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T12:07:43.015802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4506`

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

- `market_context_high->unknown_1h` score `23595.4167` n `60` status `ready` deltaP `0.1796` edge `1966.2997` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `15861.4771` n `60` status `ready` deltaP `4.5935` edge `1321.773` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.6966` n `31` status `ready` deltaP `3.728` edge `108.1341` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1103.2738` n `31` status `ready` deltaP `4.701` edge `91.9138` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.3421` n `31` status `ready` deltaP `50.5208` edge `3.4417` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9789` n `31` status `ready` deltaP `48.6111` edge `2.7575` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5696` n `31` status `ready` deltaP `48.7847` edge `2.3889` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.4639` n `31` status `ready` deltaP `51.1313` edge `0.8086` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3582` n `31` status `ready` deltaP `32.9564` edge `0.6917` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1572` n `31` status `ready` deltaP `21.7299` edge `0.7886` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.1102` n `31` status `ready` deltaP `48.4375` edge `0.2696` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.3349` n `31` status `ready` deltaP `53.6907` edge `0.1828` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1873` n `31` status `ready` deltaP `11.2903` edge `0.8597` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6979` n `31` status `ready` deltaP `18.7898` edge `0.2016` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2645` n `31` status `ready` deltaP `34.3283` edge `0.0692` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6351` n `31` status `ready` deltaP `30.9446` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3558` n `31` status `ready` deltaP `8.9627` edge `0.2884` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9544` n `31` status `ready` deltaP `7.6154` edge `0.2355` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5314` n `31` status `ready` deltaP `29.1336` edge `0.03` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4531` n `31` status `ready` deltaP `20.2842` edge `0.1068` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

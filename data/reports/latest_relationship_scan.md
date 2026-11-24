# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T20:37:29.490162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32268.1478` n `45` status `ready` deltaP `1.4171` edge `2689.0123` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22060.5433` n `45` status `ready` deltaP `3.1776` edge `1838.3713` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1033.1929` n `31` status `ready` deltaP `1.6322` edge `86.1061` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `807.5958` n `31` status `ready` deltaP `4.3962` edge `67.276` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.5295` n `31` status `ready` deltaP `50.1736` edge `2.8763` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.956` n `31` status `ready` deltaP `43.75` edge `2.788` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.0619` n `31` status `ready` deltaP `48.9583` edge `2.5121` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7403` n `31` status `ready` deltaP `26.6079` edge `0.888` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1014` n `31` status `ready` deltaP `41.2355` edge `0.6777` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.36` n `31` status `ready` deltaP `34.6332` edge `0.6805` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.29` n `31` status `ready` deltaP `17.5403` edge `0.9594` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.0203` n `31` status `ready` deltaP `50.9129` edge `0.1751` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5437` n `31` status `ready` deltaP `41.6667` edge `0.1842` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5708` n `31` status `ready` deltaP `18.9395` edge `0.19` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0635` n `31` status `ready` deltaP `32.9564` edge `0.0616` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7391` n `45` status `ready` deltaP `33.2893` edge `0.0348` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6971` n `31` status `ready` deltaP `12.4058` edge `0.3092` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5572` n `31` status `ready` deltaP `30.3458` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.358` n `31` status `ready` deltaP `12.1064` edge `0.2573` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6509` n `31` status `ready` deltaP `21.8086` edge `0.122` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

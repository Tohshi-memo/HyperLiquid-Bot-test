# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T11:22:32.384571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_1h` score `3233.3665` n `31` status `ready` deltaP `1.6322` edge `269.4539` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3231.5779` n `31` status `ready` deltaP `3.4815` edge `269.2806` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `103.0746` n `31` status `ready` deltaP `1.6322` edge `8.5881` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `36.5475` n `31` status `ready` deltaP `43.9236` edge `2.7528` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.3637` n `31` status `ready` deltaP `44.7917` edge `2.7317` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6154` n `31` status `ready` deltaP `44.0972` edge `2.2573` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.011` n `31` status `ready` deltaP `27.8275` edge `0.8191` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.849` n `31` status `ready` deltaP `39.8161` edge `0.6867` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.8015` n `31` status `ready` deltaP `30.4716` edge `0.5578` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0666` n `31` status `ready` deltaP `19.9793` edge `0.9145` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.079` n `31` status `ready` deltaP `45.3125` edge `0.2045` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0694` n `31` status `ready` deltaP `42.9268` edge `0.1491` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8837` n `31` status `ready` deltaP `21.3347` edge `0.2001` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5793` n `31` status `ready` deltaP `38.4442` edge `0.068` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.8148` n `31` status `ready` deltaP `33.1901` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5203` n `31` status `ready` deltaP `10.1603` edge `0.3015` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2892` n `31` status `ready` deltaP `13.1543` edge `0.2415` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9984` n `31` status `ready` deltaP `25.5901` edge `0.0244` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5056` n `31` status `ready` deltaP `29.433` edge `0.0247` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0613` n `31` status `ready` deltaP `16.1683` edge `0.084` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

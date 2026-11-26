# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T12:37:27.048086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3467`

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

- `news_risk_high->unknown_1h` score `3231.2388` n `31` status `ready` deltaP `1.7819` edge `269.2756` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.3135` n `31` status `ready` deltaP `3.4815` edge `268.0919` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `100.947` n `31` status `ready` deltaP `1.7819` edge `8.4098` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `35.5011` n `31` status `ready` deltaP `43.9236` edge `2.6656` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.1628` n `31` status `ready` deltaP `43.0556` edge `2.6432` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.6447` n `31` status `ready` deltaP `43.2292` edge `2.1822` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7929` n `31` status `ready` deltaP `27.0653` edge `0.806` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6202` n `31` status `ready` deltaP `39.2064` edge `0.6717` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.5161` n `31` status `ready` deltaP `29.6035` edge `0.5398` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9821` n `31` status `ready` deltaP `19.6744` edge `0.9057` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8776` n `31` status `ready` deltaP `44.4444` edge `0.1935` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9856` n `31` status `ready` deltaP `42.0587` edge `0.1479` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7782` n `31` status `ready` deltaP `20.5862` edge `0.1963` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5018` n `31` status `ready` deltaP `37.8344` edge `0.0656` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7489` n `31` status `ready` deltaP `32.4416` edge `0.0213` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.514` n `31` status `ready` deltaP `10.1603` edge `0.3007` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2713` n `31` status `ready` deltaP `13.0046` edge `0.2402` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9716` n `31` status `ready` deltaP `25.2853` edge `0.0242` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4776` n `31` status `ready` deltaP `28.9839` edge `0.0241` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0054` n `31` status `ready` deltaP `15.5586` edge `0.0809` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T19:37:32.774078+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9981`

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

- `market_context_high->unknown_1h` score `86.2723` n `47` status `ready` deltaP `10.116` edge `7.129` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.8121` n `47` status `ready` deltaP `30.4226` edge `3.5708` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.8636` n `47` status `ready` deltaP `24.782` edge `2.3614` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.8439` n `47` status `ready` deltaP `30.9434` edge `1.8996` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8334` n `47` status `ready` deltaP `34.7628` edge `0.434` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9411` n `47` status `ready` deltaP `33.6695` edge `0.1278` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4663` n `111` status `ready` deltaP `16.6937` edge `0.2266` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9461` n `47` status `ready` deltaP `33.7215` edge `0.0361` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8135` n `111` status `ready` deltaP `18.6398` edge `0.1537` maxDD `-1.8141`
- `news_risk_high->crypto_major_24h` score `2.7222` n `84` status `ready` deltaP `-2.4801` edge `1.2698` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `2.5357` n `106` status `ready` deltaP `8.8558` edge `0.3974` maxDD `-15.9436`
- `news_risk_high->crypto_major_4h` score `2.4893` n `106` status `ready` deltaP `16.4692` edge `0.3108` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.4107` n `47` status `ready` deltaP `17.1445` edge `0.1284` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.8753` n `84` status `ready` deltaP `20.6846` edge `0.0907` maxDD `-1.7857`
- `news_risk_high->fx_4h` score `1.7796` n `106` status `ready` deltaP `25.394` edge `0.0426` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.6016` n `111` status `ready` deltaP `20.2622` edge `0.0269` maxDD `-0.6142`
- `news_risk_high->unknown_1h` score `1.473` n `111` status `ready` deltaP `-4.5476` edge `0.1775` maxDD `-0.9543`
- `market_context_high->index_1h` score `0.9858` n `47` status `ready` deltaP `14.9095` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9199` n `47` status `ready` deltaP `11.4664` edge `0.0405` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8942` n `84` status `ready` deltaP `23.4871` edge `0.1029` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

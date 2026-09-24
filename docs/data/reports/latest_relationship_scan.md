# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T17:37:30.991150+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10041`

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

- `market_context_high->unknown_1h` score `87.1075` n `47` status `ready` deltaP `10.116` edge `7.1986` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.9157` n `47` status `ready` deltaP `30.4226` edge `3.4961` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.3812` n `47` status `ready` deltaP `24.782` edge `2.3212` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.5108` n `47` status `ready` deltaP `29.5545` edge `1.8811` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8262` n `47` status `ready` deltaP `34.7628` edge `0.4334` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.3038` n `92` status `ready` deltaP `0.936` edge `1.578` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7544` n `47` status `ready` deltaP `32.2806` edge `0.1215` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.1855` n `92` status `ready` deltaP `-1.3512` edge `1.1187` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.047` n `47` status `ready` deltaP `34.7885` edge `0.0374` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.9575` n `116` status `ready` deltaP `14.2939` edge `0.2002` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.5728` n `116` status `ready` deltaP `17.2517` edge `0.1429` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.5373` n `47` status `ready` deltaP `17.6018` edge `0.1359` maxDD `-1.3444`
- `news_risk_high->crypto_major_4h` score `2.3023` n `113` status `ready` deltaP `16.2314` edge `0.2968` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.1907` n `113` status `ready` deltaP `8.7578` edge `0.3693` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.5911` n `113` status `ready` deltaP `23.4135` edge `0.0401` maxDD `-0.421`
- `news_risk_high->metal_24h` score `1.1691` n `92` status `ready` deltaP `25.2038` edge `0.1267` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1218` n `92` status `ready` deltaP `27.8004` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0086` n `47` status `ready` deltaP `15.2089` edge `0.0105` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8887` n `47` status `ready` deltaP `11.167` edge `0.0399` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.8724` n `116` status `ready` deltaP `15.6618` edge `0.0218` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

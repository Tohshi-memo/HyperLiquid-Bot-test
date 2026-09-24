# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T18:07:32.440403+00:00`
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

- `market_context_high->unknown_1h` score `86.7007` n `47` status `ready` deltaP `10.116` edge `7.1647` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.1437` n `47` status `ready` deltaP `30.4226` edge `3.5151` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.512` n `47` status `ready` deltaP `24.782` edge `2.3321` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.5985` n `47` status `ready` deltaP `29.9017` edge `1.8861` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8274` n `47` status `ready` deltaP `34.7628` edge `0.4335` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `4.7827` n `90` status `ready` deltaP `0.1389` edge `1.5165` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.8026` n `47` status `ready` deltaP `32.6278` edge `0.1232` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.1659` n `114` status `ready` deltaP `15.5794` edge `0.209` maxDD `-1.5895`
- `market_context_high->index_4h` score `3.0336` n `47` status `ready` deltaP `34.6361` edge `0.0373` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.7705` n `114` status `ready` deltaP `18.5524` edge `0.1507` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `2.7036` n `90` status `ready` deltaP `-1.9792` edge `1.0611` maxDD `-49.7699`
- `market_context_high->equity_4h` score `2.5253` n `47` status `ready` deltaP `17.6018` edge `0.1349` maxDD `-1.3444`
- `news_risk_high->crypto_major_4h` score `2.424` n `111` status `ready` deltaP `16.6131` edge `0.3044` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.3336` n `111` status `ready` deltaP `9.0598` edge `0.3792` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.6109` n `111` status `ready` deltaP `23.5402` edge `0.0409` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.1203` n `90` status `ready` deltaP `16.25` edge `0.0828` maxDD `-1.8221`
- `news_risk_high->metal_24h` score `1.1128` n `90` status `ready` deltaP `24.8264` edge `0.122` maxDD `-7.2536`
- `news_risk_high->metal_1h` score `1.0811` n `114` status `ready` deltaP `16.7507` edge `0.0236` maxDD `-0.6142`
- `news_risk_high->fx_24h` score `1.0619` n `90` status `ready` deltaP `26.9791` edge `0.1194` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0122` n `47` status `ready` deltaP `15.2089` edge `0.0108` maxDD `-0.2275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

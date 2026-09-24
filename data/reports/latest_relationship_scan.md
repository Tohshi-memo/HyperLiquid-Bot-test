# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T18:22:29.825947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10053`

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

- `market_context_high->unknown_1h` score `86.6815` n `47` status `ready` deltaP `10.116` edge `7.1631` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.2409` n `47` status `ready` deltaP `30.4226` edge `3.5232` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.5672` n `47` status `ready` deltaP `24.782` edge `2.3367` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.64` n `47` status `ready` deltaP `30.0753` edge `1.8884` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8286` n `47` status `ready` deltaP `34.7628` edge `0.4336` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `4.4945` n `89` status `ready` deltaP `-0.2731` edge `1.4823` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.8261` n `47` status `ready` deltaP `32.8014` edge `0.124` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.2787` n `113` status `ready` deltaP `16.2392` edge `0.214` maxDD `-1.5895`
- `market_context_high->index_4h` score `3.0191` n `47` status `ready` deltaP `34.4837` edge `0.0371` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8575` n `113` status `ready` deltaP `19.0703` edge `0.1545` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.5421` n `110` status `ready` deltaP `17.1896` edge `0.3104` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.5035` n `47` status `ready` deltaP `17.4494` edge `0.1341` maxDD `-1.3444`
- `news_risk_high->crypto_alt_4h` score `2.4809` n `110` status `ready` deltaP `9.5953` edge `0.3879` maxDD `-15.9436`
- `news_risk_high->crypto_alt_24h` score `2.4317` n `89` status `ready` deltaP `-2.3038` edge `1.0284` maxDD `-49.7699`
- `news_risk_high->fx_4h` score `1.6501` n `110` status `ready` deltaP `23.9856` edge `0.0412` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.25` n `89` status `ready` deltaP `16.9378` edge `0.0844` maxDD `-1.7857`
- `news_risk_high->metal_1h` score `1.1747` n `113` status `ready` deltaP `17.1599` edge `0.0245` maxDD `-0.6142`
- `news_risk_high->metal_24h` score `1.0798` n `89` status `ready` deltaP `24.6254` edge `0.1191` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.0313` n `89` status `ready` deltaP `26.5547` edge `0.1183` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0122` n `47` status `ready` deltaP `15.2089` edge `0.0108` maxDD `-0.2275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

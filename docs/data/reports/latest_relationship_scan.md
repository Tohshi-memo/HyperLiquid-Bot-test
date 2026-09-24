# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T18:52:30.388698+00:00`
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

- `market_context_high->unknown_1h` score `87.1507` n `47` status `ready` deltaP `10.116` edge `7.2022` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.4581` n `47` status `ready` deltaP `30.4226` edge `3.5413` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.68` n `47` status `ready` deltaP `24.782` edge `2.3461` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.717` n `47` status `ready` deltaP `30.4226` edge `1.8925` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8298` n `47` status `ready` deltaP `34.7628` edge `0.4337` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8719` n `47` status `ready` deltaP `33.1487` edge `0.1255` maxDD `-0.2401`
- `news_risk_high->crypto_major_24h` score `3.8426` n `87` status `ready` deltaP `-1.1254` edge `1.4044` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `3.3823` n `111` status `ready` deltaP `16.6937` edge `0.2196` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9911` n `47` status `ready` deltaP `34.1788` edge `0.0368` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8243` n `111` status `ready` deltaP `18.6398` edge `0.1546` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.5613` n `108` status `ready` deltaP `9.31` edge `0.3965` maxDD `-15.9436`
- `news_risk_high->crypto_major_4h` score `2.545` n `108` status `ready` deltaP `16.8361` edge `0.313` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.4697` n `47` status `ready` deltaP `17.2969` edge `0.1323` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `1.8351` n `87` status `ready` deltaP `-2.9754` edge `0.9564` maxDD `-49.7699`
- `news_risk_high->fx_4h` score `1.7336` n `108` status `ready` deltaP `24.9097` edge `0.042` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.5068` n `87` status `ready` deltaP `18.3728` edge `0.0879` maxDD `-1.7857`
- `news_risk_high->metal_1h` score `1.351` n `111` status `ready` deltaP `18.0086` edge `0.0252` maxDD `-0.6142`
- `market_context_high->index_1h` score `1.0242` n `47` status `ready` deltaP `15.3586` edge `0.0108` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `1.0084` n `87` status `ready` deltaP `24.1978` edge `0.1128` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.9669` n `87` status `ready` deltaP `25.6764` edge `0.1159` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T09:07:27.494555+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1824.2851` n `126` status `ready` deltaP `-5.6796` edge `152.1046` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `97.7803` n `98` status `ready` deltaP `-6.0919` edge `8.2176` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `28.2728` n `126` status `ready` deltaP `1.9139` edge `2.3566` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.5615` n `30` status `ready` deltaP `49.2709` edge `1.2231` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.1984` n `126` status `ready` deltaP `22.8671` edge `0.8898` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.2071` n `98` status `ready` deltaP `18.7905` edge `0.4473` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.3529` n `126` status `ready` deltaP `40.8234` edge `0.1089` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9627` n `126` status `ready` deltaP `14.0006` edge `0.0159` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.9056` n `98` status `ready` deltaP `8.096` edge `0.1044` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.4963` n `126` status `ready` deltaP `6.6486` edge `0.0846` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.4922` n `126` status `ready` deltaP `10.1678` edge `0.076` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.4853` n `126` status `ready` deltaP `17.545` edge `0.0328` maxDD `-1.671`
- `market_context_high->commodity_4h` score `0.2277` n `126` status `ready` deltaP `12.9985` edge `0.0542` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.0147` n `126` status `ready` deltaP `2.1075` edge `0.1425` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0582` n `126` status `ready` deltaP `4.4031` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2803` n `126` status `ready` deltaP `1.9009` edge `0.0154` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.3158` n `126` status `ready` deltaP `6.7212` edge `0.1794` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4859` n `126` status `ready` deltaP `0.0315` edge `-0.0028` maxDD `-0.4433`
- `market_context_high->index_1h` score `-0.5192` n `126` status `ready` deltaP `1.6776` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7502` n `126` status `ready` deltaP `3.7877` edge `0.0561` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

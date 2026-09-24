# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T13:37:30.773576+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10068`

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

- `market_context_high->unknown_1h` score `98.9323` n `47` status `ready` deltaP `10.116` edge `8.184` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.949` n `47` status `ready` deltaP `29.5545` edge `3.338` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.9506` n `47` status `ready` deltaP `24.4348` edge `2.2043` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.7984` n `47` status `ready` deltaP `26.9503` edge `1.8391` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8209` n `47` status `ready` deltaP `34.9364` edge `0.4318` maxDD `-0.3705`
- `news_risk_high->crypto_alt_24h` score `7.6699` n `102` status `ready` deltaP `1.0723` edge `1.3333` maxDD `-49.7699`
- `news_risk_high->crypto_major_24h` score `6.7114` n `102` status `ready` deltaP `3.5846` edge `1.7408` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.5081` n `47` status `ready` deltaP `30.3709` edge `0.1137` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0736` n `47` status `ready` deltaP `34.941` edge `0.0386` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6769` n `47` status `ready` deltaP `17.9067` edge `0.1455` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4795` n `120` status `ready` deltaP `12.8344` edge `0.1701` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0823` n `120` status `ready` deltaP `15.0799` edge `0.1165` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7413` n `113` status `ready` deltaP `25.3062` edge `0.04` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.3482` n `102` status `ready` deltaP `30.7292` edge `0.1311` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.2689` n `102` status `ready` deltaP `17.2692` edge `0.1085` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0589` n `102` status `ready` deltaP `23.5499` edge `0.1236` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.9906` n `47` status `ready` deltaP `14.9095` edge `0.011` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9403` n `47` status `ready` deltaP `11.167` edge `0.0442` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.7942` n `113` status `ready` deltaP `13.0261` edge `0.1925` maxDD `-13.719`
- `market_context_high->crypto_alt_4h` score `0.5011` n `47` status `ready` deltaP `6.3343` edge `0.0663` maxDD `-3.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

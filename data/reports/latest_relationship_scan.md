# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T23:37:29.547131+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11662`

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

- `news_risk_high->unknown_24h` score `1399.2568` n `83` status `ready` deltaP `-0.8576` edge `116.6149` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.5138` n `47` status `ready` deltaP `8.3196` edge `5.9111` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.1166` n `47` status `ready` deltaP `29.0337` edge `4.0221` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.6048` n `47` status `ready` deltaP `24.782` edge `2.5065` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1568` n `47` status `ready` deltaP `32.6795` edge `1.9141` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6065` n `47` status `ready` deltaP `34.4156` edge `0.4174` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7831` n `47` status `ready` deltaP `31.9334` edge `0.1262` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5482` n `47` status `ready` deltaP `29.4532` edge `0.0314` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3821` n `47` status `ready` deltaP `11.2124` edge `0.1072` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0913` n `47` status `ready` deltaP `12.5143` edge `0.0478` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9152` n `112` status `ready` deltaP `9.6343` edge `0.1031` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8397` n `47` status `ready` deltaP `13.2628` edge `0.0094` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6942` n `83` status `ready` deltaP `23.7304` edge `0.0969` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5225` n `47` status `ready` deltaP `10.7083` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4082` n `47` status `ready` deltaP `4.6899` edge `0.0932` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.2044` n `47` status `ready` deltaP `4.3031` edge `0.0701` maxDD `-4.5405`
- `market_context_high->fx_4h` score `0.0469` n `47` status `ready` deltaP `9.4739` edge `0.0075` maxDD `-0.6736`
- `news_risk_high->equity_1h` score `0.0239` n `112` status `ready` deltaP `2.8069` edge `0.0351` maxDD `-2.0595`
- `market_context_high->metal_1h` score `0.0126` n `47` status `ready` deltaP `3.4272` edge `0.0104` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

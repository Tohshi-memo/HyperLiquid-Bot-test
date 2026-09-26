# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T01:37:26.621275+00:00`
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

- `news_risk_high->unknown_24h` score `2128.0331` n `88` status `ready` deltaP `-0.7892` edge `177.3458` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `71.4706` n `47` status `ready` deltaP `8.3196` edge `5.9075` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.8129` n `47` status `ready` deltaP `27.8184` edge `4.0049` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.3444` n `47` status `ready` deltaP `24.782` edge `2.4848` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1772` n `47` status `ready` deltaP `32.6795` edge `1.9158` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.5463` n `47` status `ready` deltaP `34.0684` edge `0.4147` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7023` n `47` status `ready` deltaP `31.2389` edge `0.1241` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7205` n `47` status `ready` deltaP `17.2969` edge `0.1532` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5262` n `47` status `ready` deltaP `29.1483` edge `0.0316` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.2845` n `47` status `ready` deltaP `10.9075` edge `0.1011` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1344` n `47` status `ready` deltaP `12.9634` edge `0.0484` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8445` n `47` status `ready` deltaP `13.2628` edge `0.0098` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.8397` n `88` status `ready` deltaP `24.9526` edge `0.1074` maxDD `-6.9545`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.367` n `47` status `ready` deltaP `4.385` edge `0.0918` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3171` n `47` status `ready` deltaP `5.0516` edge `0.0745` maxDD `-4.5405`
- `news_risk_high->crypto_alt_1h` score `0.2647` n `117` status `ready` deltaP `7.8152` edge `0.0729` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0591` n `47` status `ready` deltaP `9.6264` edge `0.0075` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`
- `news_risk_high->equity_4h` score `0.013` n `108` status `ready` deltaP `14.7753` edge `0.0641` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

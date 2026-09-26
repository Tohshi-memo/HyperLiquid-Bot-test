# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T05:07:28.707033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11768`

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

- `news_risk_high->unknown_24h` score `3236.1267` n `96` status `ready` deltaP `-0.6945` edge `269.6863` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.3642` n `47` status `ready` deltaP `8.1698` edge `5.8163` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.7941` n `47` status `ready` deltaP `25.3878` edge `3.9362` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.1927` n `47` status `ready` deltaP `23.0459` edge `2.4004` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2927` n `47` status `ready` deltaP `33.3739` edge `1.9208` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.3606` n `47` status `ready` deltaP `32.3323` edge `0.4108` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5197` n `47` status `ready` deltaP `29.6764` edge `0.1193` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7021` n `47` status `ready` deltaP `16.992` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.503` n `47` status `ready` deltaP `28.8434` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1391` n `47` status `ready` deltaP `10.755` edge `0.09` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1182` n `96` status `ready` deltaP `27.0833` edge `0.1289` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7571` n `47` status `ready` deltaP `12.2149` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4152` n `96` status `ready` deltaP `13.7153` edge `0.0433` maxDD `-2.344`
- `market_context_high->crypto_major_4h` score `0.3442` n `47` status `ready` deltaP `4.385` edge `0.0899` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3386` n `47` status `ready` deltaP `5.2013` edge `0.0753` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.2025` n `125` status `ready` deltaP `6.2575` edge `0.0044` maxDD `-0.3395`
- `market_context_high->metal_1h` score `0.0281` n `47` status `ready` deltaP `3.7266` edge `0.0104` maxDD `-0.1976`
- `market_context_high->fx_4h` score `0.0103` n `47` status `ready` deltaP `9.0166` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

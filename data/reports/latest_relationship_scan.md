# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T05:37:29.319311+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11848`

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

- `news_risk_high->unknown_24h` score `3305.4836` n `98` status `ready` deltaP `-0.6732` edge `275.4659` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8614` n `47` status `ready` deltaP `8.1698` edge `5.7744` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.6427` n `47` status `ready` deltaP `25.0406` edge `3.9259` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.0137` n `47` status `ready` deltaP `22.6987` edge `2.3878` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3011` n `47` status `ready` deltaP `33.3739` edge `1.9215` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.3268` n `47` status `ready` deltaP `31.9851` edge `0.4103` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4811` n `47` status `ready` deltaP `29.3292` edge `0.1184` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.6741` n `47` status `ready` deltaP `16.6872` edge `0.1534` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.4908` n `47` status `ready` deltaP `28.691` edge `0.0317` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.1851` n `47` status `ready` deltaP `11.0599` edge `0.0918` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1573` n `98` status `ready` deltaP `27.3101` edge `0.1324` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0362` n `47` status `ready` deltaP `11.9155` edge `0.0472` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7439` n `47` status `ready` deltaP `12.0652` edge `0.0094` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5213` n `47` status `ready` deltaP `10.7083` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4175` n `98` status `ready` deltaP `13.8783` edge `0.0424` maxDD `-2.344`
- `market_context_high->crypto_major_4h` score `0.3732` n `47` status `ready` deltaP `4.5375` edge `0.0913` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3338` n `47` status `ready` deltaP `5.2013` edge `0.0749` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1755` n `127` status `ready` deltaP `5.9503` edge `0.0042` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0237` n `47` status `ready` deltaP `9.1691` edge `0.0076` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.0118` n `47` status `ready` deltaP `3.4272` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

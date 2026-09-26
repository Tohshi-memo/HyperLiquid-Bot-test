# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T09:07:32.922073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11858`

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

- `news_risk_high->unknown_24h` score `3529.1792` n `98` status `ready` deltaP `-0.6732` edge `294.1072` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9105` n `47` status `ready` deltaP `8.619` edge `5.7755` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.6954` n `47` status `ready` deltaP `22.7837` edge `3.862` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.8422` n `47` status `ready` deltaP `20.789` edge `2.3029` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4439` n `47` status `ready` deltaP `33.3739` edge `1.9334` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1338` n `47` status `ready` deltaP `29.9017` edge `0.4081` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3939` n `47` status `ready` deltaP `28.8084` edge `0.1146` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7119` n `47` status `ready` deltaP `17.1445` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5554` n `47` status `ready` deltaP `29.4532` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4209` n `47` status `ready` deltaP `11.5172` edge `0.1084` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1614` n `98` status `ready` deltaP `26.7893` edge `0.1364` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0254` n `47` status `ready` deltaP `11.7658` edge `0.0473` maxDD `-1.5564`
- `news_risk_high->index_24h` score `0.8306` n `98` status `ready` deltaP `15.8765` edge `0.0454` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6514` n `47` status `ready` deltaP `6.2143` edge `0.1033` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5464` n `47` status `ready` deltaP `11.0077` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3171` n `47` status `ready` deltaP `5.0516` edge `0.0745` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.0905` n `137` status `ready` deltaP `4.9511` edge `0.0037` maxDD `-0.3331`
- `market_context_high->fx_4h` score `0.0359` n `47` status `ready` deltaP `9.3215` edge `0.0076` maxDD `-0.6736`
- `news_risk_high->crypto_alt_1h` score `0.0251` n `137` status `ready` deltaP `5.6067` edge `0.0569` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

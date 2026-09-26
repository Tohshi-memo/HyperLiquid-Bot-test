# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T10:37:30.012439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11882`

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

- `news_risk_high->unknown_24h` score `3943.085` n `92` status `ready` deltaP `-0.7398` edge `328.5998` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8133` n `47` status `ready` deltaP `8.4693` edge `5.7684` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.4516` n `47` status `ready` deltaP `22.4364` edge `3.844` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.2848` n `47` status `ready` deltaP `19.7473` edge `2.2634` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5267` n `47` status `ready` deltaP `33.3739` edge `1.9403` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0849` n `47` status `ready` deltaP `29.3809` edge `0.4075` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4252` n `47` status `ready` deltaP `29.1556` edge `0.1149` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5932` n `47` status `ready` deltaP `29.9105` edge `0.0321` maxDD `-0.2323`
- `news_risk_high->index_24h` score `1.6398` n `92` status `ready` deltaP `20.5465` edge `0.0567` maxDD `-2.2287`
- `market_context_high->crypto_alt_4h` score `1.4245` n `47` status `ready` deltaP `11.5172` edge `0.1087` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1641` n `92` status `ready` deltaP `26.4266` edge `0.1391` maxDD `-6.9489`
- `market_context_high->equity_1h` score `1.0386` n `47` status `ready` deltaP `11.9155` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7697` n `47` status `ready` deltaP `6.8241` edge `0.1091` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5332` n `47` status `ready` deltaP `10.858` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3818` n `47` status `ready` deltaP `5.5007` edge `0.0769` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1407` n `137` status `ready` deltaP `5.5313` edge `0.004` maxDD `-0.3322`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`
- `market_context_high->fx_4h` score `-0.0433` n `47` status `ready` deltaP `8.4069` edge `0.0071` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

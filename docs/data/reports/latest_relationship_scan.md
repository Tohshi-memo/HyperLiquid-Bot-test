# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T10:22:30.798560+00:00`
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

- `news_risk_high->unknown_24h` score `3869.0484` n `93` status `ready` deltaP `-0.7281` edge `322.43` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8277` n `47` status `ready` deltaP `8.4693` edge `5.7696` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.4912` n `47` status `ready` deltaP `22.4364` edge `3.8473` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.3947` n `47` status `ready` deltaP `19.9209` edge `2.2714` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5147` n `47` status `ready` deltaP `33.3739` edge `1.9393` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1` n `47` status `ready` deltaP `29.5545` edge `0.4076` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.424` n `47` status `ready` deltaP `29.1556` edge `0.1148` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5798` n `47` status `ready` deltaP `29.758` edge `0.032` maxDD `-0.2323`
- `news_risk_high->index_24h` score `1.5092` n `93` status `ready` deltaP `19.8085` edge `0.0549` maxDD `-2.2287`
- `market_context_high->crypto_alt_4h` score `1.4293` n `47` status `ready` deltaP `11.5172` edge `0.1091` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1172` n `93` status `ready` deltaP `25.6552` edge `0.1383` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0398` n `47` status `ready` deltaP `11.9155` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7637` n `47` status `ready` deltaP `6.8241` edge `0.1086` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5452` n `47` status `ready` deltaP `11.0077` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3854` n `47` status `ready` deltaP `5.5007` edge `0.0772` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1395` n `137` status `ready` deltaP `5.5313` edge `0.0039` maxDD `-0.3322`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`
- `market_context_high->fx_4h` score `-0.0299` n `47` status `ready` deltaP `8.5593` edge `0.0072` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

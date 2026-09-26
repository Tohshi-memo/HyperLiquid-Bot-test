# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T07:07:32.499093+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11840`

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

- `news_risk_high->unknown_24h` score `3383.638` n `102` status `ready` deltaP `-0.6332` edge `281.9785` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8373` n `47` status `ready` deltaP `8.7687` edge `5.7684` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.2246` n `47` status `ready` deltaP `23.9989` edge `3.898` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.5749` n `47` status `ready` deltaP `22.1779` edge `2.3547` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3599` n `47` status `ready` deltaP `33.3739` edge `1.9264` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.2327` n `47` status `ready` deltaP `30.9434` edge `0.4094` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4293` n `47` status `ready` deltaP `28.982` edge `0.1164` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7277` n `47` status `ready` deltaP `17.2969` edge `0.1538` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5176` n `47` status `ready` deltaP `28.9958` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3477` n `47` status `ready` deltaP `11.5172` edge `0.1023` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2266` n `102` status `ready` deltaP `28.0433` edge `0.1364` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7583` n `47` status `ready` deltaP `12.2149` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5452` n `47` status `ready` deltaP `11.0077` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4988` n `47` status `ready` deltaP `5.1472` edge `0.0977` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.3738` n `102` status `ready` deltaP `13.797` edge `0.0393` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3338` n `47` status `ready` deltaP `5.2013` edge `0.0749` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1496` n `133` status `ready` deltaP `5.656` edge `0.004` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0615` n `47` status `ready` deltaP `9.6264` edge `0.0077` maxDD `-0.6736`
- `market_context_high->metal_1h` score `-0.0038` n `47` status `ready` deltaP `3.1278` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

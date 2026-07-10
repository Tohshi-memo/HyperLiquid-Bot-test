# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T07:37:27.334039+00:00`
- Price records: `672`
- Market context records: `6262`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11096`

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

- `news_risk_high->crypto_alt_24h` score `14.737` n `32` status `ready` deltaP `42.6351` edge `0.9586` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.971` n `32` status `ready` deltaP `50.7719` edge `0.1591` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1817` n `32` status `ready` deltaP `43.8262` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.6946` n `32` status `ready` deltaP `16.0538` edge `0.4446` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4704` n `32` status `ready` deltaP `26.056` edge `0.0527` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.1437` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2158` n `193` status `ready` deltaP `2.3192` edge `0.27` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.3855` n `192` status `ready` deltaP `-1.2322` edge `0.3769` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3501` n `32` status `ready` deltaP `13.9783` edge `0.1266` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7888` n `32` status `ready` deltaP `10.5726` edge `0.0768` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1589` n `32` status `ready` deltaP `9.2517` edge `0.0051` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.2445` n `192` status `ready` deltaP `4.1921` edge `0.0434` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2785` n `193` status `ready` deltaP `1.3302` edge `0.0` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3037` n `192` status `ready` deltaP `17.8969` edge `0.0986` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5246` n `192` status `ready` deltaP `3.8237` edge `0.026` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5443` n `193` status `ready` deltaP `-0.5585` edge `0.003` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7037` n `32` status `ready` deltaP `-2.3952` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7659` n `193` status `ready` deltaP `2.5271` edge `-0.0008` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8624` n `193` status `ready` deltaP `5.0836` edge `0.0308` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-0.9648` n `193` status `ready` deltaP `-1.9407` edge `0.0008` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T17:37:22.708804+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8174`

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

- `market_context_high->unknown_24h` score `1381.152` n `40` status `ready` deltaP `-20.6597` edge `115.2701` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `55.7444` n `79` status `ready` deltaP `-6.7324` edge `4.7483` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `10.5636` n `91` status `ready` deltaP `-2.8163` edge `0.9327` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8068` n `40` status `ready` deltaP `27.6736` edge `0.5923` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3868` n `40` status `ready` deltaP `52.4306` edge `0.1827` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3168` n `40` status `ready` deltaP `37.4653` edge `0.0396` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6273` n `40` status `ready` deltaP `-20.5903` edge `0.5877` maxDD `-17.8526`
- `market_context_high->crypto_alt_1h` score `0.7775` n `91` status `ready` deltaP `7.847` edge `0.1159` maxDD `-4.9401`
- `market_context_high->fx_4h` score `0.7569` n `79` status `ready` deltaP `12.5154` edge `0.008` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.3504` n `79` status `ready` deltaP `10.58` edge `0.012` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.0441` n `91` status `ready` deltaP `2.3492` edge `0.0769` maxDD `-3.7778`
- `market_context_high->fx_1h` score `-0.0868` n `91` status `ready` deltaP `2.3525` edge `0.0013` maxDD `-0.271`
- `market_context_high->commodity_1h` score `-0.1106` n `91` status `ready` deltaP `2.1518` edge `0.0048` maxDD `-0.6025`
- `market_context_high->metal_1h` score `-0.1209` n `91` status `ready` deltaP `6.6461` edge `0.0045` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.3265` n `79` status `ready` deltaP `3.7145` edge `0.0203` maxDD `-1.1153`
- `market_context_high->index_1h` score `-0.6005` n `91` status `ready` deltaP `-1.5463` edge `-0.0016` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.8317` n `79` status `ready` deltaP `-5.9085` edge `0.0028` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-0.853` n `79` status `ready` deltaP `-2.3425` edge `0.1551` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-0.9272` n `91` status `ready` deltaP `-5.2378` edge `0.003` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.4246` n `79` status `ready` deltaP `-5.8158` edge `0.1759` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

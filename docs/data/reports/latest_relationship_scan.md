# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T16:22:25.607359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7332`

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

- `market_context_high->unknown_24h` score `1381.3955` n `40` status `ready` deltaP `-19.7917` edge `115.2846` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `52.2895` n `77` status `ready` deltaP `-7.1389` edge `4.4631` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.0934` n `86` status `ready` deltaP `-4.0941` edge `1.0687` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8435` n `40` status `ready` deltaP `27.8472` edge `0.5942` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3995` n `40` status `ready` deltaP `52.6042` edge `0.1826` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3995` n `40` status `ready` deltaP `38.3333` edge `0.0407` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6681` n `40` status `ready` deltaP `-20.5903` edge `0.5911` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7692` n `77` status `ready` deltaP `12.6545` edge `0.0081` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.5065` n `86` status `ready` deltaP `6.1238` edge `0.1048` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.464` n `77` status `ready` deltaP `11.7458` edge `0.0137` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.0558` n `86` status `ready` deltaP `4.0976` edge `0.0057` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.1253` n `86` status `ready` deltaP `1.8869` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.1971` n `86` status `ready` deltaP `0.8286` edge `0.0581` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.2538` n `77` status `ready` deltaP `3.0211` edge `0.0196` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.2933` n `86` status `ready` deltaP `4.7312` edge `0.0029` maxDD `-0.7107`
- `market_context_high->index_1h` score `-0.7188` n `86` status `ready` deltaP `-3.6729` edge `-0.0026` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.8717` n `77` status `ready` deltaP `-6.5272` edge `0.0018` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-0.8785` n `77` status `ready` deltaP `-3.7892` edge `0.1232` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.1078` n `86` status `ready` deltaP `-7.7496` edge `-0.0034` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.9474` n `77` status `ready` deltaP `-7.131` edge `0.1411` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

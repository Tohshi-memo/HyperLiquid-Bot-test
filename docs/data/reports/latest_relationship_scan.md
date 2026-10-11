# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T18:07:28.776655+00:00`
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

- `market_context_high->unknown_24h` score `1381.1022` n `40` status `ready` deltaP `-20.8333` edge `115.2671` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `59.7265` n `81` status `ready` deltaP `-6.2011` edge `5.0766` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `9.9618` n `93` status `ready` deltaP `-2.3437` edge `0.8794` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.7984` n `40` status `ready` deltaP `27.6736` edge `0.5916` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3868` n `40` status `ready` deltaP `52.4306` edge `0.1827` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2842` n `40` status `ready` deltaP `37.1181` edge `0.0392` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.5889` n `40` status `ready` deltaP `-20.5903` edge `0.5845` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7987` n `81` status `ready` deltaP `13.0232` edge `0.0081` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.7174` n `93` status `ready` deltaP `7.4255` edge `0.1137` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.2205` n `81` status `ready` deltaP `9.1972` edge `0.0104` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.029` n `93` status `ready` deltaP `2.2664` edge `0.0762` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0638` n `93` status `ready` deltaP `2.7976` edge `0.0044` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.1003` n `93` status `ready` deltaP `2.1988` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1514` n `93` status `ready` deltaP `6.2955` edge `0.0043` maxDD `-0.7107`
- `market_context_high->crypto_major_4h` score `-0.2294` n `81` status `ready` deltaP `-0.9673` edge `0.1876` maxDD `-11.1784`
- `market_context_high->metal_4h` score `-0.244` n `81` status `ready` deltaP `4.656` edge `0.0209` maxDD `-1.1153`
- `market_context_high->crypto_alt_4h` score `-0.5513` n `81` status `ready` deltaP `-4.5656` edge `0.2156` maxDD `-13.8008`
- `market_context_high->index_1h` score `-0.6562` n `93` status `ready` deltaP `-2.6334` edge `-0.0015` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.7643` n `81` status `ready` deltaP `-4.7482` edge `0.0037` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-0.8879` n `93` status `ready` deltaP `-4.4974` edge `0.0031` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

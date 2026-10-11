# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T15:22:31.151844+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7312`

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

- `market_context_high->unknown_24h` score `1381.5169` n `40` status `ready` deltaP `-19.4444` edge `115.2924` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `54.6159` n `73` status `ready` deltaP `-8.0438` edge `4.663` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.9231` n `82` status `ready` deltaP `-5.2285` edge `1.1454` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8833` n `40` status `ready` deltaP `28.1944` edge `0.5952` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4297` n `40` status `ready` deltaP `52.9514` edge `0.1828` maxDD `0.0`
- `market_context_high->fx_24h` score `3.461` n `40` status `ready` deltaP `39.0278` edge `0.0412` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6254` n `40` status `ready` deltaP `-20.7639` edge `0.5887` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.0418` n `73` status `ready` deltaP `15.8975` edge `0.0092` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.7317` n `73` status `ready` deltaP `14.371` edge `0.0185` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.0054` n `82` status `ready` deltaP `4.4947` edge `0.073` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `-0.0848` n `82` status `ready` deltaP `2.6545` edge `0.0036` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0969` n `82` status `ready` deltaP `2.2273` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.3477` n `73` status `ready` deltaP `1.1402` edge `0.0201` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.3541` n `82` status `ready` deltaP `4.0018` edge `0.0027` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.5216` n `82` status `ready` deltaP `-0.8982` edge `0.028` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.0032` n `73` status `ready` deltaP `-8.9062` edge `0.0008` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-1.2726` n `82` status `ready` deltaP `-10.0956` edge `-0.0089` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.2958` n `82` status `ready` deltaP `-5.9259` edge `-0.0034` maxDD `-0.5392`
- `market_context_high->crypto_major_4h` score `-1.4289` n `73` status `ready` deltaP `-6.9203` edge `0.0735` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.0491` n `73` status `ready` deltaP `-9.5201` edge `0.0566` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T20:37:24.879585+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `0.9573` n `145` status `ready` deltaP `20.4064` edge `0.0245` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9344` n `179` status `ready` deltaP `12.5137` edge `0.0659` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6554` n `187` status `ready` deltaP `9.0173` edge `0.0288` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.1686` n `145` status `ready` deltaP `1.8909` edge `0.3565` maxDD `-21.0709`
- `market_context_high->fx_1h` score `-0.1102` n `187` status `ready` deltaP `4.6103` edge `0.0003` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1354` n `179` status `ready` deltaP `6.2687` edge `0.0069` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.5013` n `145` status `ready` deltaP `1.7355` edge `0.0998` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6029` n `187` status `ready` deltaP `-3.9883` edge `-0.0028` maxDD `-0.832`
- `market_context_high->metal_24h` score `-0.7278` n `145` status `ready` deltaP `2.5482` edge `0.0548` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.8462` n `179` status `ready` deltaP `-2.9747` edge `-0.0096` maxDD `-1.3245`
- `market_context_high->equity_1h` score `-1.0433` n `187` status `ready` deltaP `-3.4951` edge `-0.0068` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2048` n `187` status `ready` deltaP `-4.2444` edge `-0.0085` maxDD `-2.0884`
- `market_context_high->crypto_major_24h` score `-2.5277` n `145` status `ready` deltaP `-1.3662` edge `-0.0573` maxDD `-14.9459`
- `market_context_high->crypto_alt_1h` score `-2.6831` n `187` status `ready` deltaP `-9.4423` edge `-0.0409` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-2.9995` n `179` status `ready` deltaP `-6.026` edge `-0.0334` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.4227` n `179` status `ready` deltaP `-11.9643` edge `-0.0955` maxDD `-12.0832`
- `market_context_high->crypto_major_1h` score `-3.6362` n `187` status `ready` deltaP `-9.3151` edge `-0.0505` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-5.2932` n `145` status `ready` deltaP `-12.8226` edge `-0.1588` maxDD `-9.0785`
- `market_context_high->crypto_alt_4h` score `-6.0412` n `179` status `ready` deltaP `-11.7106` edge `-0.1318` maxDD `-16.8181`
- `market_context_high->commodity_24h` score `-8.1227` n `145` status `ready` deltaP `-4.0997` edge `-0.1578` maxDD `-51.4992`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

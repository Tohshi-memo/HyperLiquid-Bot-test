# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T11:22:25.681167+00:00`
- Price records: `672`
- Market context records: `6812`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8281` n `176` status `ready` deltaP `-1.5467` edge `0.4917` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.4103` n `176` status `ready` deltaP `10.9217` edge `0.1482` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.4064` n `193` status `ready` deltaP `5.6126` edge `0.0147` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4432` n `193` status `ready` deltaP `-1.203` edge `-0.0003` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5193` n `193` status `ready` deltaP `2.8723` edge `0.014` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6529` n `193` status `ready` deltaP `-1.3186` edge `-0.0066` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7636` n `193` status `ready` deltaP `-3.3795` edge `-0.0023` maxDD `-0.8451`
- `market_context_high->metal_1h` score `-0.9594` n `193` status `ready` deltaP `-6.8909` edge `-0.0077` maxDD `-1.8824`
- `market_context_high->fx_4h` score `-1.3476` n `185` status `ready` deltaP `5.3699` edge `-0.0022` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3617` n `185` status `ready` deltaP `-2.2932` edge `-0.0103` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.5157` n `193` status `ready` deltaP `0.8113` edge `-0.0228` maxDD `-4.3798`
- `market_context_high->index_4h` score `-1.6601` n `185` status `ready` deltaP `1.8375` edge `-0.0291` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.8233` n `193` status `ready` deltaP `-7.0406` edge `-0.0149` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.857` n `185` status `ready` deltaP `-6.0094` edge `-0.0279` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.3153` n `185` status `ready` deltaP `-0.9625` edge `-0.0859` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.5013` n `185` status `ready` deltaP `-14.1175` edge `0.0389` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5231` n `185` status `ready` deltaP `-1.6694` edge `-0.0822` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.4804` n `176` status `ready` deltaP `-9.7853` edge `-0.0045` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0509` n `185` status `ready` deltaP `-0.81` edge `-0.1883` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6195` n `176` status `ready` deltaP `-21.6225` edge `-0.2406` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T23:37:28.959496+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `7.9367` n `81` status `ready` deltaP `6.4622` edge `0.9243` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.9774` n `81` status `ready` deltaP `13.6574` edge `0.298` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7256` n `81` status `ready` deltaP `33.6034` edge `0.0672` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.5986` n `81` status `ready` deltaP `11.0146` edge `0.2111` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.5375` n `103` status `ready` deltaP `15.9631` edge `0.089` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1099` n `103` status `ready` deltaP `13.3335` edge `0.0379` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.1416` n `103` status `ready` deltaP `6.2933` edge `0.0291` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4687` n `103` status `ready` deltaP `-2.885` edge `-0.0061` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.507` n `103` status `ready` deltaP `1.9054` edge `-0.0054` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5774` n `103` status `ready` deltaP `-0.6616` edge `-0.0091` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5813` n `103` status `ready` deltaP `-2.962` edge `-0.0052` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7873` n `103` status `ready` deltaP `1.9373` edge `-0.0032` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9079` n `103` status `ready` deltaP `-0.7814` edge `-0.0103` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.4701` n `103` status `ready` deltaP `5.0275` edge `-0.0223` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.5959` n `103` status `ready` deltaP `-7.5853` edge `-0.0195` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.7886` n `81` status `ready` deltaP `11.2076` edge `-0.0546` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.0982` n `103` status `ready` deltaP `-4.8907` edge `-0.0426` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5325` n `81` status `ready` deltaP `-21.4313` edge `-0.1657` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.6901` n `103` status `ready` deltaP `-7.6827` edge `-0.0911` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0811` n `103` status `ready` deltaP `-8.9184` edge `-0.1915` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

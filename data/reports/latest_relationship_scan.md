# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T00:22:34.098481+00:00`
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

- `market_context_high->equity_24h` score `7.7043` n `81` status `ready` deltaP `5.9413` edge `0.9084` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.901` n `81` status `ready` deltaP `13.1366` edge `0.2951` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7256` n `81` status `ready` deltaP `33.6034` edge `0.0672` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.6101` n `103` status `ready` deltaP `16.4205` edge `0.092` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.5414` n `81` status `ready` deltaP `10.4938` edge `0.2098` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1111` n `103` status `ready` deltaP `13.3335` edge `0.038` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.1764` n `103` status `ready` deltaP `5.9939` edge `0.0282` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4602` n `103` status `ready` deltaP `-2.7353` edge `-0.006` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4686` n `103` status `ready` deltaP `2.3545` edge `-0.0052` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.5735` n `103` status `ready` deltaP `-2.8123` edge `-0.0052` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.59` n `103` status `ready` deltaP `-0.814` edge `-0.0097` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8287` n `103` status `ready` deltaP `1.4799` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9371` n `103` status `ready` deltaP `-1.2387` edge `-0.011` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.5751` n `103` status `ready` deltaP `4.5702` edge `-0.028` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.6378` n `103` status `ready` deltaP `-7.8847` edge `-0.021` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.8393` n `81` status `ready` deltaP `11.2076` edge `-0.0611` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1377` n `103` status `ready` deltaP `-5.1901` edge `-0.0439` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.545` n `81` status `ready` deltaP `-21.4313` edge `-0.1673` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7069` n `103` status `ready` deltaP `-7.6827` edge `-0.0925` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1027` n `103` status `ready` deltaP `-8.9184` edge `-0.1933` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

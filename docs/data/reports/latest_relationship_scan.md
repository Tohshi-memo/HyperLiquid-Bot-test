# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T15:22:28.464176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.7055` n `97` status `ready` deltaP `3.4919` edge `0.5915` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.535` n `97` status `ready` deltaP `10.9572` edge `0.1958` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4666` n `103` status `ready` deltaP `13.9814` edge `0.0963` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.1658` n `97` status `ready` deltaP `26.7325` edge `0.0579` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0082` n `103` status `ready` deltaP `11.6868` edge `0.0404` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3995` n `97` status `ready` deltaP `7.4187` edge `0.1549` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4652` n `103` status `ready` deltaP `3.449` edge `0.0211` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4866` n `103` status `ready` deltaP `2.2048` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5123` n `103` status `ready` deltaP `-3.6335` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6287` n `103` status `ready` deltaP `-1.4238` edge `-0.0106` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8759` n `103` status `ready` deltaP `1.1751` edge `-0.0055` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0391` n `103` status `ready` deltaP `-2.9156` edge `-0.0129` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9439` n `103` status `ready` deltaP `2.4361` edge `-0.0445` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.0033` n `103` status `ready` deltaP `-11.3278` edge `-0.0285` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.4932` n `97` status `ready` deltaP `5.1725` edge `-0.1047` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.5428` n `103` status `ready` deltaP `-8.4835` edge `-0.0557` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-2.9203` n `97` status `ready` deltaP `-14.8482` edge `-0.1311` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2496` n `103` status `ready` deltaP `-11.6461` edge `-0.1113` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9391` n `103` status `ready` deltaP `-14.5587` edge `-0.2254` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T09:07:30.607497+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_4h` score `34.1502` n `117` status `ready` deltaP `-2.5524` edge `2.9275` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `11.9733` n `50` status `ready` deltaP `24.5903` edge `1.5922` maxDD `-11.6881`
- `market_context_high->crypto_alt_24h` score `10.3026` n `50` status `ready` deltaP `12.9583` edge `1.525` maxDD `-17.243`
- `risk_on_high->crypto_alt_4h` score `3.758` n `49` status `ready` deltaP `18.5914` edge `0.234` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.758` n `49` status `ready` deltaP `18.5914` edge `0.234` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4302` n `49` status `ready` deltaP `32.9455` edge `0.3054` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4302` n `49` status `ready` deltaP `32.9455` edge `0.3054` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.9122` n `50` status `ready` deltaP `7.2986` edge `0.465` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.9372` n `50` status `ready` deltaP `27.5556` edge `0.1207` maxDD `-0.4833`
- `market_context_high->unknown_1h` score `1.1455` n `117` status `ready` deltaP `-5.5811` edge `0.1663` maxDD `-1.024`
- `risk_on_high->crypto_alt_1h` score `0.9489` n `49` status `ready` deltaP `6.04` edge `0.0985` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9489` n `49` status `ready` deltaP `6.04` edge `0.0985` maxDD `-2.4421`
- `market_context_high->crypto_alt_1h` score `0.8482` n `117` status `ready` deltaP `7.5401` edge `0.1155` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.7202` n `117` status `ready` deltaP `10.6187` edge `0.2321` maxDD `-11.1784`
- `risk_on_high->crypto_major_1h` score `0.4019` n `49` status `ready` deltaP `5.102` edge `0.0828` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4019` n `49` status `ready` deltaP `5.102` edge `0.0828` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.2085` n `117` status `ready` deltaP `2.9915` edge `0.0831` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.0332` n `117` status `ready` deltaP `4.0964` edge `0.2313` maxDD `-13.8008`
- `market_context_high->metal_24h` score `-0.0778` n `50` status `ready` deltaP `8.0972` edge `0.0392` maxDD `-2.5853`
- `market_context_high->metal_1h` score `-0.1276` n `117` status `ready` deltaP `5.9177` edge `0.006` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T09:37:36.076698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8110`

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

- `market_context_high->unknown_4h` score `32.3168` n `115` status `ready` deltaP `-2.8646` edge `2.7768` maxDD `-1.8373`
- `market_context_high->crypto_alt_24h` score `17.6654` n `48` status `ready` deltaP `15.2778` edge `1.6201` maxDD `-14.6536`
- `market_context_high->crypto_major_24h` score `12.7666` n `48` status `ready` deltaP `26.9098` edge `1.6487` maxDD `-9.9747`
- `risk_on_high->crypto_alt_4h` score `3.744` n `48` status `ready` deltaP `18.1911` edge `0.2355` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.744` n `48` status `ready` deltaP `18.1911` edge `0.2355` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4285` n `48` status `ready` deltaP `32.6728` edge `0.307` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4285` n `48` status `ready` deltaP `32.6728` edge `0.307` maxDD `-4.1548`
- `market_context_high->equity_24h` score `2.8103` n `48` status `ready` deltaP `5.7291` edge `0.4624` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.8767` n `48` status `ready` deltaP `26.7361` edge `0.1184` maxDD `-0.4833`
- `market_context_high->unknown_1h` score `1.5454` n `115` status `ready` deltaP `-5.3072` edge `0.1978` maxDD `-1.024`
- `market_context_high->crypto_major_4h` score `1.2113` n `115` status `ready` deltaP `10.8974` edge `0.2359` maxDD `-10.9422`
- `risk_on_high->crypto_alt_1h` score `0.7908` n `48` status `ready` deltaP `5.489` edge `0.089` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.7908` n `48` status `ready` deltaP `5.489` edge `0.089` maxDD `-2.4421`
- `market_context_high->crypto_alt_1h` score `0.7706` n `115` status `ready` deltaP `7.1557` edge `0.1116` maxDD `-4.9401`
- `risk_on_high->crypto_major_1h` score `0.322` n `48` status `ready` deltaP `4.4661` edge `0.0768` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.322` n `48` status `ready` deltaP `4.4661` edge `0.0768` maxDD `-3.2233`
- `market_context_high->crypto_alt_4h` score `0.2485` n `115` status `ready` deltaP `4.4048` edge `0.2383` maxDD `-13.4229`
- `market_context_high->metal_24h` score `0.194` n `48` status `ready` deltaP `10.4167` edge `0.0465` maxDD `-2.2855`
- `market_context_high->crypto_major_1h` score `0.1566` n `115` status `ready` deltaP `2.4733` edge `0.0799` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.1943` n `115` status `ready` deltaP `5.3241` edge `0.0044` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

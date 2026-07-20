# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T04:52:27.218487+00:00`
- Price records: `672`
- Market context records: `7321`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_4h` score `7.1817` n `32` status `ready` deltaP `39.3352` edge `0.3555` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1817` n `32` status `ready` deltaP `39.3352` edge `0.3555` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.8327` n `32` status `ready` deltaP `32.298` edge `0.2951` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.8327` n `32` status `ready` deltaP `32.298` edge `0.2951` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.2955` n `32` status `ready` deltaP `18.0102` edge `0.3642` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.2955` n `32` status `ready` deltaP `18.0102` edge `0.3642` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2519` n `32` status `ready` deltaP `19.9289` edge `0.0521` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2519` n `32` status `ready` deltaP `19.9289` edge `0.0521` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2007` n `32` status `ready` deltaP `3.8476` edge `0.019` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2007` n `32` status `ready` deltaP `3.8476` edge `0.019` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1733` n `32` status `ready` deltaP `3.7538` edge `0.0349` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1733` n `32` status `ready` deltaP `3.7538` edge `0.0349` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1134` n `32` status `ready` deltaP `0.2994` edge `0.0496` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1134` n `32` status `ready` deltaP `0.2994` edge `0.0496` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0784` n `32` status `ready` deltaP `0.0474` edge `0.0755` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0784` n `32` status `ready` deltaP `0.0474` edge `0.0755` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1762` n `129` status `ready` deltaP `3.9389` edge `0.0001` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.6008` n `129` status `ready` deltaP `5.9462` edge `0.1192` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7456` n `129` status `ready` deltaP `-3.5652` edge `-0.0146` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7734` n `129` status `ready` deltaP `-4.7105` edge `-0.0069` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

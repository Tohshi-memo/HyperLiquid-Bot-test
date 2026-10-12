# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T19:24:53.383035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `6.4653` n `63` status `ready` deltaP `24.2808` edge `1.1733` maxDD `-33.8367`
- `risk_on_high->crypto_alt_4h` score `4.5968` n `48` status `ready` deltaP `19.7155` edge `0.2964` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.5968` n `48` status `ready` deltaP `19.7155` edge `0.2964` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `3.8949` n `100` status `ready` deltaP `14.7988` edge `0.3708` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.8511` n `48` status `ready` deltaP `34.3496` edge `0.35` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8511` n `48` status `ready` deltaP `34.3496` edge `0.35` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.5342` n `100` status `ready` deltaP `18.1829` edge `0.3292` maxDD `-7.4722`
- `market_context_high->crypto_alt_24h` score `1.7301` n `63` status `ready` deltaP `12.3016` edge `0.8591` maxDD `-50.5442`
- `market_context_high->crypto_alt_1h` score `1.6304` n `100` status `ready` deltaP `12.3533` edge `0.1486` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.009` n `48` status `ready` deltaP `6.6866` edge `0.0992` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.009` n `48` status `ready` deltaP `6.6866` edge `0.0992` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.9505` n `100` status `ready` deltaP `-3.7744` edge `0.169` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.7172` n `100` status `ready` deltaP `4.6467` edge `0.1051` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4545` n `48` status `ready` deltaP `5.8134` edge `0.0848` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4545` n `48` status `ready` deltaP `5.8134` edge `0.0848` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0508` n `100` status `ready` deltaP `5.3514` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1225` n `100` status `ready` deltaP `6.2515` edge `0.0042` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2411` n `100` status `ready` deltaP `9.6768` edge `0.0107` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3052` n `48` status `ready` deltaP `3.4182` edge `0.0037` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3052` n `48` status `ready` deltaP `3.4182` edge `0.0037` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

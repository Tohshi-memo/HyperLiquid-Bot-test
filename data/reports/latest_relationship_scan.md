# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T21:22:30.464469+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9002`

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

- `risk_on_high->crypto_alt_4h` score `4.8594` n `48` status `ready` deltaP `20.4777` edge `0.3132` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.8594` n `48` status `ready` deltaP `20.4777` edge `0.3132` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.1575` n `100` status `ready` deltaP `15.561` edge `0.3876` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.9718` n `48` status `ready` deltaP `35.1118` edge `0.3604` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9718` n `48` status `ready` deltaP `35.1118` edge `0.3604` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.72` n `100` status `ready` deltaP `18.9451` edge `0.3396` maxDD `-7.4722`
- `market_context_high->crypto_major_24h` score `3.2131` n `71` status `ready` deltaP `17.1215` edge `0.9919` maxDD `-46.1949`
- `market_context_high->crypto_alt_1h` score `1.6736` n `100` status `ready` deltaP `12.6527` edge `0.1502` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0522` n `48` status `ready` deltaP `6.986` edge `0.1008` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0522` n `48` status `ready` deltaP `6.986` edge `0.1008` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.722` n `100` status `ready` deltaP `4.7964` edge `0.1045` maxDD `-3.4384`
- `market_context_high->unknown_4h` score `0.7197` n `100` status `ready` deltaP `-4.0793` edge `0.1518` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `0.4576` n `48` status `ready` deltaP `5.9631` edge `0.0842` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4576` n `48` status `ready` deltaP `5.9631` edge `0.0842` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0508` n `100` status `ready` deltaP `5.3514` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1333` n `100` status `ready` deltaP `6.1018` edge `0.0043` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2009` n `100` status `ready` deltaP `10.1341` edge `0.011` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3159` n `48` status `ready` deltaP `3.2685` edge `0.0038` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3159` n `48` status `ready` deltaP `3.2685` edge `0.0038` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.351` n `100` status `ready` deltaP `-0.8529` edge `-0.0013` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

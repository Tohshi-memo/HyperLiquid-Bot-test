# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T19:52:28.922144+00:00`
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

- `market_context_high->crypto_major_24h` score `5.5529` n `65` status `ready` deltaP `22.4519` edge `1.1193` maxDD `-37.2327`
- `risk_on_high->crypto_alt_4h` score `4.6872` n `48` status `ready` deltaP `20.0204` edge `0.3019` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.6872` n `48` status `ready` deltaP `20.0204` edge `0.3019` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `3.9853` n `100` status `ready` deltaP `15.1037` edge `0.3763` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.8927` n `48` status `ready` deltaP `34.6545` edge `0.3533` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.8927` n `48` status `ready` deltaP `34.6545` edge `0.3533` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.5982` n `100` status `ready` deltaP `18.4878` edge `0.3325` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6352` n `100` status `ready` deltaP `12.3533` edge `0.149` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0138` n `48` status `ready` deltaP `6.6866` edge `0.0996` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0138` n `48` status `ready` deltaP `6.6866` edge `0.0996` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.7369` n `100` status `ready` deltaP `-3.7744` edge `0.1512` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.7112` n `100` status `ready` deltaP `4.6467` edge `0.1046` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4506` n `48` status `ready` deltaP `5.8134` edge `0.0843` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4506` n `48` status `ready` deltaP `5.8134` edge `0.0843` maxDD `-3.2233`
- `market_context_high->crypto_alt_24h` score `0.2819` n `65` status `ready` deltaP `10.4727` edge `0.7646` maxDD `-56.195`
- `market_context_high->index_1h` score `0.0508` n `100` status `ready` deltaP `5.3514` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1081` n `100` status `ready` deltaP `6.4012` edge `0.0044` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2143` n `100` status `ready` deltaP `9.9817` edge `0.0109` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.2908` n `48` status `ready` deltaP `3.5679` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.2908` n `48` status `ready` deltaP `3.5679` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

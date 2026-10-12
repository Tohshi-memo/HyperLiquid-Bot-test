# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T16:37:28.517908+00:00`
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

- `market_context_high->crypto_major_24h` score `20.8413` n `52` status `ready` deltaP `36.3115` edge `1.6469` maxDD `-9.176`
- `market_context_high->crypto_alt_24h` score `17.9093` n `52` status `ready` deltaP `24.3323` edge `1.5736` maxDD `-16.1364`
- `risk_on_high->crypto_alt_4h` score `4.0884` n `48` status `ready` deltaP `18.1911` edge `0.2642` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.0884` n `48` status `ready` deltaP `18.1911` edge `0.2642` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6192` n `48` status `ready` deltaP `33.1301` edge `0.3284` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6192` n `48` status `ready` deltaP `33.1301` edge `0.3284` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3865` n `100` status `ready` deltaP `13.2744` edge `0.3386` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.1774` n `100` status `ready` deltaP `16.9634` edge `0.3076` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5801` n `100` status `ready` deltaP `12.0539` edge `0.1464` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9587` n `48` status `ready` deltaP `6.3872` edge `0.097` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9587` n `48` status `ready` deltaP `6.3872` edge `0.097` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6584` n `100` status `ready` deltaP `4.3473` edge `0.1022` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4163` n `48` status `ready` deltaP `5.514` edge `0.0819` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4163` n `48` status `ready` deltaP `5.514` edge `0.0819` maxDD `-3.2233`
- `market_context_high->metal_24h` score `0.3361` n `52` status `ready` deltaP `11.4183` edge `0.0516` maxDD `-1.7708`
- `market_context_high->unknown_4h` score `0.0355` n `100` status `ready` deltaP `-4.2317` edge `0.0958` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0328` n `100` status `ready` deltaP `3.8498` edge `0.0032` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1321` n `100` status `ready` deltaP `6.1018` edge `0.0044` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

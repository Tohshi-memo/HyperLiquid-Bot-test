# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T16:22:24.151977+00:00`
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

- `market_context_high->crypto_major_24h` score `21.8267` n `51` status `ready` deltaP `37.8575` edge `1.6933` maxDD `-7.4764`
- `market_context_high->crypto_alt_24h` score `19.2965` n `51` status `ready` deltaP `25.8783` edge `1.6446` maxDD `-13.7267`
- `risk_on_high->crypto_alt_4h` score `4.0824` n `48` status `ready` deltaP `18.1911` edge `0.2637` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.0824` n `48` status `ready` deltaP `18.1911` edge `0.2637` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6231` n `48` status `ready` deltaP `33.1301` edge `0.3289` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6231` n `48` status `ready` deltaP `33.1301` edge `0.3289` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3805` n `100` status `ready` deltaP `13.2744` edge `0.3381` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.1834` n `100` status `ready` deltaP `16.9634` edge `0.3081` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5945` n `100` status `ready` deltaP `12.0539` edge `0.1476` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9731` n `48` status `ready` deltaP `6.3872` edge `0.0982` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9731` n `48` status `ready` deltaP `6.3872` edge `0.0982` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6728` n `100` status `ready` deltaP `4.3473` edge `0.1034` maxDD `-3.4384`
- `market_context_high->metal_24h` score `0.4812` n `51` status `ready` deltaP `12.7757` edge `0.0553` maxDD `-1.6354`
- `risk_on_high->crypto_major_1h` score `0.4256` n `48` status `ready` deltaP `5.514` edge `0.0831` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4256` n `48` status `ready` deltaP `5.514` edge `0.0831` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.0175` n `100` status `ready` deltaP `-4.2317` edge `0.0943` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0336` n `100` status `ready` deltaP `3.8498` edge `0.0031` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1321` n `100` status `ready` deltaP `6.1018` edge `0.0044` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

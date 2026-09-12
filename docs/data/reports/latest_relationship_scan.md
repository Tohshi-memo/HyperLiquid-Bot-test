# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T22:22:25.911262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12499`

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

- `market_context_high->unknown_24h` score `13606.9706` n `66` status `ready` deltaP `12.4211` edge `1133.8366` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.3612` n `82` status `ready` deltaP `-5.6996` edge `31.9436` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.0865` n `79` status `ready` deltaP `38.9196` edge `1.3948` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.8542` n `79` status `ready` deltaP `32.4521` edge `1.3203` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `12.0989` n `66` status `ready` deltaP `25.9312` edge `0.9181` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.9094` n `66` status `ready` deltaP `44.0972` edge `0.5318` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.6198` n `79` status `ready` deltaP `16.2491` edge `0.5988` maxDD `-5.7715`
- `news_risk_high->index_24h` score `6.3483` n `79` status `ready` deltaP `44.1126` edge `0.2526` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.2737` n `79` status `ready` deltaP `30.3402` edge `0.2826` maxDD `-0.6317`
- `market_context_high->commodity_24h` score `3.3505` n `66` status `ready` deltaP `36.1269` edge `0.0518` maxDD `-0.0748`
- `market_context_high->index_24h` score `3.3241` n `66` status `ready` deltaP `35.5587` edge `0.0793` maxDD `-0.1483`
- `risk_on_high->crypto_alt_4h` score `0.7291` n `47` status `ready` deltaP `10.3367` edge `0.1616` maxDD `-5.6296`
- `risk_on_and_context->crypto_alt_4h` score `0.7291` n `47` status `ready` deltaP `10.3367` edge `0.1616` maxDD `-5.6296`
- `risk_on_high->index_1h` score `0.1136` n `53` status `ready` deltaP `7.4427` edge `0.0003` maxDD `-0.162`
- `risk_on_and_context->index_1h` score `0.1136` n `53` status `ready` deltaP `7.4427` edge `0.0003` maxDD `-0.162`
- `news_risk_high->index_4h` score `0.0747` n `82` status `ready` deltaP `6.7073` edge `0.0277` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `-0.0255` n `53` status `ready` deltaP `4.3865` edge `0.0005` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0255` n `53` status `ready` deltaP `4.3865` edge `0.0005` maxDD `-0.3081`
- `market_context_high->equity_4h` score `-0.1084` n `94` status `ready` deltaP `10.4794` edge `0.0304` maxDD `-3.466`
- `market_context_high->metal_24h` score `-0.1757` n `66` status `ready` deltaP `4.6402` edge `0.1027` maxDD `-3.4925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

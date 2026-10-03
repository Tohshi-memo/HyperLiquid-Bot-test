# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T01:07:28.067638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.2971` n `50` status `ready` deltaP `10.4251` edge `30.2935` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.6993` n `50` status `ready` deltaP `10.3659` edge `24.3225` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.103` n `70` status `ready` deltaP `34.1915` edge `1.0879` maxDD `-2.2476`
- `market_context_high->crypto_alt_24h` score `10.825` n `50` status `ready` deltaP `21.0486` edge `0.9321` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.6554` n `70` status `ready` deltaP `33.7351` edge `0.6282` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9723` n `50` status `ready` deltaP `31.6528` edge `0.6783` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.6091` n `50` status `ready` deltaP `18.3049` edge `0.5824` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.3425` n `105` status `ready` deltaP `29.5034` edge `0.5496` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.0259` n `50` status `ready` deltaP `16.6463` edge `0.5201` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `5.6083` n `70` status `ready` deltaP `9.6528` edge `0.5728` maxDD `-7.9166`
- `news_risk_high->crypto_major_4h` score `4.7476` n `105` status `ready` deltaP `21.7335` edge `0.3893` maxDD `-6.7511`
- `market_context_high->crypto_alt_1h` score `3.229` n `50` status `ready` deltaP `14.8024` edge `0.2367` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.0926` n `105` status `ready` deltaP `25.6925` edge `0.1477` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0097` n `50` status `ready` deltaP `13.4012` edge `0.2065` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8275` n `50` status `ready` deltaP `31.622` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->index_24h` score `1.6968` n `70` status `ready` deltaP `19.2361` edge `0.0582` maxDD `-0.2696`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.2632` n `50` status `ready` deltaP `6.0208` edge `0.308` maxDD `-11.8957`
- `news_risk_high->metal_24h` score `1.2184` n `70` status `ready` deltaP `12.1429` edge `0.2012` maxDD `-2.0759`
- `news_risk_high->crypto_alt_1h` score `1.2098` n `105` status `ready` deltaP `4.9929` edge `0.1236` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

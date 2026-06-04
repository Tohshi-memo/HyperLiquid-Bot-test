# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T10:22:22.900771+00:00`
- Price records: `672`
- Market context records: `2857`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `4.123` n `142` status `ready` deltaP `3.7437` edge `0.7103` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.3733` n `142` status `ready` deltaP `5.7267` edge `0.2894` maxDD `-1.7175`
- `market_context_high->equity_24h` score `1.479` n `142` status `ready` deltaP `5.0885` edge `0.2897` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.303` n `142` status `ready` deltaP `13.9891` edge `0.3247` maxDD `-12.4171`
- `market_context_high->index_24h` score `0.9408` n `142` status `ready` deltaP `7.2868` edge `0.1279` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.9022` n `142` status `ready` deltaP `6.0331` edge `0.1403` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.3803` n `142` status `ready` deltaP `13.6057` edge `0.0422` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.175` n `142` status `ready` deltaP `4.9296` edge `0.0548` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0843` n `142` status `ready` deltaP `4.0483` edge `0.0116` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.5821` n `142` status `ready` deltaP `5.2459` edge `0.0664` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6194` n `142` status `ready` deltaP `-0.5819` edge `-0.0002` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.7084` n `142` status `ready` deltaP `-2.4837` edge `0.0019` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7674` n `142` status `ready` deltaP `-0.6157` edge `-0.0097` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.7861` n `142` status `ready` deltaP `4.5248` edge `0.056` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.8` n `142` status `ready` deltaP `3.0294` edge `0.0511` maxDD `-5.7037`
- `market_context_high->equity_1h` score `-0.8523` n `142` status `ready` deltaP `-2.3003` edge `0.0276` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.9979` n `142` status `ready` deltaP `13.7281` edge `0.2594` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2369` n `142` status `ready` deltaP `-4.5152` edge `0.0049` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2714` n `142` status `ready` deltaP `2.4476` edge `0.0127` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3987` n `142` status `ready` deltaP `-1.8852` edge `-0.0168` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

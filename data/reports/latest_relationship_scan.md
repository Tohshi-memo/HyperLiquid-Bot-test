# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T00:37:26.399953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10450`

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

- `risk_on_high->unknown_4h` score `19.9519` n `133` status `ready` deltaP `8.9985` edge `1.6645` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9519` n `133` status `ready` deltaP `8.9985` edge `1.6645` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4544` n `217` status `ready` deltaP `9.4351` edge `0.7945` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.6934` n `41` status `ready` deltaP `20.2363` edge `0.3665` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `3.3448` n `41` status `ready` deltaP `16.0061` edge `0.2161` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `2.9382` n `41` status `ready` deltaP `16.8064` edge `0.15` maxDD `-0.042`
- `news_risk_high->metal_4h` score `2.1375` n `41` status `ready` deltaP `21.9513` edge `0.0539` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6849` n `41` status `ready` deltaP `15.2366` edge `0.0779` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5784` n `41` status `ready` deltaP `9.6037` edge `0.0876` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.4273` n `41` status `ready` deltaP `17.8874` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.0515` n `41` status `ready` deltaP `12.8158` edge `0.0215` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.9371` n `41` status `ready` deltaP `4.0018` edge `0.0697` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.8` n `41` status `ready` deltaP `5.9452` edge `0.0599` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.6868` n `41` status `ready` deltaP `6.4846` edge `0.0405` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0685` n `41` status `ready` deltaP `7.5763` edge `0.0029` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `-0.0531` n `41` status `ready` deltaP `6.5549` edge `-0.0029` maxDD `-0.9514`
- `risk_on_high->index_1h` score `-0.2291` n `133` status `ready` deltaP `2.7948` edge `-0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2291` n `133` status `ready` deltaP `2.7948` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T01:37:25.365184+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10456`

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

- `risk_on_high->unknown_4h` score `19.7797` n `133` status `ready` deltaP `8.5412` edge `1.6532` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.7797` n `133` status `ready` deltaP `8.5412` edge `1.6532` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.2822` n `217` status `ready` deltaP `8.9778` edge `0.7832` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.9822` n `40` status `ready` deltaP `20.3819` edge `0.3896` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `3.3308` n `40` status `ready` deltaP `15.4268` edge `0.2188` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `3.2714` n `40` status `ready` deltaP `18.7153` edge `0.1606` maxDD `-0.0201`
- `news_risk_high->metal_4h` score `2.3067` n `40` status `ready` deltaP `23.8415` edge `0.0554` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.7043` n `40` status `ready` deltaP `15.1647` edge `0.08` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.551` n `40` status `ready` deltaP `8.811` edge `0.0906` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.3939` n `40` status `ready` deltaP `17.4551` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1784` n `40` status `ready` deltaP `14.2515` edge `0.0225` maxDD `-0.2118`
- `news_risk_high->crypto_alt_4h` score `0.9375` n `40` status `ready` deltaP `7.439` edge `0.0614` maxDD `-1.296`
- `news_risk_high->crypto_major_1h` score `0.8085` n `40` status `ready` deltaP `2.9042` edge `0.0663` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.5764` n `40` status `ready` deltaP `5.2096` edge `0.0398` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.1284` n `40` status `ready` deltaP `8.7126` edge `0.003` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `-0.1676` n `40` status `ready` deltaP `5.2744` edge `-0.0039` maxDD `-0.9514`
- `news_risk_high->fx_24h` score `-0.1864` n `40` status `ready` deltaP `8.9583` edge `0.0391` maxDD `-3.1481`
- `risk_on_high->index_1h` score `-0.2128` n `133` status `ready` deltaP `3.0942` edge `-0.0034` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

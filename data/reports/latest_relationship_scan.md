# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T00:52:28.042836+00:00`
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

- `risk_on_high->unknown_4h` score `19.9543` n `133` status `ready` deltaP `8.9985` edge `1.6647` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9543` n `133` status `ready` deltaP `8.9985` edge `1.6647` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4568` n `217` status `ready` deltaP `9.4351` edge `0.7947` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.9129` n `40` status `ready` deltaP `19.8611` edge `0.3873` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `3.3018` n `40` status `ready` deltaP `15.2744` edge `0.2174` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `3.2877` n `40` status `ready` deltaP `18.8889` edge `0.1608` maxDD `-0.0201`
- `news_risk_high->metal_4h` score `2.3055` n `40` status `ready` deltaP `23.8415` edge `0.0553` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6636` n `40` status `ready` deltaP `14.7156` edge `0.0796` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5656` n `40` status `ready` deltaP `8.9634` edge `0.0908` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.3688` n `40` status `ready` deltaP `17.1557` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1784` n `40` status `ready` deltaP `14.2515` edge `0.0225` maxDD `-0.2118`
- `news_risk_high->crypto_alt_4h` score `0.9555` n `40` status `ready` deltaP `7.439` edge `0.0629` maxDD `-1.296`
- `news_risk_high->crypto_major_1h` score `0.8121` n `40` status `ready` deltaP `2.9042` edge `0.0666` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.6195` n `40` status `ready` deltaP `5.509` edge `0.0414` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.154` n `40` status `ready` deltaP `9.1617` edge `0.0033` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `news_risk_high->fx_4h` score `-0.1664` n `40` status `ready` deltaP `5.2744` edge `-0.0038` maxDD `-0.9514`
- `news_risk_high->fx_24h` score `-0.2074` n `40` status `ready` deltaP `8.7847` edge `0.0385` maxDD `-3.1481`
- `risk_on_high->index_1h` score `-0.2291` n `133` status `ready` deltaP `2.7948` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

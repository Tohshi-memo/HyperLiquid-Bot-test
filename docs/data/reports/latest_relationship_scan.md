# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T01:07:25.108043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10452`

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

- `risk_on_high->unknown_4h` score `19.9313` n `133` status `ready` deltaP `8.846` edge `1.6638` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9313` n `133` status `ready` deltaP `8.846` edge `1.6638` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4338` n `217` status `ready` deltaP `9.2826` edge `0.7938` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `5.9424` n `40` status `ready` deltaP `20.0347` edge `0.3886` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `3.309` n `40` status `ready` deltaP `15.2744` edge `0.218` maxDD `-1.1927`
- `news_risk_high->commodity_24h` score `3.2726` n `40` status `ready` deltaP `18.7153` edge `0.1607` maxDD `-0.0201`
- `news_risk_high->metal_4h` score `2.3055` n `40` status `ready` deltaP `23.8415` edge `0.0553` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6768` n `40` status `ready` deltaP `14.8653` edge `0.0797` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5644` n `40` status `ready` deltaP `8.9634` edge `0.0907` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.3688` n `40` status `ready` deltaP `17.1557` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1784` n `40` status `ready` deltaP `14.2515` edge `0.0225` maxDD `-0.2118`
- `news_risk_high->crypto_alt_4h` score `0.9519` n `40` status `ready` deltaP `7.439` edge `0.0626` maxDD `-1.296`
- `news_risk_high->crypto_major_1h` score `0.8277` n `40` status `ready` deltaP `3.0539` edge `0.0669` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.6171` n `40` status `ready` deltaP `5.509` edge `0.0412` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.1455` n `40` status `ready` deltaP `9.012` edge `0.0032` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `news_risk_high->fx_4h` score `-0.1664` n `40` status `ready` deltaP `5.2744` edge `-0.0038` maxDD `-0.9514`
- `market_context_high->crypto_major_24h` score `-0.2007` n `167` status `ready` deltaP `20.5631` edge `0.7926` maxDD `-61.3797`
- `news_risk_high->fx_24h` score `-0.205` n `40` status `ready` deltaP `8.7847` edge `0.0387` maxDD `-3.1481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

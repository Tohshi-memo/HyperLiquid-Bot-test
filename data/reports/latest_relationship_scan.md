# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T23:37:29.148336+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10658`

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

- `risk_on_high->unknown_4h` score `19.9411` n `133` status `ready` deltaP `8.9985` edge `1.6636` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9411` n `133` status `ready` deltaP `8.9985` edge `1.6636` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4436` n `217` status `ready` deltaP `9.4351` edge `0.7936` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `4.8411` n `45` status `ready` deltaP `21.4931` edge `0.2871` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.36` n `45` status `ready` deltaP `9.7188` edge `0.1802` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.2164` n `45` status `ready` deltaP `13.2292` edge `0.1137` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6566` n `45` status `ready` deltaP `17.3001` edge `0.049` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6411` n `45` status `ready` deltaP `11.8123` edge `0.0781` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5851` n `45` status `ready` deltaP `15.0998` edge `0.0705` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.0913` n `45` status `ready` deltaP `13.9721` edge `0.0112` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7231` n `45` status `ready` deltaP `9.2515` edge `0.0179` maxDD `-0.2118`
- `news_risk_high->commodity_1h` score `0.3524` n `45` status `ready` deltaP `10.3793` edge `0.0048` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `0.3435` n `45` status `ready` deltaP `11.1077` edge `-0.0002` maxDD `-0.9514`
- `news_risk_high->crypto_alt_1h` score `0.1876` n `45` status `ready` deltaP `3.7359` edge `0.021` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.1381` n `133` status `ready` deltaP `13.1613` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1381` n `133` status `ready` deltaP `13.1613` edge `0.0012` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0929` n `45` status `ready` deltaP `-0.5356` edge `0.0447` maxDD `-1.0047`
- `news_risk_high->crypto_alt_4h` score `-0.2021` n `45` status `ready` deltaP `0.7012` edge `0.0209` maxDD `-1.7264`
- `risk_on_high->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2213` n `133` status `ready` deltaP `2.9445` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

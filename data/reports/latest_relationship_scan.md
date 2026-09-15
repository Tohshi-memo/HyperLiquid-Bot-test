# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T14:22:35.981622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11070`

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

- `news_risk_high->unknown_4h` score `396.496` n `78` status `ready` deltaP `-23.0652` edge `33.2845` maxDD `-4.1517`
- `news_risk_high->crypto_alt_24h` score `22.4978` n `78` status `ready` deltaP `47.0753` edge `1.6001` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.4363` n `78` status `ready` deltaP `20.8333` edge `1.7308` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.5662` n `78` status `ready` deltaP `38.3414` edge `1.3553` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.0984` n `78` status `ready` deltaP `48.8114` edge `1.1102` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4448` n `78` status `ready` deltaP `59.8557` edge `0.3223` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4306` n `78` status `ready` deltaP `37.6202` edge `0.3305` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0196` n `52` status `ready` deltaP `38.1944` edge `0.247` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0196` n `52` status `ready` deltaP `38.1944` edge `0.247` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7226` n `137` status `ready` deltaP `30.8951` edge `0.2401` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.3899` n `52` status `ready` deltaP `40.2644` edge `0.0183` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.3899` n `52` status `ready` deltaP `40.2644` edge `0.0183` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.9929` n `137` status `ready` deltaP `37.078` edge `0.0238` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7428` n `52` status `ready` deltaP `23.8508` edge `0.0212` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7428` n `52` status `ready` deltaP `23.8508` edge `0.0212` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6425` n `149` status `ready` deltaP `20.3531` edge `0.043` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7551` n `149` status `ready` deltaP `12.7678` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.687` n `78` status `ready` deltaP `17.1162` edge `0.0368` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2038` n `149` status `ready` deltaP `10.0384` edge `0.0068` maxDD `-0.1412`
- `risk_on_high->metal_1h` score `0.1731` n `52` status `ready` deltaP `7.0129` edge `0.006` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

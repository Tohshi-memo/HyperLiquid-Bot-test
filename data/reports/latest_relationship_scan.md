# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T18:22:36.141822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11093`

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

- `news_risk_high->unknown_4h` score `396.1253` n `78` status `ready` deltaP `-23.9798` edge `33.2597` maxDD `-4.1517`
- `news_risk_high->unknown_24h` score `24.6792` n `78` status `ready` deltaP `21.1806` edge `1.9154` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.0634` n `78` status `ready` deltaP `47.7698` edge `1.6426` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `18.5406` n `78` status `ready` deltaP `39.5566` edge `1.4284` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.4673` n `78` status `ready` deltaP `49.8531` edge `1.134` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4141` n `78` status `ready` deltaP `59.6821` edge `0.3209` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.6152` n `78` status `ready` deltaP `38.4882` edge `0.3401` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0292` n `52` status `ready` deltaP `38.1944` edge `0.2478` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0292` n `52` status `ready` deltaP `38.1944` edge `0.2478` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7322` n `137` status `ready` deltaP `30.8951` edge `0.2409` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.0621` n `52` status `ready` deltaP `37.4866` edge `0.0095` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.0621` n `52` status `ready` deltaP `37.4866` edge `0.0095` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.6651` n `137` status `ready` deltaP `34.3002` edge `0.015` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.6448` n `52` status `ready` deltaP `23.2411` edge `0.0171` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.6448` n `52` status `ready` deltaP `23.2411` edge `0.0171` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5445` n `149` status `ready` deltaP `19.7434` edge `0.0389` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7453` n `78` status `ready` deltaP `17.8784` edge `0.0392` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.6257` n `149` status `ready` deltaP `11.5702` edge `0.0127` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.1482` n `52` status `ready` deltaP `6.5638` edge `0.0058` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1482` n `52` status `ready` deltaP `6.5638` edge `0.0058` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

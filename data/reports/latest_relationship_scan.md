# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T02:37:27.568120+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.4924` n `83` status `ready` deltaP `-20.9007` edge `31.6865` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.6978` n `83` status `ready` deltaP `38.6985` edge `1.2714` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.2796` n `83` status `ready` deltaP `30.7647` edge `1.2677` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.4785` n `83` status `ready` deltaP `39.9975` edge `0.8673` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.6138` n `52` status `ready` deltaP `42.8819` edge `0.3486` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.6138` n `52` status `ready` deltaP `42.8819` edge `0.3486` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5382` n `83` status `ready` deltaP `45.4276` edge `0.2596` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.3146` n `149` status `ready` deltaP `36.1705` edge `0.3376` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.725` n `83` status `ready` deltaP `31.9905` edge `0.2259` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5548` n `52` status `ready` deltaP `33.32` edge `-0.005` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5548` n `52` status `ready` deltaP `33.32` edge `-0.005` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4199` n `149` status `ready` deltaP `30.5451` edge `0.0196` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.255` n `52` status `ready` deltaP `28.424` edge `0.0334` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.255` n `52` status `ready` deltaP `28.424` edge `0.0334` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1548` n `149` status `ready` deltaP `24.9263` edge `0.0552` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9443` n `149` status `ready` deltaP `14.7139` edge `0.0183` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3643` n `83` status `ready` deltaP `11.736` edge `0.0313` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.796` edge `0.01` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.796` edge `0.01` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1544` n `52` status `ready` deltaP `6.4141` edge `0.0076` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

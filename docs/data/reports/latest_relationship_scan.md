# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T02:22:29.770584+00:00`
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

- `news_risk_high->unknown_4h` score `377.4972` n `83` status `ready` deltaP `-20.9007` edge `31.6869` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.7789` n `83` status `ready` deltaP `38.8721` edge `1.277` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.3535` n `83` status `ready` deltaP `30.9383` edge `1.2727` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.55` n `83` status `ready` deltaP `40.1711` edge `0.8721` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.5711` n `52` status `ready` deltaP `42.7083` edge `0.3462` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.5711` n `52` status `ready` deltaP `42.7083` edge `0.3462` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5592` n `83` status `ready` deltaP `45.6012` edge `0.2602` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.2719` n `149` status `ready` deltaP `35.9969` edge `0.3352` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.7454` n `83` status `ready` deltaP `31.9905` edge `0.2276` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5536` n `52` status `ready` deltaP `33.32` edge `-0.0051` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5536` n `52` status `ready` deltaP `33.32` edge `-0.0051` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4187` n `149` status `ready` deltaP `30.5451` edge `0.0195` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2708` n `52` status `ready` deltaP `28.5764` edge `0.0337` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2708` n `52` status `ready` deltaP `28.5764` edge `0.0337` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1705` n `149` status `ready` deltaP `25.0787` edge `0.0555` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9443` n `149` status `ready` deltaP `14.7139` edge `0.0183` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3627` n `83` status `ready` deltaP `11.736` edge `0.0311` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.796` edge `0.01` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.796` edge `0.01` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1435` n `52` status `ready` deltaP `6.2644` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

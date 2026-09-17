# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T12:22:23.935628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.5096` n `83` status `ready` deltaP `-22.1202` edge `32.2794` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.6137` n `83` status `ready` deltaP `31.9277` edge `0.9762` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.1219` n `83` status `ready` deltaP `23.9939` edge `1.0497` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.2174` n `52` status `ready` deltaP `49.6528` edge `0.4371` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2174` n `52` status `ready` deltaP `49.6528` edge `0.4371` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.7048` n `83` status `ready` deltaP `33.2267` edge `0.6813` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.9183` n `149` status `ready` deltaP `42.9414` edge `0.4261` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.7205` n `83` status `ready` deltaP `38.6567` edge `0.2366` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.9495` n `83` status `ready` deltaP `31.296` edge `0.1659` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.7175` n `52` status `ready` deltaP `31.6252` edge `0.0506` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7175` n `52` status `ready` deltaP `31.6252` edge `0.0506` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6172` n `149` status `ready` deltaP `28.1275` edge `0.0724` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.4118` n `52` status `ready` deltaP `31.7575` edge `-0.0065` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4118` n `52` status `ready` deltaP `31.7575` edge `-0.0065` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2769` n `149` status `ready` deltaP `28.9826` edge `0.0181` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1229` n `149` status `ready` deltaP `16.3606` edge `0.0222` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4996` n `52` status `ready` deltaP `9.4427` edge `0.0139` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4996` n `52` status `ready` deltaP `9.4427` edge `0.0139` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.153` n `83` status `ready` deltaP `8.9921` edge `0.0225` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0797` n `149` status `ready` deltaP `5.1009` edge `0.002` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

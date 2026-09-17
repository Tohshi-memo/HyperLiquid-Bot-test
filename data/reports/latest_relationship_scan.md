# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T00:52:05.663359+00:00`
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

- `news_risk_high->unknown_4h` score `376.926` n `83` status `ready` deltaP `-20.9007` edge `31.6393` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.3818` n `83` status `ready` deltaP `39.9138` edge `1.3203` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.8928` n `83` status `ready` deltaP `31.98` edge `1.3107` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.0773` n `83` status `ready` deltaP `41.2128` edge `0.9091` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.2897` n `52` status `ready` deltaP `41.6667` edge `0.3297` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.2897` n `52` status `ready` deltaP `41.6667` edge `0.3297` maxDD `0.0`
- `news_risk_high->index_24h` score `6.7038` n `83` status `ready` deltaP `46.6428` edge `0.2653` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.9906` n `149` status `ready` deltaP `34.9553` edge `0.3187` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.9582` n `83` status `ready` deltaP `32.6849` edge `0.2407` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4673` n `52` status `ready` deltaP `32.4519` edge `-0.0065` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4673` n `52` status `ready` deltaP `32.4519` edge `-0.0065` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.345` n `52` status `ready` deltaP `29.3386` edge `0.0348` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.345` n `52` status `ready` deltaP `29.3386` edge `0.0348` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.3325` n `149` status `ready` deltaP `29.677` edge `0.0181` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2447` n `149` status `ready` deltaP `25.8409` edge `0.0566` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9959` n `149` status `ready` deltaP `15.163` edge `0.0196` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3856` n `83` status `ready` deltaP `12.0408` edge `0.032` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1576` n `52` status `ready` deltaP `6.4141` edge `0.008` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

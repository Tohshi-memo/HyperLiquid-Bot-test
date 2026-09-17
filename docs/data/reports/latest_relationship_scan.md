# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T00:37:29.130153+00:00`
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

- `news_risk_high->unknown_4h` score `376.7928` n `83` status `ready` deltaP `-20.9007` edge `31.6282` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.4869` n `83` status `ready` deltaP `40.0874` edge `1.3279` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.9811` n `83` status `ready` deltaP `32.1536` edge `1.3169` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.1692` n `83` status `ready` deltaP `41.3864` edge `0.9156` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.235` n `52` status `ready` deltaP `41.4931` edge `0.3263` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.235` n `52` status `ready` deltaP `41.4931` edge `0.3263` maxDD `0.0`
- `news_risk_high->index_24h` score `6.7273` n `83` status `ready` deltaP `46.8164` edge `0.2661` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.9359` n `149` status `ready` deltaP `34.7817` edge `0.3153` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.981` n `83` status `ready` deltaP `32.6849` edge `0.2426` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4487` n `52` status `ready` deltaP `32.2783` edge `-0.0069` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4487` n `52` status `ready` deltaP `32.2783` edge `-0.0069` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3462` n `52` status `ready` deltaP `29.3386` edge `0.0349` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3462` n `52` status `ready` deltaP `29.3386` edge `0.0349` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.3138` n `149` status `ready` deltaP `29.5034` edge `0.0177` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2459` n `149` status `ready` deltaP `25.8409` edge `0.0567` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9959` n `149` status `ready` deltaP `15.163` edge `0.0196` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3872` n `83` status `ready` deltaP `12.0408` edge `0.0322` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1498` n `52` status `ready` deltaP `6.2644` edge `0.008` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

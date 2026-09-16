# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T23:52:25.363845+00:00`
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

- `news_risk_high->unknown_4h` score `374.328` n `83` status `ready` deltaP `-20.9007` edge `31.4228` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.7661` n `83` status `ready` deltaP `40.6083` edge `1.3477` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.2316` n `83` status `ready` deltaP `32.6744` edge `1.3343` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.4437` n `83` status `ready` deltaP `41.9073` edge `0.935` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.0854` n `52` status `ready` deltaP `40.9722` edge `0.3173` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0854` n `52` status `ready` deltaP `40.9722` edge `0.3173` maxDD `0.0`
- `news_risk_high->index_24h` score `6.8013` n `83` status `ready` deltaP `47.3373` edge `0.2688` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.7862` n `149` status `ready` deltaP `34.2608` edge `0.3063` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.0542` n `83` status `ready` deltaP `32.6849` edge `0.2487` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4252` n `52` status `ready` deltaP `32.1047` edge `-0.0077` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4252` n `52` status `ready` deltaP `32.1047` edge `-0.0077` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3546` n `52` status `ready` deltaP `29.3386` edge `0.0356` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3546` n `52` status `ready` deltaP `29.3386` edge `0.0356` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2903` n `149` status `ready` deltaP `29.3298` edge `0.0169` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2543` n `149` status `ready` deltaP `25.8409` edge `0.0574` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9959` n `149` status `ready` deltaP `15.163` edge `0.0196` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3926` n `83` status `ready` deltaP `12.0408` edge `0.0329` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3726` n `52` status `ready` deltaP `8.2451` edge `0.0113` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1778` n `52` status `ready` deltaP `6.7135` edge `0.0086` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

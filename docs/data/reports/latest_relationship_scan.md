# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T22:24:53.283376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10767`

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

- `news_risk_high->unknown_4h` score `372.114` n `83` status `ready` deltaP `-20.9007` edge `31.2383` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.1013` n `83` status `ready` deltaP `41.3027` edge `1.371` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.5993` n `83` status `ready` deltaP `33.7161` edge `1.358` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.9506` n `83` status `ready` deltaP `42.9489` edge `0.9703` maxDD `-6.5262`
- `news_risk_high->index_24h` score `6.9399` n `83` status `ready` deltaP `48.3789` edge `0.2734` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.774` n `52` status `ready` deltaP `39.9306` edge `0.2983` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.774` n `52` status `ready` deltaP `39.9306` edge `0.2983` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4749` n `149` status `ready` deltaP `33.2192` edge `0.2873` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.1814` n `83` status `ready` deltaP `32.6849` edge `0.2593` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4168` n `52` status `ready` deltaP `32.1047` edge `-0.0084` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4168` n `52` status `ready` deltaP `32.1047` edge `-0.0084` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.4068` n `52` status `ready` deltaP `29.796` edge `0.0369` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4068` n `52` status `ready` deltaP `29.796` edge `0.0369` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.3065` n `149` status `ready` deltaP `26.2983` edge `0.0587` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2819` n `149` status `ready` deltaP `29.3298` edge `0.0162` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9575` n `149` status `ready` deltaP `14.7139` edge `0.0194` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4447` n `83` status `ready` deltaP `12.803` edge `0.0345` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3343` n `52` status `ready` deltaP `7.796` edge `0.0111` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3343` n `52` status `ready` deltaP `7.796` edge `0.0111` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1957` n `52` status `ready` deltaP `7.0129` edge `0.0089` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

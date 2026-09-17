# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T00:07:27.244583+00:00`
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

- `news_risk_high->unknown_4h` score `376.53` n `83` status `ready` deltaP `-20.9007` edge `31.6063` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.6815` n `83` status `ready` deltaP `40.4346` edge `1.3418` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.1505` n `83` status `ready` deltaP `32.5008` edge `1.3287` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.3494` n `83` status `ready` deltaP `41.7336` edge `0.9283` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.1365` n `52` status `ready` deltaP `41.1458` edge `0.3204` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1365` n `52` status `ready` deltaP `41.1458` edge `0.3204` maxDD `0.0`
- `news_risk_high->index_24h` score `6.7754` n `83` status `ready` deltaP `47.1637` edge `0.2678` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.8373` n `149` status `ready` deltaP `34.4344` edge `0.3094` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.0302` n `83` status `ready` deltaP `32.6849` edge `0.2467` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4288` n `52` status `ready` deltaP `32.1047` edge `-0.0074` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4288` n `52` status `ready` deltaP `32.1047` edge `-0.0074` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3522` n `52` status `ready` deltaP `29.3386` edge `0.0354` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3522` n `52` status `ready` deltaP `29.3386` edge `0.0354` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2939` n `149` status `ready` deltaP `29.3298` edge `0.0172` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2519` n `149` status `ready` deltaP `25.8409` edge `0.0572` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9971` n `149` status `ready` deltaP `15.163` edge `0.0197` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3903` n `83` status `ready` deltaP `12.0408` edge `0.0326` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3738` n `52` status `ready` deltaP `8.2451` edge `0.0114` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3738` n `52` status `ready` deltaP `8.2451` edge `0.0114` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1677` n `52` status `ready` deltaP `6.5638` edge `0.0083` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

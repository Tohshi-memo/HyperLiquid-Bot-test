# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T20:22:29.234970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10548`

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

- `news_risk_high->unknown_4h` score `396.896` n `78` status `ready` deltaP `-22.4554` edge `33.3137` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.0019` n `78` status `ready` deltaP `18.9236` edge `1.874` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.9229` n `78` status `ready` deltaP `46.7281` edge `1.5545` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.7282` n `78` status `ready` deltaP `34.0011` edge `1.3144` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.7146` n `78` status `ready` deltaP `41.5197` edge `1.0441` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7267` n `78` status `ready` deltaP `61.9391` edge `0.3319` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4289` n `78` status `ready` deltaP `37.7938` edge `0.3292` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.3799` n `121` status `ready` deltaP `36.4583` edge `0.2886` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.8951` n `51` status `ready` deltaP `36.4583` edge `0.2482` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8951` n `51` status `ready` deltaP `36.4583` edge `0.2482` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.5119` n `51` status `ready` deltaP `50.6434` edge `0.0426` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.5119` n `51` status `ready` deltaP `50.6434` edge `0.0426` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.1455` n `121` status `ready` deltaP `47.6455` edge `0.0494` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1227` n `52` status `ready` deltaP `27.2045` edge `0.0305` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1227` n `52` status `ready` deltaP `27.2045` edge `0.0305` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.923` n `137` status `ready` deltaP `22.6144` edge `0.0513` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7814` n `137` status `ready` deltaP `12.812` edge `0.0174` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6258` n `78` status `ready` deltaP `15.7442` edge `0.0381` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.266` n `52` status `ready` deltaP `7.1972` edge `0.0094` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.266` n `52` status `ready` deltaP `7.1972` edge `0.0094` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

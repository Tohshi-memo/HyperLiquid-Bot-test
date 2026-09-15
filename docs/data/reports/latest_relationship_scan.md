# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T07:52:34.671615+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11166`

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

- `news_risk_high->unknown_4h` score `399.2354` n `78` status `ready` deltaP `-21.9981` edge `33.5056` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.0395` n `78` status `ready` deltaP `18.2292` edge `1.7151` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.4104` n `78` status `ready` deltaP `44.2976` edge `1.528` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.067` n `78` status `ready` deltaP `34.0011` edge `1.2593` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.8188` n `78` status `ready` deltaP `47.5961` edge `1.0956` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6123` n `78` status `ready` deltaP `61.2446` edge `0.327` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4608` n `78` status `ready` deltaP `37.9674` edge `0.3307` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0473` n `52` status `ready` deltaP `38.5417` edge `0.247` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0473` n `52` status `ready` deltaP `38.5417` edge `0.247` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7504` n `137` status `ready` deltaP `31.2424` edge `0.2401` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.9119` n `52` status `ready` deltaP `44.7783` edge `0.0317` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.9119` n `52` status `ready` deltaP `44.7783` edge `0.0317` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.5149` n `137` status `ready` deltaP `41.5919` edge `0.0372` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9555` n `52` status `ready` deltaP `25.0703` edge `0.0308` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9555` n `52` status `ready` deltaP `25.0703` edge `0.0308` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8553` n `149` status `ready` deltaP `21.5726` edge `0.0526` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8258` n `149` status `ready` deltaP `13.3666` edge `0.0174` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6632` n `78` status `ready` deltaP `16.6588` edge `0.0368` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2479` n `52` status `ready` deltaP `8.2105` edge `0.0076` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2479` n `52` status `ready` deltaP `8.2105` edge `0.0076` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T17:52:33.601372+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9046`

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

- `news_risk_high->unknown_4h` score `421.9695` n `77` status `ready` deltaP `-20.8821` edge `35.3928` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.3707` n `52` status `ready` deltaP `50.1736` edge `0.4464` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3707` n `52` status `ready` deltaP `50.1736` edge `0.4464` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.0751` n `75` status `ready` deltaP `29.3056` edge `0.6988` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `8.8596` n `75` status `ready` deltaP `20.7291` edge `0.7996` maxDD `-13.2931`
- `market_context_high->commodity_24h` score `8.0715` n `149` status `ready` deltaP `43.4622` edge `0.4354` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.8095` n `75` status `ready` deltaP `29.0555` edge `0.6345` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.486` n `75` status `ready` deltaP `36.8958` edge `0.2288` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.6473` n `75` status `ready` deltaP `27.7292` edge `0.1645` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9299` n `52` status `ready` deltaP `32.5399` edge `0.0622` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9299` n `52` status `ready` deltaP `32.5399` edge `0.0622` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8296` n `149` status `ready` deltaP `29.0422` edge `0.084` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.0306` n `52` status `ready` deltaP `27.938` edge `-0.0128` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.0306` n `52` status `ready` deltaP `27.938` edge `-0.0128` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.8958` n `149` status `ready` deltaP `25.1631` edge `0.0118` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1193` n `149` status `ready` deltaP `16.0612` edge `0.0239` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7833` n `77` status `ready` deltaP `13.2701` edge `0.0234` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.4961` n `52` status `ready` deltaP `9.1433` edge `0.0156` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4961` n `52` status `ready` deltaP `9.1433` edge `0.0156` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2048` n `149` status `ready` deltaP `10.3433` edge `0.0049` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

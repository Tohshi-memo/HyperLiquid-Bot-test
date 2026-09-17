# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T16:52:29.578376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `news_risk_high->unknown_4h` score `408.8839` n `79` status `ready` deltaP `-22.287` edge `34.3117` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `10.3021` n `79` status `ready` deltaP `30.3183` edge `0.7943` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `10.164` n `79` status `ready` deltaP `22.0793` edge `0.8993` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4261` n `52` status `ready` deltaP `50.5208` edge `0.4487` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4261` n `52` status `ready` deltaP `50.5208` edge `0.4487` maxDD `0.0`
- `market_context_high->commodity_24h` score `8.1269` n `149` status `ready` deltaP `43.8094` edge `0.4377` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `8.0417` n `79` status `ready` deltaP `30.6083` edge `0.6435` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.5958` n `79` status `ready` deltaP `37.6384` edge `0.233` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7283` n `79` status `ready` deltaP `29.1469` edge `0.1618` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9311` n `52` status `ready` deltaP `32.5399` edge `0.0623` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9311` n `52` status `ready` deltaP `32.5399` edge `0.0623` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8308` n `149` status `ready` deltaP `29.0422` edge `0.0841` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.1042` n `52` status `ready` deltaP `28.6325` edge `-0.0113` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.1042` n `52` status `ready` deltaP `28.6325` edge `-0.0113` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.9693` n `149` status `ready` deltaP `25.8576` edge `0.0133` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1373` n `149` status `ready` deltaP `16.2109` edge `0.0244` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.514` n `52` status `ready` deltaP `9.293` edge `0.0161` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.514` n `52` status `ready` deltaP `9.293` edge `0.0161` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.4539` n `79` status `ready` deltaP `9.5728` edge `0.0208` maxDD `-0.4099`
- `market_context_high->fx_4h` score `0.1874` n `149` status `ready` deltaP `10.0384` edge `0.0047` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

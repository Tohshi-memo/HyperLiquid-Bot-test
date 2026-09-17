# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T17:07:36.865172+00:00`
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

- `news_risk_high->unknown_4h` score `415.5716` n `78` status `ready` deltaP `-21.5955` edge `34.8644` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `10.0067` n `78` status `ready` deltaP `30.0748` edge `0.7713` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `9.8296` n `78` status `ready` deltaP `21.7548` edge `0.8736` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4213` n `52` status `ready` deltaP `50.5208` edge `0.4483` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4213` n `52` status `ready` deltaP `50.5208` edge `0.4483` maxDD `0.0`
- `market_context_high->commodity_24h` score `8.1221` n `149` status `ready` deltaP `43.8094` edge `0.4373` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.9807` n `78` status `ready` deltaP `30.235` edge `0.6409` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.5659` n `78` status `ready` deltaP `37.4599` edge `0.2317` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7071` n `78` status `ready` deltaP `28.8061` edge `0.1623` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9287` n `52` status `ready` deltaP `32.5399` edge `0.0621` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9287` n `52` status `ready` deltaP `32.5399` edge `0.0621` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8284` n `149` status `ready` deltaP `29.0422` edge `0.0839` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.0855` n `52` status `ready` deltaP `28.4588` edge `-0.0117` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.0855` n `52` status `ready` deltaP `28.4588` edge `-0.0117` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.9506` n `149` status `ready` deltaP `25.6839` edge `0.0129` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1337` n `149` status `ready` deltaP `16.2109` edge `0.0241` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5213` n `78` status `ready` deltaP `10.2643` edge `0.0216` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.5104` n `52` status `ready` deltaP `9.293` edge `0.0158` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5104` n `52` status `ready` deltaP `9.293` edge `0.0158` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1961` n `149` status `ready` deltaP `10.1909` edge `0.0048` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

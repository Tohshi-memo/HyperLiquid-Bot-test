# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T15:52:29.211133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8860`

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

- `news_risk_high->unknown_4h` score `390.0668` n `82` status `ready` deltaP `-23.1708` edge `32.7495` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `11.2661` n `82` status `ready` deltaP `31.0129` edge `0.87` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.2233` n `82` status `ready` deltaP `23.0056` edge `0.9814` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4261` n `52` status `ready` deltaP `50.5208` edge `0.4487` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4261` n `52` status `ready` deltaP `50.5208` edge `0.4487` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.1708` n `82` status `ready` deltaP `31.847` edge `0.646` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.1269` n `149` status `ready` deltaP `43.8094` edge `0.4377` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6618` n `82` status `ready` deltaP `38.1479` edge `0.2351` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7761` n `82` status `ready` deltaP `30.1194` edge `0.1593` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9239` n `52` status `ready` deltaP `32.5399` edge `0.0617` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9239` n `52` status `ready` deltaP `32.5399` edge `0.0617` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8236` n `149` status `ready` deltaP `29.0422` edge `0.0835` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.1729` n `52` status `ready` deltaP `29.3269` edge `-0.0102` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.1729` n `52` status `ready` deltaP `29.3269` edge `-0.0102` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.0381` n `149` status `ready` deltaP `26.552` edge `0.0144` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1133` n `149` status `ready` deltaP `16.0612` edge `0.0234` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4901` n `52` status `ready` deltaP `9.1433` edge `0.0151` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4901` n `52` status `ready` deltaP `9.1433` edge `0.0151` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1533` n `149` status `ready` deltaP `9.4287` edge `0.0044` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1132` n `149` status `ready` deltaP `5.6997` edge `0.0023` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

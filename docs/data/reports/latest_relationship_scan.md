# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T16:07:27.403783+00:00`
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

- `news_risk_high->unknown_4h` score `390.0512` n `82` status `ready` deltaP `-23.1708` edge `32.7482` maxDD `-4.1571`
- `news_risk_high->crypto_major_24h` score `11.2209` n `82` status `ready` deltaP `23.0056` edge `0.9812` maxDD `-13.2931`
- `news_risk_high->crypto_alt_24h` score `11.2013` n `82` status `ready` deltaP `31.0129` edge `0.8646` maxDD `-9.3661`
- `risk_on_high->commodity_24h` score `9.4309` n `52` status `ready` deltaP `50.5208` edge `0.4491` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4309` n `52` status `ready` deltaP `50.5208` edge `0.4491` maxDD `0.0`
- `market_context_high->commodity_24h` score `8.1317` n `149` status `ready` deltaP `43.8094` edge `0.4381` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `8.1197` n `82` status `ready` deltaP `31.6734` edge `0.6429` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.6606` n `82` status `ready` deltaP `38.1479` edge `0.235` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7725` n `82` status `ready` deltaP `30.1194` edge `0.159` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9287` n `52` status `ready` deltaP `32.5399` edge `0.0621` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9287` n `52` status `ready` deltaP `32.5399` edge `0.0621` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8284` n `149` status `ready` deltaP `29.0422` edge `0.0839` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.1567` n `52` status `ready` deltaP `29.1533` edge `-0.0104` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.1567` n `52` status `ready` deltaP `29.1533` edge `-0.0104` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.0218` n `149` status `ready` deltaP `26.3784` edge `0.0142` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1313` n `149` status `ready` deltaP `16.2109` edge `0.0239` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.508` n `52` status `ready` deltaP `9.293` edge `0.0156` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.508` n `52` status `ready` deltaP `9.293` edge `0.0156` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1628` n `149` status `ready` deltaP `9.5811` edge `0.0046` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1217` n `149` status `ready` deltaP `5.8494` edge `0.0024` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

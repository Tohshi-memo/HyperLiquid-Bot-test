# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T15:22:28.634882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8884`

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

- `news_risk_high->unknown_4h` score `390.1136` n `82` status `ready` deltaP `-23.1708` edge `32.7534` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `11.3897` n `82` status `ready` deltaP `31.0129` edge `0.8803` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.2197` n `82` status `ready` deltaP `23.0056` edge `0.9811` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.4026` n `52` status `ready` deltaP `50.3472` edge `0.4479` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4026` n `52` status `ready` deltaP `50.3472` edge `0.4479` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.2634` n `82` status `ready` deltaP `32.1943` edge `0.6514` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.1034` n `149` status `ready` deltaP `43.6358` edge `0.4369` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.663` n `82` status `ready` deltaP `38.1479` edge `0.2352` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7936` n `82` status `ready` deltaP `30.293` edge `0.1596` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9095` n `52` status `ready` deltaP `32.5399` edge `0.0605` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9095` n `52` status `ready` deltaP `32.5399` edge `0.0605` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8092` n `149` status `ready` deltaP `29.0422` edge `0.0823` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.2067` n `52` status `ready` deltaP `29.6741` edge `-0.0097` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.2067` n `52` status `ready` deltaP `29.6741` edge `-0.0097` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.0718` n `149` status `ready` deltaP `26.8992` edge `0.0149` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1061` n `149` status `ready` deltaP `16.0612` edge `0.0228` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4829` n `52` status `ready` deltaP `9.1433` edge `0.0145` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4829` n `52` status `ready` deltaP `9.1433` edge `0.0145` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1359` n `149` status `ready` deltaP `9.1238` edge `0.0042` maxDD `-0.1412`
- `news_risk_high->index_4h` score `0.1053` n `82` status `ready` deltaP `8.0792` edge `0.0182` maxDD `-0.6848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

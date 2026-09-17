# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T14:07:31.078048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8682`

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

- `news_risk_high->unknown_4h` score `384.2299` n `83` status `ready` deltaP `-23.1873` edge `32.2632` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `11.9257` n `83` status `ready` deltaP `31.2333` edge `0.9235` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.6704` n `83` status `ready` deltaP `23.2994` edge `1.0167` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3635` n `52` status `ready` deltaP `50.1736` edge `0.4458` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3635` n `52` status `ready` deltaP `50.1736` edge `0.4458` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.3889` n `83` status `ready` deltaP `32.5323` edge `0.6596` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0643` n `149` status `ready` deltaP `43.4622` edge `0.4348` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6675` n `83` status `ready` deltaP `38.3095` edge `0.2345` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.8303` n `83` status `ready` deltaP `30.6016` edge `0.1606` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.8711` n `52` status `ready` deltaP `32.5399` edge `0.0573` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8711` n `52` status `ready` deltaP `32.5399` edge `0.0573` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7708` n `149` status `ready` deltaP `29.0422` edge `0.0791` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.2942` n `52` status `ready` deltaP `30.5422` edge `-0.0082` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.2942` n `52` status `ready` deltaP `30.5422` edge `-0.0082` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.1593` n `149` status `ready` deltaP `27.7673` edge `0.0164` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1361` n `149` status `ready` deltaP `16.3606` edge `0.0233` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.4427` edge `0.015` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.4427` edge `0.015` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.0901` n `149` status `ready` deltaP `8.3616` edge `0.0034` maxDD `-0.1412`
- `news_risk_high->index_4h` score `0.0717` n `83` status `ready` deltaP `7.925` edge `0.0192` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

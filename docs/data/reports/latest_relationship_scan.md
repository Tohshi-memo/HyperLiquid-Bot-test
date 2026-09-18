# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T23:07:28.568206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `55.002` n `39` status `ready` deltaP `32.2783` edge `4.4575` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `50.7541` n `39` status `ready` deltaP `33.7073` edge `4.1427` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.9024` n `149` status `ready` deltaP `-0.9208` edge `3.188` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.9982` n `39` status `ready` deltaP `42.5214` edge `0.7465` maxDD `-1.0765`
- `risk_on_high->unknown_4h` score `11.7811` n `52` status `ready` deltaP `-8.1614` edge `1.0587` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7811` n `52` status `ready` deltaP `-8.1614` edge `1.0587` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `9.0676` n `76` status `ready` deltaP `28.9554` edge `0.6752` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.7807` n `76` status `ready` deltaP `24.2057` edge `0.4378` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.0714` n `39` status `ready` deltaP `29.6207` edge `0.1576` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1982` n `76` status `ready` deltaP `17.6962` edge `0.1951` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.8271` n `52` status `ready` deltaP `32.8447` edge `0.0516` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8271` n `52` status `ready` deltaP `32.8447` edge `0.0516` maxDD `-0.1313`
- `news_risk_high->crypto_major_1h` score `2.7889` n `76` status `ready` deltaP `21.3442` edge `0.1424` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `2.7268` n `149` status `ready` deltaP `29.347` edge `0.0734` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.6397` n `76` status `ready` deltaP `14.0004` edge `0.1333` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.391` n `76` status `ready` deltaP `15.3001` edge `0.0358` maxDD `-0.084`
- `news_risk_high->equity_1h` score `1.2963` n `76` status `ready` deltaP `15.0725` edge `0.0481` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

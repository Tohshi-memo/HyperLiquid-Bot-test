# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T21:37:32.964569+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8170`

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

- `news_risk_high->crypto_major_24h` score `41.5926` n `39` status `ready` deltaP `20.3259` edge `3.4239` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `40.4341` n `39` status `ready` deltaP `33.7073` edge `3.2827` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.774` n `149` status `ready` deltaP `-0.9208` edge `3.1773` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.6527` n `52` status `ready` deltaP `-8.1614` edge `1.048` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6527` n `52` status `ready` deltaP `-8.1614` edge `1.048` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.7932` n `82` status `ready` deltaP `29.7256` edge `0.6472` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.5287` n `39` status `ready` deltaP `28.1784` edge `0.5144` maxDD `-2.6561`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `2.9549` n `82` status `ready` deltaP `20.122` edge `0.378` maxDD `-8.9985`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.2944` n `39` status `ready` deltaP `17.6683` edge `0.1017` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `1.9114` n `82` status `ready` deltaP `12.7538` edge `0.1443` maxDD `-3.27`
- `news_risk_high->equity_4h` score `1.8198` n `82` status `ready` deltaP `16.311` edge `0.1329` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.1553` n `82` status `ready` deltaP `12.9573` edge `0.0321` maxDD `-0.1099`
- `market_context_high->commodity_1h` score `1.1349` n `149` status `ready` deltaP `16.3606` edge `0.0232` maxDD `-0.3491`
- `news_risk_high->crypto_major_1h` score `1.0181` n `82` status `ready` deltaP `15.8135` edge `0.1006` maxDD `-3.7064`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T14:52:31.806135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8022`

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

- `market_context_high->unknown_4h` score `94.3937` n `150` status `ready` deltaP `0.4018` edge `7.897` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5227` n `113` status `ready` deltaP `27.6207` edge `0.1499` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.1539` n `150` status `ready` deltaP `9.656` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1409` n `152` status `ready` deltaP `6.8031` edge `0.0022` maxDD `-0.1986`
- `market_context_high->fx_24h` score `-0.0438` n `113` status `ready` deltaP `18.4828` edge `0.0284` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.204` n `152` status `ready` deltaP `7.3401` edge `0.0041` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3611` n `152` status `ready` deltaP `1.421` edge `0.0105` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.3978` n `113` status `ready` deltaP `11.5689` edge `0.0001` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.535` n `152` status `ready` deltaP `-0.4937` edge `-0.0001` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.5829` n `150` status `ready` deltaP `5.1476` edge `0.04` maxDD `-1.165`
- `market_context_high->metal_4h` score `-1.0684` n `150` status `ready` deltaP `5.7808` edge `-0.0045` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.0923` n `152` status `ready` deltaP `2.7958` edge `-0.0006` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.7719` n `150` status `ready` deltaP `-4.0395` edge `-0.0128` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.1155` n `152` status `ready` deltaP `-0.4347` edge `-0.0397` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.2115` n `152` status `ready` deltaP `-1.7809` edge `-0.0232` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.337` n `113` status `ready` deltaP `-1.8159` edge `-0.0582` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8836` n `150` status `ready` deltaP `-2.344` edge `-0.1065` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9675` n `113` status `ready` deltaP `-2.0445` edge `-0.1939` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4028` n `113` status `ready` deltaP `-18.0365` edge `-0.1417` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.4676` n `150` status `ready` deltaP `-3.452` edge `-0.2082` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

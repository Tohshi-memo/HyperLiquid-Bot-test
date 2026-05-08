# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T06:07:19.047340+00:00`
- Price records: `620`
- Market context records: `725`
- Flow alert records: `2049`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `11.8087` n `146` status `ready` deltaP `28.6129` edge `0.8267` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3538` n `146` status `ready` deltaP `7.9029` edge `0.4816` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.324` n `149` status `ready` deltaP `5.5514` edge `0.0086` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.3697` n `146` status `ready` deltaP `-0.3899` edge `0.1713` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.4368` n `155` status `ready` deltaP `2.8357` edge `0.0025` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5154` n `155` status `ready` deltaP `2.1453` edge `0.0402` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.918` n `155` status `ready` deltaP `0.8328` edge `0.0033` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.989` n `149` status `ready` deltaP `17.6552` edge `0.1261` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0486` n `155` status `ready` deltaP `-0.6378` edge `-0.0021` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0867` n `155` status `ready` deltaP `5.4713` edge `-0.0035` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2115` n `146` status `ready` deltaP `-2.1575` edge `0.1739` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.4791` n `155` status `ready` deltaP `3.9767` edge `-0.0183` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5623` n `155` status `ready` deltaP `-4.5266` edge `-0.023` maxDD `-3.4946`
- `market_context_high->index_4h` score `-1.8491` n `149` status `ready` deltaP `1.0917` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0033` n `149` status `ready` deltaP `3.2601` edge `0.0683` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8047` n `149` status `ready` deltaP `-1.9083` edge `-0.0058` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2535` n `155` status `ready` deltaP `-4.5601` edge `-0.0448` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.601` n `149` status `ready` deltaP `-5.2628` edge `0.0851` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9939` n `149` status `ready` deltaP `4.3035` edge `-0.1737` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2183` n `146` status `ready` deltaP `-13.9252` edge `-0.059` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

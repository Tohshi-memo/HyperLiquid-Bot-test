# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T00:22:27.893731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10807`

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

- `risk_on_high->unknown_4h` score `21.2246` n `135` status `ready` deltaP `-3.0646` edge `1.9897` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.2246` n `135` status `ready` deltaP `-3.0646` edge `1.9897` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.4351` n `230` status `ready` deltaP `1.4926` edge `0.9398` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.7752` n `37` status `ready` deltaP `24.4839` edge `0.345` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9031` n `37` status `ready` deltaP `20.1389` edge `0.191` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3069` n `37` status `ready` deltaP `16.4181` edge `0.2074` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.7461` n `153` status `ready` deltaP `14.757` edge `0.4843` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.5763` n `37` status `ready` deltaP `12.935` edge `0.0842` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5368` n `37` status `ready` deltaP `7.313` edge `0.0994` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.4079` n `78` status `ready` deltaP `11.445` edge `0.8368` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.4079` n `78` status `ready` deltaP `11.445` edge `0.8368` maxDD `-47.9416`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1631` n `37` status `ready` deltaP `6.1661` edge `0.0741` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.0469` n `37` status `ready` deltaP `21.3447` edge `0.0465` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8686` n `37` status `ready` deltaP `8.7272` edge `0.0407` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.082` n `37` status `ready` deltaP `3.0447` edge `0.0194` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0356` n `37` status `ready` deltaP `5.5754` edge `0.0029` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

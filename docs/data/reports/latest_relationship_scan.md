# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T10:52:32.117109+00:00`
- Price records: `672`
- Market context records: `8613`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5192.709` n `60` status `ready` deltaP `34.2345` edge `432.5396` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.508` n `40` status `ready` deltaP `52.0451` edge `1.2351` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1615` n `60` status `ready` deltaP `20.7991` edge `0.4345` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4447` n `60` status `ready` deltaP `20.9513` edge `0.0831` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.7545` n `62` status `ready` deltaP `12.8271` edge `0.1564` maxDD `-5.323`
- `market_context_high->fx_24h` score `1.7465` n `40` status `ready` deltaP `27.565` edge `0.0771` maxDD `-0.6228`
- `news_risk_high->equity_1h` score `1.6844` n `60` status `ready` deltaP `14.9302` edge `0.0885` maxDD `-2.4803`
- `market_context_high->crypto_major_24h` score `1.2669` n `40` status `ready` deltaP `6.2998` edge `0.4942` maxDD `-23.9025`
- `news_risk_high->crypto_major_4h` score `1.0075` n `60` status `ready` deltaP `5.9893` edge `0.1668` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4584` n `60` status `ready` deltaP `8.6327` edge `0.0539` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3434` n `60` status `ready` deltaP `6.517` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3073` n `60` status `ready` deltaP `14.6651` edge `0.0236` maxDD `-0.6604`
- `news_risk_high->crypto_alt_4h` score `0.3017` n `60` status `ready` deltaP `9.9239` edge `0.1117` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1242` n `60` status `ready` deltaP `5.8982` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0679` n `60` status `ready` deltaP `5.6387` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `0.058` n `60` status `ready` deltaP `3.0822` edge `0.0345` maxDD `-0.8085`
- `news_risk_high->index_1h` score `-0.0162` n `60` status `ready` deltaP `3.0739` edge `0.0091` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.1551` n `62` status `ready` deltaP `8.0522` edge `0.013` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2591` n `62` status `ready` deltaP `2.5111` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.313` n `62` status `ready` deltaP `4.1578` edge `-0.0053` maxDD `-2.0038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

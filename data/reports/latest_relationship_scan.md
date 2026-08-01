# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T12:22:24.232227+00:00`
- Price records: `672`
- Market context records: `8621`
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

- `news_risk_high->unknown_24h` score `5192.1486` n `60` status `ready` deltaP `34.2345` edge `432.4929` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.7827` n `44` status `ready` deltaP `52.9542` edge `1.1686` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1895` n `60` status `ready` deltaP `21.1035` edge `0.4348` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.469` n `60` status `ready` deltaP `21.2557` edge `0.0831` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6688` n `60` status `ready` deltaP `14.7805` edge `0.0882` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5699` n `60` status `ready` deltaP `12.1994` edge `0.1452` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0971` n `60` status `ready` deltaP `6.9026` edge `0.1722` maxDD `-3.5385`
- `market_context_high->fx_24h` score `0.8233` n `44` status `ready` deltaP `18.1504` edge `0.0544` maxDD `-1.5878`
- `news_risk_high->crypto_alt_1h` score `0.4265` n `60` status `ready` deltaP `8.1836` edge `0.0528` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3661` n `60` status `ready` deltaP `10.5327` edge `0.1159` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3341` n `60` status `ready` deltaP `6.3673` edge `0.0516` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3145` n `60` status `ready` deltaP `14.6651` edge `0.0242` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1274` n `60` status `ready` deltaP `5.8982` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.1007` n `60` status `ready` deltaP `3.8432` edge `0.0349` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.0679` n `60` status `ready` deltaP `5.6387` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0147` n `60` status `ready` deltaP `3.0739` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0165` n `60` status `ready` deltaP `9.6651` edge `0.0138` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.1665` n `60` status `ready` deltaP `4.2315` edge `0.0007` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3348` n `60` status `ready` deltaP `3.7625` edge `-0.0058` maxDD `-1.9764`
- `market_context_high->crypto_alt_1h` score `-0.6033` n `60` status `ready` deltaP `-3.483` edge `0.0086` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

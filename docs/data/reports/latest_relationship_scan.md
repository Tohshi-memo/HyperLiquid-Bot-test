# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T00:07:24.389311+00:00`
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

- `risk_on_high->unknown_4h` score `20.3643` n `134` status `ready` deltaP `-3.1831` edge `1.9188` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.3643` n `134` status `ready` deltaP `-3.1831` edge `1.9188` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.0247` n `229` status `ready` deltaP `1.5064` edge `0.9055` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.8755` n `37` status `ready` deltaP `24.6575` edge `0.3522` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9031` n `37` status `ready` deltaP `20.1389` edge `0.191` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3093` n `37` status `ready` deltaP `16.4181` edge `0.2076` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.7864` n `153` status `ready` deltaP `14.9306` edge `0.4865` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.5763` n `37` status `ready` deltaP `12.935` edge `0.0842` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5368` n `37` status `ready` deltaP `7.313` edge `0.0994` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.4723` n `78` status `ready` deltaP `11.6186` edge `0.8439` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.4723` n `78` status `ready` deltaP `11.6186` edge `0.8439` maxDD `-47.9416`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.181` n `37` status `ready` deltaP `6.3158` edge `0.0746` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.0306` n `37` status `ready` deltaP `21.1711` edge `0.0463` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8913` n `37` status `ready` deltaP `8.8769` edge `0.0416` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1074` n `37` status `ready` deltaP `3.1971` edge `0.0205` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0433` n `37` status `ready` deltaP `5.4257` edge `0.0029` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

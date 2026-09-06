# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T01:07:24.445327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10963`

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

- `risk_on_high->unknown_4h` score `22.2133` n `138` status `ready` deltaP `-3.3051` edge `2.0737` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `22.2133` n `138` status `ready` deltaP `-3.3051` edge `2.0737` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.9047` n `233` status `ready` deltaP `1.1671` edge `0.9811` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.4791` n `37` status `ready` deltaP `23.963` edge `0.3238` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9019` n `37` status `ready` deltaP `20.1389` edge `0.1909` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2803` n `37` status `ready` deltaP `16.2657` edge `0.2062` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.6216` n `153` status `ready` deltaP `14.2361` edge `0.4774` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3747` n `37` status `ready` deltaP `24.1513` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.5632` n `37` status `ready` deltaP `12.7853` edge `0.0841` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5222` n `37` status `ready` deltaP `7.1605` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3317` n `37` status `ready` deltaP `15.9128` edge `0.0242` maxDD `-0.2118`
- `risk_on_high->crypto_major_24h` score `1.2061` n `78` status `ready` deltaP `10.9242` edge `0.8144` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.2061` n `78` status `ready` deltaP `10.9242` edge `0.8144` maxDD `-47.9416`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1055` n `37` status `ready` deltaP `5.717` edge `0.0723` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.0958` n `37` status `ready` deltaP `21.8656` edge `0.0471` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.7882` n `37` status `ready` deltaP `8.2781` edge `0.037` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.0036` n `37` status `ready` deltaP `2.7398` edge `0.0149` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0449` n `37` status `ready` deltaP `5.4257` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

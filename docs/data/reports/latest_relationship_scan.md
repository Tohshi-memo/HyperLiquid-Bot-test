# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T19:37:31.763051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `28.3699` n `58` status `ready` deltaP `1.6874` edge `2.3679` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `15.5546` n `101` status `ready` deltaP `3.4567` edge `1.959` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.9973` n `101` status `ready` deltaP `3.8418` edge `1.2956` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7023` n `101` status `ready` deltaP `17.3946` edge `0.3135` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0295` n `101` status `ready` deltaP `19.0715` edge `0.2511` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6323` n `101` status `ready` deltaP `15.932` edge `0.1597` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `1.9933` n `101` status `ready` deltaP `27.7107` edge `0.2014` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.9237` n `101` status `ready` deltaP `17.429` edge `0.0964` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.652` n `40` status `ready` deltaP `-4.6181` edge `0.164` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.5994` n `58` status `ready` deltaP `4.2123` edge `0.0472` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.4843` n `101` status `ready` deltaP `13.2507` edge `0.0122` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4669` n `58` status `ready` deltaP `7.8825` edge `0.0119` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3537` n `101` status `ready` deltaP `10.1651` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2649` n `101` status `ready` deltaP `14.2025` edge `0.0328` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2064` n `58` status `ready` deltaP `4.8008` edge `0.016` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.0777` n `58` status `ready` deltaP `11.1228` edge `-0.0005` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.1505` n `40` status `ready` deltaP `11.6319` edge `-0.0667` maxDD `-0.2042`
- `market_context_high->crypto_major_1h` score `-0.3612` n `58` status `ready` deltaP `-2.39` edge `0.0577` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

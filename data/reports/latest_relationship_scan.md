# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T22:37:25.528288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8700`

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

- `news_risk_high->crypto_major_24h` score `51.1088` n `72` status `ready` deltaP `27.0833` edge `4.1677` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5484` n `72` status `ready` deltaP `33.507` edge `3.6269` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `21.017` n `108` status `ready` deltaP `-4.8837` edge `1.8073` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.6291` n `72` status `ready` deltaP `36.9792` edge `0.4768` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.963` n `108` status `ready` deltaP `39.5254` edge `0.4526` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8104` n `98` status `ready` deltaP `21.7707` edge `0.46` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5123` n `98` status `ready` deltaP `22.3805` edge `0.3526` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3084` n `98` status `ready` deltaP `18.7737` edge `0.1971` maxDD `-2.058`
- `market_context_high->commodity_4h` score `3.0783` n `108` status `ready` deltaP `29.9345` edge `0.0888` maxDD `-0.2136`
- `news_risk_high->crypto_major_1h` score `2.4667` n `98` status `ready` deltaP `20.121` edge `0.1237` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.699` n `72` status `ready` deltaP `22.3958` edge `0.0767` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5471` n `110` status `ready` deltaP `18.8133` edge `0.0287` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0857` n `108` status `ready` deltaP `20.472` edge `0.0008` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7455` n `98` status `ready` deltaP `18.2149` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.5508` n `72` status `ready` deltaP `3.6459` edge `0.0398` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.4335` n `108` status `ready` deltaP `9.6644` edge `-0.0241` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4306` n `98` status `ready` deltaP `6.816` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.1885` n `110` status `ready` deltaP `5.969` edge `0.0017` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.1495` n `98` status `ready` deltaP `7.8366` edge `0.0797` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

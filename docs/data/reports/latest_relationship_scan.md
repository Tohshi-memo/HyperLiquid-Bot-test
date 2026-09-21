# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T19:07:34.415756+00:00`
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

- `market_context_high->unknown_4h` score `28.5317` n `58` status `ready` deltaP `1.5349` edge `2.3824` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `15.9963` n `101` status `ready` deltaP `3.8039` edge `1.9935` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `10.3455` n `101` status `ready` deltaP `4.189` edge `1.3223` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7227` n `101` status `ready` deltaP `17.3946` edge `0.3152` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1139` n `101` status `ready` deltaP `19.3763` edge `0.2561` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6119` n `101` status `ready` deltaP `15.932` edge `0.158` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `1.9324` n `101` status `ready` deltaP `27.3635` edge `0.1959` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.8937` n `101` status `ready` deltaP `17.429` edge `0.0939` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.6317` n `58` status `ready` deltaP `4.5117` edge `0.0479` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5106` n `101` status `ready` deltaP `13.5501` edge `0.0124` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4944` n `58` status `ready` deltaP `8.1819` edge `0.0122` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3415` n `101` status `ready` deltaP `10.0126` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2929` n `101` status `ready` deltaP `14.5073` edge `0.0331` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2327` n `58` status `ready` deltaP `5.1002` edge `0.0162` maxDD `-0.1314`
- `market_context_high->index_24h` score `0.2088` n `38` status `ready` deltaP `-6.1129` edge `0.1464` maxDD `-1.644`
- `market_context_high->index_4h` score `0.0975` n `58` status `ready` deltaP `11.4277` edge `0.0` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.2641` n `38` status `ready` deltaP `10.3161` edge `-0.0674` maxDD `-0.2042`
- `market_context_high->crypto_major_1h` score `-0.3912` n `58` status `ready` deltaP `-2.39` edge `0.0552` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

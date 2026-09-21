# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T17:52:30.690862+00:00`
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

- `market_context_high->unknown_4h` score `28.4737` n `58` status `ready` deltaP `1.23` edge `2.3796` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `17.0318` n `101` status `ready` deltaP `4.672` edge `2.074` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `11.189` n `101` status `ready` deltaP `5.057` edge `1.3868` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7505` n `101` status `ready` deltaP `17.5471` edge `0.3165` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2731` n `101` status `ready` deltaP `19.9861` edge `0.2653` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6394` n `101` status `ready` deltaP `16.0817` edge `0.1593` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9225` n `101` status `ready` deltaP `17.429` edge `0.0963` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.7804` n `101` status `ready` deltaP `26.4954` edge `0.1822` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7456` n `58` status `ready` deltaP `5.2602` edge `0.0524` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5861` n `101` status `ready` deltaP `14.2986` edge `0.0137` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5639` n `58` status `ready` deltaP `8.9304` edge `0.013` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4217` n `58` status `ready` deltaP `9.6738` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3415` n `101` status `ready` deltaP `10.0126` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3269` n `101` status `ready` deltaP `14.8122` edge `0.0339` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3082` n `58` status `ready` deltaP `5.8487` edge `0.0175` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1535` n `58` status `ready` deltaP `12.1899` edge `0.0021` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1274` n `101` status `ready` deltaP `4.0404` edge `0.0068` maxDD `-0.2147`
- `market_context_high->index_24h` score `-0.2507` n `34` status `ready` deltaP `-9.5793` edge `0.1106` maxDD `-1.644`
- `news_risk_high->equity_1h` score `-0.3292` n `101` status `ready` deltaP `0.873` edge `0.0073` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.3624` n `58` status `ready` deltaP `-2.39` edge `0.0576` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

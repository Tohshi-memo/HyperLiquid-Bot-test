# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T17:07:30.485272+00:00`
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

- `market_context_high->unknown_4h` score `28.4005` n `58` status `ready` deltaP `1.23` edge `2.3735` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `17.5258` n `101` status `ready` deltaP `5.1928` edge `2.1117` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `11.5858` n `101` status `ready` deltaP `5.5779` edge `1.4164` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7059` n `101` status `ready` deltaP `17.3946` edge `0.3138` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2827` n `101` status `ready` deltaP `19.9861` edge `0.2661` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5387` n `101` status `ready` deltaP `15.6326` edge `0.1539` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.859` n `101` status `ready` deltaP `17.1296` edge `0.093` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.6885` n `101` status `ready` deltaP `25.9746` edge `0.1739` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7624` n `58` status `ready` deltaP `5.4099` edge `0.0528` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5651` n `58` status `ready` deltaP `8.9304` edge `0.0131` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4217` n `58` status `ready` deltaP `9.6738` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3185` n `101` status `ready` deltaP `14.8122` edge `0.0332` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.3037` n `101` status `ready` deltaP `9.5553` edge `0.0252` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.2877` n `31` status `ready` deltaP `13.7041` edge `-0.0533` maxDD `-0.1267`
- `market_context_high->metal_1h` score `0.2794` n `58` status `ready` deltaP `5.5493` edge `0.0171` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.189` n `58` status `ready` deltaP `12.6472` edge `0.0036` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1274` n `101` status `ready` deltaP `4.0404` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3125` n `101` status `ready` deltaP `1.0227` edge `0.0077` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.426` n `58` status `ready` deltaP `-2.6894` edge `0.0543` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

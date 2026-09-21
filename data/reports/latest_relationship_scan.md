# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T17:37:32.668267+00:00`
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

- `market_context_high->unknown_4h` score `28.4089` n `58` status `ready` deltaP `1.23` edge `2.3742` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `17.1885` n `101` status `ready` deltaP `4.8456` edge `2.0859` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `11.3133` n `101` status `ready` deltaP `5.2307` edge `1.396` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7373` n `101` status `ready` deltaP `17.5471` edge `0.3154` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2731` n `101` status `ready` deltaP `19.9861` edge `0.2653` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6035` n `101` status `ready` deltaP `15.932` edge `0.1573` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8913` n `101` status `ready` deltaP `17.2793` edge `0.0947` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.7495` n `101` status `ready` deltaP `26.3218` edge `0.1794` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7612` n `58` status `ready` deltaP `5.4099` edge `0.0527` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5861` n `101` status `ready` deltaP `14.2986` edge `0.0137` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5771` n `58` status `ready` deltaP `9.0801` edge `0.0131` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4337` n `58` status `ready` deltaP `9.8235` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3293` n `101` status `ready` deltaP `9.8602` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3257` n `101` status `ready` deltaP `14.8122` edge `0.0338` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3082` n `58` status `ready` deltaP `5.8487` edge `0.0175` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1653` n `58` status `ready` deltaP `12.3423` edge `0.0026` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1154` n `101` status `ready` deltaP `4.1901` edge `0.0068` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.2244` n `33` status `ready` deltaP `9.1856` edge `-0.0613` maxDD `-0.1577`
- `news_risk_high->equity_1h` score `-0.3137` n `101` status `ready` deltaP `1.0227` edge `0.0076` maxDD `-0.9112`
- `market_context_high->index_24h` score `-0.3838` n `33` status `ready` deltaP `-10.6534` edge `0.1007` maxDD `-1.644`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

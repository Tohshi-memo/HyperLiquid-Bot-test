# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T09:07:32.585699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6362` n `83` status `ready` deltaP `-21.6629` edge `32.2869` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.0135` n `83` status `ready` deltaP `34.1846` edge `1.0778` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.0777` n `83` status `ready` deltaP `26.2508` edge `1.1143` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.5322` n `83` status `ready` deltaP `35.4836` edge `0.7352` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.7669` n `52` status `ready` deltaP `47.3958` edge `0.4146` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7669` n `52` status `ready` deltaP `47.3958` edge `0.4146` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4677` n `149` status `ready` deltaP `40.6844` edge `0.4036` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.9706` n `83` status `ready` deltaP `40.9137` edge `0.2424` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.1314` n `83` status `ready` deltaP `31.4696` edge `0.1799` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6157` n `52` status `ready` deltaP `33.8408` edge `-0.0034` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6157` n `52` status `ready` deltaP `33.8408` edge `-0.0034` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4808` n `149` status `ready` deltaP `31.0659` edge `0.0212` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.4198` n `52` status `ready` deltaP `29.6435` edge `0.039` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4198` n `52` status `ready` deltaP `29.6435` edge `0.039` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.3195` n `149` status `ready` deltaP `26.1458` edge `0.0608` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9815` n `149` status `ready` deltaP `15.0133` edge `0.0194` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.3582` n `52` status `ready` deltaP `8.0954` edge `0.0111` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3582` n `52` status `ready` deltaP `8.0954` edge `0.0111` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.313` n `83` status `ready` deltaP `10.9738` edge `0.0298` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0766` n `52` status `ready` deltaP `5.2165` edge `0.0056` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

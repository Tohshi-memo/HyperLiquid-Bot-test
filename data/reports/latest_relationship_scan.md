# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T23:07:38.731233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6755`

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

- `market_context_high->unknown_24h` score `3690.4083` n `86` status `ready` deltaP `-11.9549` edge `307.6567` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `118.0517` n `86` status `ready` deltaP `0.9501` edge `9.8446` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0656` n `108` status `ready` deltaP `-5.1951` edge `6.7354` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `17.598` n `86` status `ready` deltaP `41.2346` edge `1.2211` maxDD `-1.3601`
- `market_context_high->equity_24h` score `10.6311` n `86` status `ready` deltaP `22.1455` edge `1.014` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5862` n `108` status `ready` deltaP `21.189` edge `0.4629` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9865` n `86` status `ready` deltaP `44.0326` edge `0.1403` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `1.6407` n `86` status `ready` deltaP `19.0797` edge `0.0684` maxDD `-0.3766`
- `market_context_high->metal_4h` score `1.3807` n `86` status `ready` deltaP `17.2114` edge `0.0428` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.89` n `108` status `ready` deltaP `9.1761` edge `0.1084` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.6999` n `86` status `ready` deltaP `10.2353` edge `0.0191` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.6119` n `86` status `ready` deltaP `13.2303` edge `0.0019` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4643` n `86` status `ready` deltaP `11.708` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.3834` n `86` status `ready` deltaP `-0.1524` edge `0.1895` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.3353` n `86` status `ready` deltaP `3.7878` edge `0.1053` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.1146` n `86` status `ready` deltaP `6.2631` edge `0.0757` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3625` n `86` status `ready` deltaP `-1.6572` edge `0.016` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4293` n `86` status `ready` deltaP `-0.1497` edge `0.0018` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-0.6089` n `86` status `ready` deltaP `5.6443` edge `0.149` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.715` n `108` status `ready` deltaP `3.554` edge `-0.0033` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

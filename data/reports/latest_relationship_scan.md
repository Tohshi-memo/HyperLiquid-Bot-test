# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T04:07:26.471802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9272`

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

- `news_risk_high->crypto_major_24h` score `24.6209` n `98` status `ready` deltaP `12.7906` edge `2.6523` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.5884` n `98` status `ready` deltaP `13.7046` edge `2.0291` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `6.0871` n `54` status `ready` deltaP `0.8468` edge `0.5166` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.7062` n `101` status `ready` deltaP `20.7483` edge `0.3748` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8703` n `101` status `ready` deltaP `20.5958` edge `0.311` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7941` n `101` status `ready` deltaP `16.6805` edge `0.1682` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1647` n `101` status `ready` deltaP `18.6266` edge `0.1085` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1013` n `98` status `ready` deltaP `22.6013` edge `0.1211` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0548` n `58` status `ready` deltaP `7.8051` edge `0.0612` maxDD `-0.36`
- `market_context_high->index_1h` score `0.867` n `58` status `ready` deltaP `12.3735` edge `0.0153` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.4612` n `101` status `ready` deltaP `15.7268` edge `0.039` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3919` n `54` status `ready` deltaP `15.56` edge `0.0102` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.3669` n `58` status `ready` deltaP `6.4475` edge `0.0184` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3067` n `58` status `ready` deltaP `8.3265` edge `0.0057` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1651` n `101` status `ready` deltaP `8.1834` edge `0.0228` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.02` n `101` status `ready` deltaP `3.4179` edge `0.0161` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1202` n `58` status `ready` deltaP `-1.1924` edge `0.0698` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.164` n `54` status `ready` deltaP `4.0764` edge `-0.0034` maxDD `-0.5838`
- `news_risk_high->equity_24h` score `-0.1643` n `98` status `ready` deltaP `13.446` edge `0.0376` maxDD `-4.941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

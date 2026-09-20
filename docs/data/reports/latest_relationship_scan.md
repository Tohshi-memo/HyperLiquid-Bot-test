# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T13:37:26.731420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `21.9036` n `98` status `ready` deltaP `7.235` edge `2.4629` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.9813` n `98` status `ready` deltaP `14.7463` edge `2.0549` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `17.4283` n `60` status `ready` deltaP `1.4024` edge `1.458` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9861` n `101` status `ready` deltaP `23.1873` edge `0.4652` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.2384` n `49` status `ready` deltaP `28.8974` edge `0.2964` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.4839` n `101` status `ready` deltaP `21.8154` edge `0.354` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3788` n `60` status `ready` deltaP `38.628` edge `0.1207` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.1241` n `101` status `ready` deltaP `16.9799` edge `0.1937` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2727` n `101` status `ready` deltaP `18.6266` edge `0.1175` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.6335` n `60` status `ready` deltaP `22.2357` edge `0.0094` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.6325` n `49` status `ready` deltaP `18.9661` edge `0.0138` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3793` n `60` status `ready` deltaP `15.7884` edge `0.0372` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0417` n `98` status `ready` deltaP `22.775` edge `0.1123` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7579` n `60` status `ready` deltaP `11.8763` edge `0.0056` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.6917` n `98` status `ready` deltaP `16.571` edge `0.0881` maxDD `-4.941`
- `news_risk_high->metal_4h` score `0.664` n `101` status `ready` deltaP `17.5561` edge `0.0437` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6544` n `101` status `ready` deltaP `14.8974` edge `0.0154` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.2815` n `60` status `ready` deltaP `7.8842` edge `0.0059` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2788` n `98` status `ready` deltaP `15.5046` edge `0.0168` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2233` n `101` status `ready` deltaP `5.2143` edge `0.0244` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

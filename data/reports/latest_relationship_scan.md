# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T03:37:28.571342+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.7073` n `98` status `ready` deltaP `12.7906` edge `2.6595` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.7925` n `98` status `ready` deltaP `14.0519` edge `2.0438` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.7496` n `101` status `ready` deltaP `20.9007` edge `0.3774` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8485` n `101` status `ready` deltaP `20.4434` edge `0.3102` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8217` n `101` status `ready` deltaP `16.6805` edge `0.1705` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1491` n `101` status `ready` deltaP `18.4769` edge `0.1082` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0865` n `98` status `ready` deltaP `22.6013` edge `0.1192` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0692` n `58` status `ready` deltaP `7.9548` edge `0.0614` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8921` n `58` status `ready` deltaP `12.6729` edge `0.0154` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.466` n `101` status `ready` deltaP `15.7268` edge `0.0394` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.355` n `52` status `ready` deltaP `14.939` edge `0.0096` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3199` n `58` status `ready` deltaP `8.4762` edge `0.0058` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1505` n `101` status `ready` deltaP `8.0309` edge `0.0226` maxDD `-0.421`
- `market_context_high->fx_4h` score `0.0406` n `52` status `ready` deltaP `6.2031` edge `-0.0011` maxDD `-0.4701`
- `news_risk_high->equity_1h` score `-0.0057` n `101` status `ready` deltaP `3.5676` edge `0.0163` maxDD `-0.9112`
- `news_risk_high->equity_24h` score `-0.0849` n `98` status `ready` deltaP `13.7932` edge `0.0419` maxDD `-4.941`
- `market_context_high->crypto_major_1h` score `-0.1358` n `58` status `ready` deltaP `-1.3421` edge `0.0695` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2292` n `101` status `ready` deltaP `2.8428` edge `0.0063` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T03:22:30.732518+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9248`

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

- `news_risk_high->crypto_major_24h` score `24.7565` n `98` status `ready` deltaP `12.7906` edge `2.6636` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.894` n `98` status `ready` deltaP `14.2255` edge `2.0511` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.7628` n `101` status `ready` deltaP `20.9007` edge `0.3785` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8509` n `101` status `ready` deltaP `20.4434` edge `0.3104` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8409` n `101` status `ready` deltaP `16.6805` edge `0.1721` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1515` n `101` status `ready` deltaP `18.4769` edge `0.1084` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.0848` n `58` status `ready` deltaP `8.1045` edge `0.0617` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `1.0779` n `98` status `ready` deltaP `22.6013` edge `0.1181` maxDD `-3.4467`
- `market_context_high->index_1h` score `0.9053` n `58` status `ready` deltaP `12.8226` edge `0.0155` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.4806` n `101` status `ready` deltaP `15.8793` edge `0.0396` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.3327` n `51` status `ready` deltaP `14.6013` edge `0.009` maxDD `-1.0949`
- `market_context_high->fx_1h` score `0.3199` n `58` status `ready` deltaP `8.4762` edge `0.0058` maxDD `-0.1854`
- `market_context_high->fx_4h` score `0.1553` n `51` status `ready` deltaP `7.4097` edge `0.0005` maxDD `-0.3994`
- `news_risk_high->fx_4h` score `0.1505` n `101` status `ready` deltaP `8.0309` edge `0.0226` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.0099` n `101` status `ready` deltaP `3.7173` edge `0.0166` maxDD `-0.9112`
- `news_risk_high->equity_24h` score `-0.0446` n `98` status `ready` deltaP `13.9668` edge `0.0441` maxDD `-4.941`
- `market_context_high->crypto_major_1h` score `-0.1334` n `58` status `ready` deltaP `-1.3421` edge `0.0697` maxDD `-2.7494`
- `news_risk_high->metal_24h` score `-0.2171` n `98` status `ready` deltaP `11.3379` edge `-0.019` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

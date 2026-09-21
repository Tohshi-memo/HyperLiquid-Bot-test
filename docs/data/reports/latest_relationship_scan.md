# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T02:37:28.745601+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9166`

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

- `news_risk_high->crypto_major_24h` score `24.8789` n `98` status `ready` deltaP `12.7906` edge `2.6738` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.1505` n `98` status `ready` deltaP `14.7463` edge `2.069` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.8002` n `101` status `ready` deltaP `21.0532` edge `0.3806` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8641` n `101` status `ready` deltaP `20.4434` edge `0.3115` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9153` n `101` status `ready` deltaP `17.1296` edge `0.1753` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1743` n `101` status `ready` deltaP `18.6266` edge `0.1093` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.1171` n `58` status `ready` deltaP `8.4039` edge `0.0624` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `1.0529` n `98` status `ready` deltaP `22.6013` edge `0.1149` maxDD `-3.4467`
- `market_context_high->index_1h` score `0.9436` n `58` status `ready` deltaP `13.2717` edge `0.0157` maxDD `-0.0435`
- `market_context_high->fx_4h` score `0.6457` n `48` status `ready` deltaP `11.3313` edge `0.0065` maxDD `-0.2586`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.4854` n `101` status `ready` deltaP `15.8793` edge `0.04` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3199` n `58` status `ready` deltaP `8.4762` edge `0.0058` maxDD `-0.1854`
- `market_context_high->index_4h` score `0.2526` n `48` status `ready` deltaP `13.4655` edge `0.0063` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.1457` n `101` status `ready` deltaP `8.0309` edge `0.0222` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.0679` n `98` status `ready` deltaP `14.4876` edge `0.05` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.0423` n `101` status `ready` deltaP `4.0167` edge `0.0173` maxDD `-0.9112`
- `market_context_high->metal_4h` score `-0.0887` n `48` status `ready` deltaP `1.626` edge `0.0214` maxDD `-0.5038`
- `market_context_high->crypto_major_1h` score `-0.1106` n `58` status `ready` deltaP `-1.1924` edge `0.0706` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

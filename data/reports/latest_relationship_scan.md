# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T02:22:26.945130+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.8885` n `98` status `ready` deltaP `12.7906` edge `2.6746` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.1932` n `98` status `ready` deltaP `14.9199` edge `2.0714` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.7748` n `101` status `ready` deltaP `20.9007` edge `0.3795` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8641` n `101` status `ready` deltaP `20.4434` edge `0.3115` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8889` n `101` status `ready` deltaP `16.9799` edge `0.1741` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1479` n `101` status `ready` deltaP `18.4769` edge `0.1081` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.1135` n `58` status `ready` deltaP `8.4039` edge `0.0621` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `1.0345` n `98` status `ready` deltaP `22.4277` edge `0.1137` maxDD `-3.4467`
- `market_context_high->index_1h` score `0.9448` n `58` status `ready` deltaP `13.2717` edge `0.0158` maxDD `-0.0435`
- `market_context_high->fx_4h` score `0.7784` n `47` status `ready` deltaP `12.7497` edge `0.0081` maxDD `-0.2586`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.5` n `101` status `ready` deltaP `16.0317` edge `0.0402` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3187` n `58` status `ready` deltaP `8.4762` edge `0.0057` maxDD `-0.1854`
- `market_context_high->index_4h` score `0.2235` n `47` status `ready` deltaP `13.0416` edge `0.0054` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.1445` n `101` status `ready` deltaP `8.0309` edge `0.0221` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.0949` n `98` status `ready` deltaP `14.6612` edge `0.0511` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.0387` n `101` status `ready` deltaP `4.0167` edge `0.017` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.137` n `58` status `ready` deltaP `-1.3421` edge `0.0694` maxDD `-2.7494`
- `market_context_high->metal_4h` score `-0.1485` n `47` status `ready` deltaP `0.7589` edge `0.0222` maxDD `-0.5038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

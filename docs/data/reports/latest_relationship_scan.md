# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T23:52:25.979129+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.7865` n `98` status `ready` deltaP `12.7906` edge `2.6661` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3103` n `98` status `ready` deltaP `15.0935` edge `2.08` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6652` n `101` status `ready` deltaP `20.5958` edge `0.3724` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8365` n `101` status `ready` deltaP `20.4434` edge `0.3092` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7677` n `101` status `ready` deltaP `16.6805` edge `0.166` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0592` n `101` status `ready` deltaP `18.1775` edge `0.1027` maxDD `-2.8494`
- `market_context_high->fx_1h` score `1.0573` n `51` status `ready` deltaP `14.4359` edge `0.0098` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9818` n `98` status `ready` deltaP `22.2541` edge `0.1081` maxDD `-3.4467`
- `market_context_high->commodity_4h` score `0.6821` n `43` status `ready` deltaP `22.8552` edge `-0.0008` maxDD `-2.1296`
- `news_risk_high->metal_1h` score `0.6592` n `101` status `ready` deltaP `15.0471` edge `0.0148` maxDD `-0.8144`
- `market_context_high->fx_4h` score `0.619` n `43` status `ready` deltaP `10.848` edge `0.0075` maxDD `-0.2586`
- `news_risk_high->metal_4h` score `0.5972` n `101` status `ready` deltaP `16.9464` edge `0.0422` maxDD `-2.0994`
- `market_context_high->index_1h` score `0.5566` n `51` status `ready` deltaP `8.6885` edge `0.014` maxDD `-0.0435`
- `news_risk_high->equity_24h` score `0.2446` n `98` status `ready` deltaP `15.1821` edge `0.0601` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2371` n `101` status `ready` deltaP `9.098` edge `0.0227` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.154` n `51` status `ready` deltaP `3.584` edge `0.0264` maxDD `-0.7775`
- `news_risk_high->equity_1h` score `0.059` n `101` status `ready` deltaP `4.1664` edge `0.0177` maxDD `-0.9112`
- `market_context_high->index_4h` score `0.0145` n `43` status `ready` deltaP `10.9259` edge `-0.0073` maxDD `-1.0949`
- `news_risk_high->metal_24h` score `-0.021` n `98` status `ready` deltaP `13.5948` edge `-0.0089` maxDD `-2.4203`
- `market_context_high->metal_1h` score `-0.0276` n `51` status `ready` deltaP `2.6418` edge `0.0124` maxDD `-0.2519`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

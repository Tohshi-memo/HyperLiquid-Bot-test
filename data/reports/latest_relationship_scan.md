# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T10:22:33.841617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.8213` n `58` status `ready` deltaP `1.23` edge `2.7419` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.9778` n `101` status `ready` deltaP `9.7067` edge `2.4526` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `16.5201` n `101` status `ready` deltaP `10.0918` edge `1.7975` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.8079` n `101` status `ready` deltaP `17.3946` edge `0.3223` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.4847` n `101` status `ready` deltaP `20.291` edge `0.2809` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5112` n `101` status `ready` deltaP `15.3332` edge `0.1536` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8781` n `101` status `ready` deltaP `17.2793` edge `0.0936` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.221` n `101` status `ready` deltaP `23.7177` edge `0.129` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8031` n `58` status `ready` deltaP `6.0087` edge `0.0522` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6825` n `58` status `ready` deltaP `10.2777` edge `0.0139` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5598` n `101` status `ready` deltaP `14.1489` edge `0.0125` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3846` n `58` status `ready` deltaP `9.2247` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3525` n `101` status `ready` deltaP `10.1651` edge `0.0252` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2993` n `101` status `ready` deltaP `14.8122` edge `0.0316` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2878` n `58` status `ready` deltaP `14.1716` edge `0.0061` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2818` n `58` status `ready` deltaP `5.699` edge `0.0163` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1645` n `101` status `ready` deltaP `3.5913` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2718` n `101` status `ready` deltaP `1.6215` edge `0.0071` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.4068` n `58` status `ready` deltaP `-2.5397` edge `0.0549` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.4069` n `58` status `ready` deltaP `1.9712` edge `-0.0029` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

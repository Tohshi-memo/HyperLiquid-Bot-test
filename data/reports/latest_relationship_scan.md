# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T14:52:29.795532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_4h` score `30.7897` n `58` status `ready` deltaP `1.23` edge `2.5726` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `19.152` n `101` status `ready` deltaP `6.7553` edge `2.2368` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `13.158` n `101` status `ready` deltaP `7.1404` edge `1.537` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4529` n `101` status `ready` deltaP `16.6324` edge `0.2978` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1579` n `101` status `ready` deltaP `19.9861` edge `0.2557` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4212` n `101` status `ready` deltaP `14.8841` edge `0.1491` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7715` n `101` status `ready` deltaP `16.5308` edge `0.0897` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.438` n `101` status `ready` deltaP `24.4121` edge `0.1522` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7384` n `58` status `ready` deltaP `5.2602` edge `0.0518` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5771` n `58` status `ready` deltaP `9.0801` edge `0.0131` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.513` n `101` status `ready` deltaP `13.5501` edge `0.0126` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3965` n `58` status `ready` deltaP `9.3744` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3101` n `101` status `ready` deltaP `14.8122` edge `0.0325` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.2635` n `101` status `ready` deltaP `9.098` edge `0.0249` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2592` n `58` status `ready` deltaP `13.5618` edge `0.0065` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2351` n `58` status `ready` deltaP `5.1002` edge `0.0164` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1525` n `101` status `ready` deltaP `3.741` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3364` n `101` status `ready` deltaP `0.873` edge `0.0067` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `-0.4643` n `101` status `ready` deltaP `8.9091` edge `-0.0345` maxDD `-2.4203`
- `market_context_high->fx_4h` score `-0.4647` n `58` status `ready` deltaP `0.9041` edge `-0.0032` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

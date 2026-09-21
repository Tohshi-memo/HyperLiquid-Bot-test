# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T18:52:30.583415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `28.5087` n `58` status `ready` deltaP `1.3825` edge `2.3815` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `16.213` n `101` status `ready` deltaP `3.9776` edge `2.0104` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `10.519` n `101` status `ready` deltaP `4.3626` edge `1.3356` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7167` n `101` status `ready` deltaP `17.3946` edge `0.3147` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1283` n `101` status `ready` deltaP `19.3763` edge `0.2573` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6131` n `101` status `ready` deltaP `15.932` edge `0.1581` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `1.9015` n `101` status `ready` deltaP `27.1899` edge `0.1931` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.8949` n `101` status `ready` deltaP `17.429` edge `0.094` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.6557` n `58` status `ready` deltaP `4.6614` edge `0.0489` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5262` n `101` status `ready` deltaP `13.6998` edge `0.0127` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5088` n `58` status `ready` deltaP `8.3316` edge `0.0124` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3415` n `101` status `ready` deltaP `10.0126` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2941` n `101` status `ready` deltaP `14.5073` edge `0.0332` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2483` n `58` status `ready` deltaP `5.2499` edge `0.0165` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1085` n `58` status `ready` deltaP `11.5801` edge `0.0004` maxDD `-1.0949`
- `market_context_high->index_24h` score `0.095` n `37` status `ready` deltaP `-6.935` edge `0.1373` maxDD `-1.644`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.3162` n `37` status `ready` deltaP `9.6049` edge `-0.067` maxDD `-0.2042`
- `market_context_high->crypto_major_1h` score `-0.39` n `58` status `ready` deltaP `-2.39` edge `0.0553` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T23:22:30.755155+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9916`

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

- `market_context_high->unknown_4h` score `25.3481` n `58` status `ready` deltaP `2.4496` edge `2.111` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `11.8878` n `101` status `ready` deltaP `0.8526` edge `1.6708` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `7.2006` n `101` status `ready` deltaP `1.2376` edge `1.0799` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.2406` n `101` status `ready` deltaP `15.7178` edge `0.2862` maxDD `-7.675`
- `market_context_high->crypto_major_24h` score `3.2017` n `51` status `ready` deltaP `3.1046` edge `1.0556` maxDD `-48.5989`
- `market_context_high->equity_24h` score `2.9223` n `51` status `ready` deltaP `-3.6663` edge `0.5477` maxDD `-17.7117`
- `news_risk_high->commodity_24h` score `2.4173` n `101` status `ready` deltaP `30.3149` edge `0.2384` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3817` n `101` status `ready` deltaP `14.5847` edge `0.1478` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.2576` n `101` status `ready` deltaP `16.9373` edge `0.201` maxDD `-8.0625`
- `market_context_high->index_24h` score `1.6367` n `51` status `ready` deltaP `0.3268` edge `0.2131` maxDD `-1.644`
- `news_risk_high->crypto_major_1h` score `1.6036` n `101` status `ready` deltaP `15.932` edge `0.0797` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.5994` n `58` status `ready` deltaP `4.2123` edge `0.0472` maxDD `-0.36`
- `market_context_high->index_1h` score `0.4944` n `58` status `ready` deltaP `8.1819` edge `0.0122` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4708` n `58` status `ready` deltaP `10.2726` edge `0.0064` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.4546` n `101` status `ready` deltaP `11.2322` edge `0.0266` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4531` n `101` status `ready` deltaP `12.9513` edge `0.0116` maxDD `-0.8144`
- `market_context_high->metal_24h` score `0.2749` n `51` status `ready` deltaP `17.0241` edge `-0.0672` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1943` n `101` status `ready` deltaP `13.4403` edge `0.032` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.1752` n `58` status `ready` deltaP `4.5014` edge `0.0154` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.0879` n `58` status `ready` deltaP `11.1228` edge `0.0008` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

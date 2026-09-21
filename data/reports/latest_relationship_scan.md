# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T22:22:33.241125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.2441` n `58` status `ready` deltaP `1.8398` edge `2.1064` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `12.8074` n `101` status `ready` deltaP `1.547` edge `1.7428` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `7.9138` n `101` status `ready` deltaP `1.932` edge `1.1347` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.389` n `101` status `ready` deltaP `16.3276` edge `0.2945` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.4524` n `101` status `ready` deltaP `15.0338` edge `0.1507` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.4336` n `101` status `ready` deltaP `17.5471` edge `0.2116` maxDD `-8.0625`
- `news_risk_high->commodity_24h` score `2.3173` n `101` status `ready` deltaP `29.6204` edge `0.2302` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.6767` n `101` status `ready` deltaP `16.3811` edge `0.0828` maxDD `-2.8494`
- `market_context_high->crypto_major_24h` score `1.4557` n `47` status `ready` deltaP `1.4628` edge `0.8427` maxDD `-48.5989`
- `market_context_high->index_24h` score `1.3362` n `47` status `ready` deltaP `-1.315` edge `0.199` maxDD `-1.644`
- `market_context_high->equity_24h` score `1.205` n `47` status `ready` deltaP `-5.308` edge `0.4696` maxDD `-17.7117`
- `market_context_high->equity_1h` score `0.6186` n `58` status `ready` deltaP `4.362` edge `0.0478` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.513` n `101` status `ready` deltaP `13.5501` edge `0.0126` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4956` n `58` status `ready` deltaP `8.1819` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4325` n `58` status `ready` deltaP `9.8235` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3974` n `101` status `ready` deltaP `10.6224` edge `0.0259` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2351` n `58` status `ready` deltaP `5.1002` edge `0.0164` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.1919` n `101` status `ready` deltaP `13.4403` edge `0.0318` maxDD `-2.0994`
- `market_context_high->metal_24h` score `0.1258` n `47` status `ready` deltaP `15.3553` edge `-0.0685` maxDD `-0.2042`
- `market_context_high->index_4h` score `0.0832` n `58` status `ready` deltaP `11.1228` edge `0.0002` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

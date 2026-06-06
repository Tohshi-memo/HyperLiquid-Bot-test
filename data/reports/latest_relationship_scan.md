# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T19:37:27.447541+00:00`
- Price records: `672`
- Market context records: `3105`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.6295` n `85` status `ready` deltaP `14.808` edge `2.5643` maxDD `-33.816`
- `market_context_high->commodity_24h` score `14.9944` n `85` status `ready` deltaP `45.4882` edge `0.9891` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.6884` n `85` status `ready` deltaP `23.75` edge `1.1145` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.4465` n `85` status `ready` deltaP `31.8525` edge `0.9102` maxDD `-15.8276`
- `market_context_high->equity_24h` score `7.1103` n `85` status `ready` deltaP `17.5245` edge `1.3609` maxDD `-38.6259`
- `market_context_high->commodity_4h` score `2.9978` n `120` status `ready` deltaP `17.9878` edge `0.1757` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.1931` n `123` status `ready` deltaP `0.3858` edge `0.0236` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4996` n `123` status `ready` deltaP `3.9786` edge `0.0157` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6136` n `85` status `ready` deltaP `3.5743` edge `-0.0022` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.751` n `123` status `ready` deltaP `-7.7881` edge `-0.0045` maxDD `-0.5225`
- `market_context_high->crypto_alt_1h` score `-0.7641` n `123` status `ready` deltaP `3.465` edge `0.0919` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.2334` n `123` status `ready` deltaP `-1.7331` edge `0.002` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.2853` n `120` status `ready` deltaP `-11.6565` edge `-0.0027` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.462` n `120` status `ready` deltaP `9.0244` edge `0.0433` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.874` n `120` status `ready` deltaP `4.8984` edge `0.0129` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.2416` n `123` status `ready` deltaP `-1.351` edge `0.0485` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3759` n `123` status `ready` deltaP `-7.0834` edge `-0.0114` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-3.1096` n `123` status `ready` deltaP `2.5693` edge `-0.077` maxDD `-13.9411`
- `market_context_high->crypto_alt_4h` score `-3.936` n `120` status `ready` deltaP `12.2053` edge `0.2185` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0664` n `120` status `ready` deltaP `5.9146` edge `-0.0302` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

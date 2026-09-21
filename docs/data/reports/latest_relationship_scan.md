# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T18:37:28.632385+00:00`
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

- `market_context_high->unknown_4h` score `28.4653` n `58` status `ready` deltaP `1.23` edge `2.3789` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `16.4609` n `101` status `ready` deltaP `4.1512` edge `2.0299` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `10.7261` n `101` status `ready` deltaP `4.5362` edge `1.3517` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7191` n `101` status `ready` deltaP `17.3946` edge `0.3149` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1669` n `101` status `ready` deltaP `19.5288` edge `0.2595` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.643` n `101` status `ready` deltaP `16.0817` edge `0.1596` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9285` n `101` status `ready` deltaP `17.5787` edge `0.0958` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.8706` n `101` status `ready` deltaP `27.0163` edge `0.1903` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.6809` n `58` status `ready` deltaP `4.8111` edge `0.05` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.543` n `101` status `ready` deltaP `13.8495` edge `0.0131` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5232` n `58` status `ready` deltaP `8.4813` edge `0.0126` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3293` n `101` status `ready` deltaP `9.8602` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3087` n `101` status `ready` deltaP `14.6598` edge `0.0334` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2651` n `58` status `ready` deltaP `5.3996` edge `0.0169` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1196` n `58` status `ready` deltaP `11.7325` edge `0.0008` maxDD `-1.0949`
- `market_context_high->index_24h` score `0.1158` n `37` status `ready` deltaP `-6.7614` edge `0.1388` maxDD `-1.644`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.3174` n `37` status `ready` deltaP `9.6049` edge `-0.0671` maxDD `-0.2042`
- `market_context_high->crypto_major_1h` score `-0.3564` n `58` status `ready` deltaP `-2.2403` edge `0.0571` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

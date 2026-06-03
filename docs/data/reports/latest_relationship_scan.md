# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T01:07:23.408971+00:00`
- Price records: `672`
- Market context records: `2716`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.0683` n `111` status `ready` deltaP `16.3523` edge `1.1627` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5935` n `111` status `ready` deltaP `16.9576` edge `0.6359` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8564` n `143` status `ready` deltaP `6.0965` edge `0.1357` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.609` n `111` status `ready` deltaP `6.5175` edge `0.7909` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2239` n `143` status `ready` deltaP `11.6184` edge `0.0354` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1378` n `143` status `ready` deltaP `3.4997` edge `0.0084` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2422` n `143` status `ready` deltaP `2.4497` edge `0.0363` maxDD `-3.1587`
- `market_context_high->crypto_alt_4h` score `-0.4273` n `143` status `ready` deltaP `16.2108` edge `0.2904` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4308` n `143` status `ready` deltaP `0.7004` edge `0.0038` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.4782` n `143` status `ready` deltaP `1.6991` edge `0.0027` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.491` n `143` status `ready` deltaP `6.5942` edge `0.0691` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7146` n `143` status `ready` deltaP `-0.9506` edge `-0.0007` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.8442` n `111` status `ready` deltaP `3.8758` edge `-0.009` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.924` n `143` status `ready` deltaP `-1.3539` edge `0.0099` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.944` n `143` status `ready` deltaP `3.6473` edge `0.0416` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1948` n `143` status `ready` deltaP `-4.1863` edge `0.0122` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2465` n `143` status `ready` deltaP `2.5808` edge `0.015` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.3393` n `111` status `ready` deltaP `4.3169` edge `0.1089` maxDD `-12.4171`
- `market_context_high->index_24h` score `-1.7635` n `111` status `ready` deltaP `0.1971` edge `-0.0502` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9705` n `143` status `ready` deltaP `-0.7291` edge `-0.0189` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

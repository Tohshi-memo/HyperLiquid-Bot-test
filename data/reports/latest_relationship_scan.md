# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T11:22:25.624931+00:00`
- Price records: `672`
- Market context records: `3172`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.8979` n `101` status `ready` deltaP `47.2171` edge `0.8862` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0096` n `101` status `ready` deltaP `20.2643` edge `0.9145` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.5863` n `101` status `ready` deltaP `14.5851` edge `2.3858` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1828` n `101` status `ready` deltaP `29.2216` edge `0.8533` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4908` n `101` status `ready` deltaP `13.1498` edge `1.3297` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1064` n `134` status `ready` deltaP `19.6601` edge `0.1736` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7512` n `101` status `ready` deltaP `12.3539` edge `0.003` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2993` n `137` status `ready` deltaP `5.3248` edge `0.0317` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.183` n `134` status `ready` deltaP `11.0506` edge `0.1638` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.3842` n `137` status `ready` deltaP `5.6427` edge `0.0194` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.444` n `137` status `ready` deltaP `5.6613` edge `0.1183` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.9318` n `134` status `ready` deltaP `15.4714` edge `0.0683` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.073` n `137` status `ready` deltaP `2.7033` edge `0.0707` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.3306` n `137` status `ready` deltaP `3.7338` edge `0.0128` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3465` n `134` status `ready` deltaP `-11.5876` edge `-0.0069` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6086` n `137` status `ready` deltaP `-9.0684` edge `-0.0052` maxDD `-0.8046`
- `market_context_high->metal_1h` score `-2.1178` n `137` status `ready` deltaP `-4.2769` edge `-0.0086` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1677` n `134` status `ready` deltaP `17.9651` edge `0.4068` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.9983` n `137` status `ready` deltaP `2.8924` edge `-0.0665` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6308` n `134` status `ready` deltaP `10.9028` edge `0.2542` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

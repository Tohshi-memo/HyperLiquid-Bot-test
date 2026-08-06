# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T15:08:09.077075+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11797`

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

- `market_context_high->unknown_24h` score `27.5817` n `102` status `ready` deltaP `3.8807` edge `2.2769` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.2304` n `102` status `ready` deltaP `4.33` edge `0.1905` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0718` n `113` status `ready` deltaP `12.8912` edge `0.088` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5236` n `102` status `ready` deltaP `21.2112` edge `0.0463` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3865` n `116` status `ready` deltaP `7.3818` edge `0.0246` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0744` n `116` status `ready` deltaP `7.2373` edge `-0.0037` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2978` n `113` status `ready` deltaP `7.247` edge `-0.0005` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.496` n `116` status `ready` deltaP `-1.3421` edge `-0.0052` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.636` n `116` status `ready` deltaP `-2.0906` edge `-0.0142` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7684` n `113` status `ready` deltaP `2.6778` edge `0.0071` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7988` n `116` status `ready` deltaP `-3.1437` edge `-0.0104` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.0868` n `113` status `ready` deltaP `3.9229` edge `-0.0265` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.28` n `102` status `ready` deltaP `-4.2484` edge `0.0837` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3561` n `116` status `ready` deltaP `3.4225` edge `-0.0402` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.668` n `113` status `ready` deltaP `-7.3656` edge `-0.0393` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.7223` n `116` status `ready` deltaP `-7.6089` edge `-0.0388` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.8055` n `102` status `ready` deltaP `-4.9632` edge `-0.0564` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1777` n `113` status `ready` deltaP `0.2348` edge `-0.2647` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3741` n `102` status `ready` deltaP `9.0482` edge `-0.001` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3584` n `113` status `ready` deltaP `-6.1205` edge `-0.1512` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T20:22:30.618828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.2697` n `96` status `ready` deltaP `11.4583` edge `0.2016` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8332` n `96` status `ready` deltaP `15.0013` edge `0.0829` maxDD `-0.4112`
- `market_context_high->index_1h` score `1.0001` n `96` status `ready` deltaP `16.6604` edge `0.011` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5124` n `96` status `ready` deltaP `13.2113` edge `0.0122` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2662` n `96` status `ready` deltaP `9.4766` edge `0.0245` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2574` n `96` status `ready` deltaP `6.4236` edge `0.1735` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.1582` n `96` status `ready` deltaP `17.8819` edge `-0.0554` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0383` n `96` status `ready` deltaP `7.4949` edge `0.0052` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.0553` n `96` status `ready` deltaP `6.6617` edge `-0.0263` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1089` n `96` status `ready` deltaP `3.7238` edge `0.0048` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6731` n `96` status `ready` deltaP `-0.94` edge `0.005` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7385` n `96` status `ready` deltaP `-0.1684` edge `-0.0134` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7869` n `96` status `ready` deltaP `1.4845` edge `-0.0263` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8705` n `96` status `ready` deltaP `-7.4414` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->crypto_major_24h` score `-0.8737` n `96` status `ready` deltaP `2.9514` edge `0.0283` maxDD `-4.9964`
- `market_context_high->crypto_major_4h` score `-1.1875` n `96` status `ready` deltaP `6.2754` edge `-0.0387` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.5042` n `96` status `ready` deltaP `4.1159` edge `-0.0258` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.9922` n `96` status `ready` deltaP `-8.8542` edge `0.0062` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.4715` n `96` status `ready` deltaP `-18.4027` edge `-0.0083` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

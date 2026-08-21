# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T11:07:29.586677+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.5247` n `113` status `ready` deltaP `10.2472` edge `0.0569` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3862` n `113` status `ready` deltaP `11.1984` edge `0.0063` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.1238` n `105` status `ready` deltaP `8.705` edge `0.0081` maxDD `-0.3539`
- `market_context_high->equity_4h` score `-0.0191` n `105` status `ready` deltaP `4.2828` edge `0.1328` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.0237` n `113` status `ready` deltaP `4.132` edge `0.0053` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2554` n `105` status `ready` deltaP `6.5302` edge `-0.0187` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3106` n `105` status `ready` deltaP `5.2759` edge `0.0174` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.335` n `113` status `ready` deltaP `0.416` edge `-0.0061` maxDD `-0.503`
- `market_context_high->unknown_1h` score `-0.4375` n `113` status `ready` deltaP `9.3093` edge `-0.0758` maxDD `-0.4843`
- `market_context_high->commodity_24h` score `-0.4583` n `105` status `ready` deltaP `4.4147` edge `0.1157` maxDD `-4.666`
- `market_context_high->commodity_1h` score `-0.6419` n `113` status `ready` deltaP `-4.185` edge `0.0022` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7931` n `105` status `ready` deltaP `-3.2622` edge `0.0051` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.1073` n `113` status `ready` deltaP `-2.2919` edge `-0.0422` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-1.2696` n `113` status `ready` deltaP `-2.1951` edge `-0.011` maxDD `-2.413`
- `market_context_high->fx_24h` score `-3.1983` n `105` status `ready` deltaP `-14.2113` edge `-0.0108` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.5828` n `105` status `ready` deltaP `-1.5113` edge `-0.1615` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.9113` n `105` status `ready` deltaP `0.1278` edge `-0.2247` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0517` n `105` status `ready` deltaP `-3.8592` edge `-0.0435` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.3508` n `105` status `ready` deltaP `10.0298` edge `-0.3788` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.367` n `105` status `ready` deltaP `-16.7212` edge `-0.1176` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

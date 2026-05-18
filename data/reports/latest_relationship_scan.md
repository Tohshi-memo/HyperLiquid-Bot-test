# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T21:52:16.485571+00:00`
- Price records: `672`
- Market context records: `1158`
- Flow alert records: `5235`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.4522` n `145` status `ready` deltaP `44.8108` edge `1.5188` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.0124` n `145` status `ready` deltaP `21.1949` edge `0.8947` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7787` n `145` status `ready` deltaP `20.6741` edge `0.6034` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.049` n `145` status `ready` deltaP `19.2852` edge `0.4313` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5738` n `145` status `ready` deltaP `-2.6246` edge `0.6487` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4534` n `161` status `ready` deltaP `12.1317` edge `0.1899` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1593` n `161` status `ready` deltaP `9.1671` edge `0.1038` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4728` n `161` status `ready` deltaP `7.379` edge `0.0219` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3155` n `161` status `ready` deltaP `3.0535` edge `0.0437` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1701` n `161` status `ready` deltaP `8.3738` edge `0.1581` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1323` n `161` status `ready` deltaP `8.3693` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0253` n `161` status `ready` deltaP `7.0378` edge `0.0329` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.327` n `161` status `ready` deltaP `2.5245` edge `0.0402` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.362` n `161` status `ready` deltaP `6.0411` edge `-0.0094` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.8386` n `161` status `ready` deltaP `-3.2888` edge `-0.0048` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9116` n `161` status `ready` deltaP `-2.2241` edge `-0.0024` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.0278` n `161` status `ready` deltaP `5.6137` edge `0.1273` maxDD `-16.7194`
- `market_context_high->unknown_24h` score `-1.1086` n `145` status `ready` deltaP `3.5668` edge `0.1568` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-1.706` n `161` status `ready` deltaP `6.269` edge `-0.0651` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.0139` n `161` status `ready` deltaP `7.5045` edge `-0.0962` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

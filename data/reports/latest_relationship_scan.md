# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T21:07:26.536590+00:00`
- Price records: `672`
- Market context records: `3006`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `19.9936` n `98` status `ready` deltaP `7.5468` edge `2.0075` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.6016` n `98` status `ready` deltaP `42.6411` edge `0.7769` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.2091` n `98` status `ready` deltaP `19.7846` edge `0.932` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.0811` n `98` status `ready` deltaP `18.5197` edge `0.917` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.2507` n `98` status `ready` deltaP `18.13` edge `0.4981` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.3538` n `104` status `ready` deltaP `17.6947` edge `0.1429` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.7081` n `104` status `ready` deltaP `13.3443` edge `0.1732` maxDD `-11.3767`
- `market_context_high->index_4h` score `0.4515` n `104` status `ready` deltaP `18.1285` edge `0.1033` maxDD `-8.9682`
- `market_context_high->commodity_1h` score `-0.094` n `110` status `ready` deltaP `0.7703` edge `0.02` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.3517` n `110` status `ready` deltaP `4.129` edge `0.0352` maxDD `-5.6254`
- `market_context_high->crypto_alt_4h` score `-0.3696` n `104` status `ready` deltaP `21.7519` edge `0.3624` maxDD `-38.7172`
- `market_context_high->fx_1h` score `-0.4156` n `110` status `ready` deltaP `-2.5667` edge `0.0004` maxDD `-0.2588`
- `market_context_high->index_1h` score `-0.4917` n `110` status `ready` deltaP `3.6255` edge `0.0142` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5903` n `110` status `ready` deltaP `7.2727` edge `0.0888` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-1.0819` n `110` status `ready` deltaP `4.8122` edge `0.0555` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1656` n `104` status `ready` deltaP `-10.5769` edge `-0.0006` maxDD `-0.5987`
- `market_context_high->unknown_1h` score `-1.2942` n `110` status `ready` deltaP `2.3` edge `-0.0501` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-1.4942` n `104` status `ready` deltaP `-1.6768` edge `-0.008` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.8791` n `98` status `ready` deltaP `-6.4803` edge `-0.0262` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-2.0045` n `110` status `ready` deltaP `-3.6799` edge `-0.0107` maxDD `-6.8783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

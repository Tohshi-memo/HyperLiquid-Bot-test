# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T11:07:27.860556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10803`

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

- `market_context_high->equity_4h` score `1.6838` n `99` status `ready` deltaP `9.1017` edge `0.1723` maxDD `-2.7464`
- `market_context_high->metal_4h` score `0.4968` n `99` status `ready` deltaP `13.8273` edge `0.0068` maxDD `-1.273`
- `market_context_high->equity_1h` score `0.4413` n `104` status `ready` deltaP `9.0339` edge `0.0483` maxDD `-2.7401`
- `market_context_high->index_1h` score `0.3447` n `104` status `ready` deltaP `10.1048` edge `0.005` maxDD `-0.4912`
- `market_context_high->index_4h` score `0.0071` n `99` status `ready` deltaP `7.3094` edge `0.0205` maxDD `-0.8243`
- `market_context_high->fx_4h` score `-0.0139` n `99` status `ready` deltaP `6.5657` edge `0.0047` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.0356` n `96` status `ready` deltaP `5.0347` edge `0.1452` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1027` n `104` status `ready` deltaP `3.9959` edge `0.0035` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1794` n `104` status `ready` deltaP `1.3473` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3114` n `104` status `ready` deltaP `7.3008` edge `-0.0519` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.42` n `104` status `ready` deltaP `1.5776` edge `0.0158` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5181` n `104` status `ready` deltaP `2.4989` edge `0.0014` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8057` n `104` status `ready` deltaP `-6.6905` edge `-0.0021` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.8873` n `99` status `ready` deltaP `-4.219` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->unknown_24h` score `-0.9345` n `96` status `ready` deltaP `17.7083` edge `-0.1453` maxDD `-1.0505`
- `market_context_high->crypto_alt_4h` score `-1.7379` n `99` status `ready` deltaP `4.7949` edge `-0.0498` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0983` n `99` status `ready` deltaP `6.6812` edge `-0.1173` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5355` n `96` status `ready` deltaP `-19.0972` edge `-0.009` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7466` n `96` status `ready` deltaP `-0.5209` edge `-0.0601` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.7276` n `96` status `ready` deltaP `-19.0972` edge `-0.148` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T04:52:32.506584+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `81.0744` n `148` status `ready` deltaP `2.5585` edge `6.7727` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `13.5051` n `148` status `ready` deltaP `1.0722` edge `1.1672` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.407` n `148` status `ready` deltaP `12.6401` edge `0.0095` maxDD `-0.4545`
- `market_context_high->index_24h` score `0.3552` n `122` status `ready` deltaP `19.6181` edge `0.0208` maxDD `-3.1501`
- `market_context_high->fx_1h` score `0.3337` n `148` status `ready` deltaP `9.0791` edge `0.0031` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.133` n `122` status `ready` deltaP `21.0898` edge `0.129` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0069` n `148` status `ready` deltaP `9.9692` edge `0.0091` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.0564` n `148` status `ready` deltaP `4.135` edge `0.0178` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1746` n `122` status `ready` deltaP `16.4474` edge `0.0252` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3512` n `148` status `ready` deltaP `6.9339` edge `0.0474` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.6058` n `148` status `ready` deltaP `5.3973` edge `0.0262` maxDD `-7.8544`
- `market_context_high->index_1h` score `-0.6072` n `148` status `ready` deltaP `-0.3803` edge `-0.0016` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.7823` n `148` status `ready` deltaP `9.4512` edge `0.0009` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.6675` n `148` status `ready` deltaP `2.1646` edge `-0.0006` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.8749` n `148` status `ready` deltaP `0.1294` edge `0.0032` maxDD `-12.8878`
- `market_context_high->index_4h` score `-3.4218` n `148` status `ready` deltaP `-6.3448` edge `-0.0266` maxDD `-6.6332`
- `market_context_high->crypto_major_24h` score `-3.8368` n `122` status `ready` deltaP `2.0584` edge `-0.0199` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-3.9043` n `122` status `ready` deltaP `-2.1337` edge `-0.092` maxDD `-23.5461`
- `market_context_high->crypto_major_4h` score `-4.2102` n `148` status `ready` deltaP `0.3914` edge `-0.076` maxDD `-29.9765`
- `market_context_high->equity_4h` score `-6.5661` n `148` status `ready` deltaP `-0.3749` edge `-0.1599` maxDD `-43.3526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

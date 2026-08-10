# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T17:07:30.645897+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->equity_24h` score `1.5021` n `136` status `ready` deltaP `4.8094` edge `0.4065` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.744` n `170` status `ready` deltaP `11.094` edge `0.0595` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.714` n `178` status `ready` deltaP `9.6296` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7047` n `136` status `ready` deltaP `18.7634` edge `0.0144` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1061` n `170` status `ready` deltaP `6.5602` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1438` n `178` status `ready` deltaP `3.9343` edge `0.0005` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.2189` n `136` status `ready` deltaP `4.4258` edge `0.1054` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.569` n `178` status `ready` deltaP `-3.2917` edge `-0.0033` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.7484` n `136` status `ready` deltaP `1.5585` edge `0.0554` maxDD `-2.9193`
- `market_context_high->metal_1h` score `-0.799` n `178` status `ready` deltaP `-4.4893` edge `-0.0089` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.9467` n `178` status `ready` deltaP `-2.5381` edge `-0.0146` maxDD `-4.8543`
- `market_context_high->index_4h` score `-1.2074` n `170` status `ready` deltaP `-1.6302` edge `-0.0115` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.8332` n `178` status `ready` deltaP `-10.5934` edge `-0.0475` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.066` n `170` status `ready` deltaP `-7.4229` edge `-0.039` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.1791` n `170` status `ready` deltaP `-10.9326` edge `-0.1215` maxDD `-8.0556`
- `market_context_high->crypto_major_24h` score `-3.2798` n `136` status `ready` deltaP `1.096` edge `-0.0312` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.8279` n `136` status `ready` deltaP `-10.3477` edge `-0.1057` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.8294` n `170` status `ready` deltaP `-11.3684` edge `-0.1394` maxDD `-15.3937`
- `market_context_high->crypto_major_1h` score `-3.9758` n `178` status `ready` deltaP `-11.2343` edge `-0.066` maxDD `-11.9002`
- `market_context_high->commodity_24h` score `-8.7819` n `136` status `ready` deltaP `-5.3752` edge `-0.2185` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

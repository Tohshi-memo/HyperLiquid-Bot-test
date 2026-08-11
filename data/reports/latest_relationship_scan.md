# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T03:22:25.356738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `26.4672` n `141` status `ready` deltaP `-15.4185` edge `2.5538` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.027` n `141` status `ready` deltaP `19.7021` edge `0.035` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9173` n `168` status `ready` deltaP `12.4201` edge `0.0651` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6813` n `180` status `ready` deltaP `9.3114` edge `0.029` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1983` n `168` status `ready` deltaP `4.4788` edge `0.0047` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.2083` n `180` status `ready` deltaP `2.9042` edge `-0.0009` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8404` n `180` status `ready` deltaP `-6.67` edge `-0.0045` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.302` n `180` status `ready` deltaP `-5.2195` edge `-0.0101` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4786` n `180` status `ready` deltaP `-6.4604` edge `-0.0188` maxDD `-6.8818`
- `market_context_high->commodity_24h` score `-1.5201` n `141` status `ready` deltaP `9.0981` edge `0.105` maxDD `-20.8433`
- `market_context_high->index_4h` score `-1.7702` n `168` status `ready` deltaP `-6.3734` edge `-0.0156` maxDD `-1.4875`
- `market_context_high->metal_24h` score `-1.8862` n `141` status `ready` deltaP `1.883` edge `-0.0373` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.3149` n `141` status `ready` deltaP `-10.4773` edge `-0.0174` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.715` n `180` status `ready` deltaP `-9.9201` edge `-0.0416` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1271` n `168` status `ready` deltaP `-7.2155` edge `-0.0361` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.5116` n `180` status `ready` deltaP `-8.2069` edge `-0.0475` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.3905` n `168` status `ready` deltaP `-15.9117` edge `-0.1459` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.5213` n `168` status `ready` deltaP `-11.3458` edge `-0.133` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.7451` n `141` status `ready` deltaP `-13.5194` edge `-0.1975` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.3915` n `141` status `ready` deltaP `-12.0161` edge `-0.2227` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

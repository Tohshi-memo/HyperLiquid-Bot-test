# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T21:11:28.687957+00:00`
- Price records: `672`
- Market context records: `6748`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.1833` n `176` status `ready` deltaP `1.5783` edge `0.5164` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0594` n `176` status `ready` deltaP `8.1009` edge `0.0396` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0231` n `176` status `ready` deltaP `6.2466` edge `0.0367` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.1354` n `176` status `ready` deltaP `7.9704` edge `0.1224` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3804` n `176` status `ready` deltaP `-0.1157` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5586` n `176` status `ready` deltaP `-0.2688` edge `0.0016` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6375` n `176` status `ready` deltaP `-0.4525` edge `-0.0104` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6646` n `176` status `ready` deltaP `-4.6918` edge `-0.0014` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.014` n `176` status `ready` deltaP `4.0045` edge `-0.0085` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.2011` n `176` status `ready` deltaP `7.8437` edge `0.0001` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2034` n `176` status `ready` deltaP `6.7489` edge `-0.0113` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4501` n `176` status `ready` deltaP `-1.7738` edge `-0.0251` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7932` n `176` status `ready` deltaP `-7.6245` edge `-0.0085` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.2987` n `176` status `ready` deltaP `5.1829` edge `0.0022` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.4306` n `176` status `ready` deltaP `3.8941` edge `0.0026` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.63` n `176` status `ready` deltaP `-6.3193` edge `-0.009` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.7971` n `176` status `ready` deltaP `-16.6297` edge `0.031` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.0257` n `176` status `ready` deltaP `4.3792` edge `-0.1184` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3055` n `176` status `ready` deltaP `-8.0492` edge `-0.0015` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.1525` n `176` status `ready` deltaP `-11.7267` edge `-0.1185` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

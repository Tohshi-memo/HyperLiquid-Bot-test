# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T03:22:26.631639+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9604`

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

- `market_context_high->unknown_4h` score `89.7667` n `152` status `ready` deltaP `1.5324` edge `7.5039` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `21.3167` n `152` status `ready` deltaP `1.367` edge `1.8162` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.301` n `152` status `ready` deltaP `11.3446` edge `0.0093` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.2917` n `152` status `ready` deltaP `8.5841` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1227` n `120` status `ready` deltaP `21.9641` edge `0.1277` maxDD `-6.6721`
- `market_context_high->index_24h` score `0.0374` n `120` status `ready` deltaP `16.8602` edge `0.0124` maxDD `-4.2671`
- `market_context_high->metal_1h` score `-0.0821` n `152` status `ready` deltaP `8.9781` edge `0.0076` maxDD `-1.5714`
- `market_context_high->commodity_1h` score `-0.1613` n `152` status `ready` deltaP `3.1083` edge `0.0159` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1976` n `120` status `ready` deltaP `16.0196` edge `0.0251` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3201` n `152` status `ready` deltaP `7.0683` edge `0.0491` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6122` n `152` status `ready` deltaP `-0.4767` edge `-0.0016` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8647` n `152` status `ready` deltaP `4.818` edge `0.0151` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9049` n `152` status `ready` deltaP `8.1354` edge `-0.0012` maxDD `-5.1905`
- `market_context_high->equity_1h` score `-1.8018` n `152` status `ready` deltaP `1.2606` edge `-0.0118` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9851` n `152` status `ready` deltaP `-0.2009` edge `-0.0047` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4824` n `152` status `ready` deltaP `-6.9239` edge `-0.0264` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.304` n `120` status `ready` deltaP `-0.9865` edge `-0.0595` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6571` n `152` status `ready` deltaP `-0.9066` edge `-0.091` maxDD `-32.6685`
- `market_context_high->commodity_24h` score `-5.6496` n `120` status `ready` deltaP `-9.8541` edge `-0.0996` maxDD `-24.0547`
- `market_context_high->equity_24h` score `-5.8084` n `120` status `ready` deltaP `-5.2196` edge `-0.1966` maxDD `-33.062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

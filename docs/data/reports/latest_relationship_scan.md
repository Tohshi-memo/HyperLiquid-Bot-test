# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T12:52:28.906538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `12406.8827` n `105` status `ready` deltaP `0.4933` edge `1033.9234` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7725.469` n `105` status `ready` deltaP `-0.1495` edge `643.8185` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `24.4056` n `91` status `ready` deltaP `44.6295` edge `1.8118` maxDD `-4.0426`
- `market_context_high->crypto_alt_24h` score `11.6309` n `91` status `ready` deltaP `24.5574` edge `1.4667` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.6489` n `105` status `ready` deltaP `3.0299` edge `0.3991` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.0054` n `105` status `ready` deltaP `3.6397` edge `0.2671` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.2572` n `105` status `ready` deltaP `16.9381` edge `0.0375` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.2053` n `91` status `ready` deltaP `17.632` edge `0.2084` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.1607` n `105` status `ready` deltaP `4.722` edge `0.0144` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2985` n `105` status `ready` deltaP `3.9735` edge `0.0849` maxDD `-7.3061`
- `market_context_high->index_1h` score `-0.5453` n `105` status `ready` deltaP `0.0142` edge `0.0037` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.7` n `105` status `ready` deltaP `-1.5369` edge `0.0427` maxDD `-5.4428`
- `market_context_high->index_4h` score `-1.206` n `105` status `ready` deltaP `-2.876` edge `-0.0011` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4807` n `105` status `ready` deltaP `-10.2167` edge `-0.0008` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-2.1451` n `105` status `ready` deltaP `2.8714` edge `-0.0067` maxDD `-10.9626`
- `market_context_high->fx_4h` score `-2.4037` n `105` status `ready` deltaP `-15.1771` edge `-0.0041` maxDD `-1.8978`
- `market_context_high->commodity_1h` score `-2.4907` n `105` status `ready` deltaP `-10.6116` edge `-0.029` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.8752` n `91` status `ready` deltaP `-20.6616` edge `-0.0075` maxDD `-5.5487`
- `market_context_high->commodity_4h` score `-8.06` n `105` status `ready` deltaP `-28.5119` edge `-0.1197` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.4125` n `105` status `ready` deltaP `-8.1315` edge `-0.0592` maxDD `-43.344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

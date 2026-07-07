# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T01:37:25.222871+00:00`
- Price records: `672`
- Market context records: `5934`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11237`

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

- `news_risk_high->fx_4h` score `3.5985` n `30` status `ready` deltaP `37.2561` edge `0.0561` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2144` n `221` status `ready` deltaP `9.3657` edge `0.1482` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8325` n `30` status `ready` deltaP `10.489` edge `0.0835` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1608` n `30` status `ready` deltaP `4.8703` edge `0.0343` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.105` n `221` status `ready` deltaP `5.9928` edge `0.0386` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3062` n `221` status `ready` deltaP `3.8597` edge `0.0021` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4422` n `30` status `ready` deltaP `1.5369` edge `-0.0303` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5576` n `221` status `ready` deltaP `-2.6452` edge `-0.0023` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6266` n `221` status `ready` deltaP `3.2643` edge `0.03` maxDD `-6.2348`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->crypto_alt_1h` score `-0.708` n `221` status `ready` deltaP `2.5022` edge `0.026` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.8794` n `221` status `ready` deltaP `0.9883` edge `0.0049` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1498` n `30` status `ready` deltaP `-11.0479` edge `-0.0223` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.2468` n `213` status `ready` deltaP `16.7963` edge `0.2358` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7365` n `221` status `ready` deltaP `-4.6932` edge `-0.02` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8169` n `221` status `ready` deltaP `-4.0806` edge `-0.0425` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.8521` n `221` status `ready` deltaP `0.1779` edge `0.0132` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0718` n `30` status `ready` deltaP `-17.8455` edge `-0.0591` maxDD `-2.3372`
- `news_risk_high->index_4h` score `-2.1375` n `30` status `ready` deltaP `-14.5732` edge `-0.0735` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

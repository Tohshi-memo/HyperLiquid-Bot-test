# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T14:37:30.081300+00:00`
- Price records: `672`
- Market context records: `5887`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.7363` n `30` status `ready` deltaP `38.9329` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0753` n `30` status `ready` deltaP `25.1297` edge `0.0193` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0387` n `227` status `ready` deltaP `7.5427` edge `0.1463` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9385` n `30` status `ready` deltaP `11.5369` edge `0.0901` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2544` n `30` status `ready` deltaP `5.1697` edge `0.0443` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1714` n `230` status `ready` deltaP `5.1237` edge `0.0365` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.2947` n `230` status `ready` deltaP `3.5564` edge `0.0056` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4453` n `30` status `ready` deltaP `1.2375` edge `-0.0287` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.5078` n `230` status `ready` deltaP `3.8558` edge `0.0413` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.5351` n `230` status `ready` deltaP `-1.3825` edge `-0.0023` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.5791` n `230` status `ready` deltaP `0.919` edge `0.0044` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.583` n `230` status `ready` deltaP `2.8508` edge `0.0397` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8036` n `230` status `ready` deltaP `-2.5514` edge `-0.0011` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2728` n `30` status `ready` deltaP `-12.994` edge `-0.0251` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.6817` n `227` status `ready` deltaP `8.9301` edge `0.1621` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7992` n `30` status `ready` deltaP `-13.5772` edge `-0.0526` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.926` n `223` status `ready` deltaP `3.6108` edge `0.0108` maxDD `-5.5435`
- `market_context_high->index_4h` score `-1.9562` n `227` status `ready` deltaP `-0.9127` edge `0.0118` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.2969` n `30` status `ready` deltaP `-16.8598` edge `-0.0787` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.4598` n `227` status `ready` deltaP `-2.3584` edge `-0.0179` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T10:52:28.212482+00:00`
- Price records: `672`
- Market context records: `5871`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7315` n `30` status `ready` deltaP `38.9329` edge `0.056` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.025` n `30` status `ready` deltaP `24.5309` edge `0.0191` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2816` n `237` status `ready` deltaP `7.3679` edge `0.1677` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.8979` n `30` status `ready` deltaP `11.8363` edge `0.0829` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2582` n `30` status `ready` deltaP `5.4691` edge `0.0428` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.4198` n `241` status `ready` deltaP `-0.6696` edge `-0.0005` maxDD `-0.5751`
- `market_context_high->equity_1h` score `-0.4235` n `241` status `ready` deltaP `4.7557` edge `0.0337` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.4311` n `241` status `ready` deltaP `3.8053` edge `0.0058` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4313` n `30` status `ready` deltaP `1.5369` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5582` n `241` status `ready` deltaP `-1.8119` edge `-0.0024` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.6227` n `241` status `ready` deltaP `0.1864` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7084` n `241` status `ready` deltaP `4.1047` edge `0.0457` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.8194` n `241` status `ready` deltaP `3.1592` edge `0.0441` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2077` n `237` status `ready` deltaP `-0.0148` edge `0.014` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8174` n `30` status `ready` deltaP `-13.8821` edge `-0.0529` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8366` n `228` status `ready` deltaP `4.8794` edge `0.0138` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9314` n `237` status `ready` deltaP `-7.1852` edge `-0.0048` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.2279` n `237` status `ready` deltaP `9.3277` edge `0.1894` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2519` n `237` status `ready` deltaP `-0.4644` edge `-0.0132` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

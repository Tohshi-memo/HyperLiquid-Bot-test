# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T09:11:10.522487+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `47.0362` n `127` status `ready` deltaP `-18.7803` edge `4.2903` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `2.1604` n `127` status `ready` deltaP `13.3381` edge `0.1798` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.2157` n `32` status `ready` deltaP `12.4626` edge `0.0415` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2157` n `32` status `ready` deltaP `12.4626` edge `0.0415` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `0.8621` n `176` status `ready` deltaP `11.4606` edge `0.0669` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7564` n `181` status `ready` deltaP `10.0109` edge `0.03` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4978` n `127` status `ready` deltaP `16.8875` edge `0.032` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2353` n `32` status `ready` deltaP `9.0569` edge `0.0073` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2353` n `32` status `ready` deltaP `9.0569` edge `0.0073` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1239` n `32` status `ready` deltaP `4.6033` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1239` n `32` status `ready` deltaP `4.6033` edge `0.0024` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.1096` n `181` status `ready` deltaP `4.1544` edge `0.0006` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1703` n `176` status `ready` deltaP `5.0444` edge `0.005` maxDD `-0.504`
- `risk_on_high->equity_1h` score `-0.8066` n `32` status `ready` deltaP `-4.8091` edge `-0.017` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.8066` n `32` status `ready` deltaP `-4.8091` edge `-0.017` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.9028` n `181` status `ready` deltaP `-8.1392` edge `-0.0038` maxDD `-0.948`
- `market_context_high->metal_1h` score `-1.1443` n `181` status `ready` deltaP `-8.1748` edge `-0.0161` maxDD `-2.0884`
- `risk_on_high->crypto_major_1h` score `-1.4509` n `32` status `ready` deltaP `0.8795` edge `-0.0686` maxDD `-2.6536`
- `risk_on_and_context->crypto_major_1h` score `-1.4509` n `32` status `ready` deltaP `0.8795` edge `-0.0686` maxDD `-2.6536`
- `market_context_high->index_4h` score `-1.5096` n `176` status `ready` deltaP `-4.0465` edge `-0.0094` maxDD `-1.4875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

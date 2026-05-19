# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T01:52:16.720365+00:00`
- Price records: `672`
- Market context records: `1175`
- Flow alert records: `5286`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.5467` n `144` status `ready` deltaP `46.0069` edge `1.5187` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1498` n `144` status `ready` deltaP `22.2223` edge `0.8993` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.06` n `144` status `ready` deltaP `19.9653` edge `0.5524` maxDD `-6.4404`
- `market_context_high->metal_24h` score `5.6732` n `144` status `ready` deltaP `-2.7778` edge `0.658` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.5068` n `144` status `ready` deltaP `19.6181` edge `0.3839` maxDD `-3.4627`
- `market_context_high->equity_4h` score `2.5811` n `153` status `ready` deltaP `13.323` edge `0.1926` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2594` n `153` status `ready` deltaP `9.9673` edge `0.1068` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5907` n `153` status `ready` deltaP `8.4771` edge `0.0244` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3423` n `153` status `ready` deltaP `3.0586` edge `0.0459` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1486` n `153` status `ready` deltaP `8.6484` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1278` n `153` status `ready` deltaP `8.4748` edge `0.152` maxDD `-8.3693`
- `market_context_high->unknown_4h` score `-0.0488` n `153` status `ready` deltaP `6.4931` edge `0.0743` maxDD `-6.7322`
- `market_context_high->crypto_major_1h` score `-0.0646` n `153` status `ready` deltaP `6.0741` edge `0.0278` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.3686` n `153` status `ready` deltaP `6.2131` edge `-0.0111` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4847` n `153` status `ready` deltaP `1.8277` edge `0.0317` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8436` n `153` status `ready` deltaP `-3.4451` edge `-0.0044` maxDD `-3.7959`
- `market_context_high->unknown_24h` score `-0.8944` n `144` status `ready` deltaP `4.3403` edge `0.1695` maxDD `-10.1706`
- `market_context_high->fx_4h` score `-1.0197` n `153` status `ready` deltaP `-3.8976` edge `-0.0051` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3517` n `153` status `ready` deltaP `3.795` edge `0.0979` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8736` n `153` status `ready` deltaP `5.1899` edge `-0.0794` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

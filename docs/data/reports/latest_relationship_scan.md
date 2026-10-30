# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T01:37:27.925530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1652.7158` n `134` status `ready` deltaP `-2.7908` edge `137.7879` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `41.2009` n `134` status `ready` deltaP `5.2944` edge `3.4114` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.7163` n `134` status `ready` deltaP `31.2707` edge `0.0362` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2917` n `134` status `ready` deltaP `9.706` edge `0.0106` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1741` n `134` status `ready` deltaP `12.7184` edge `0.0516` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0767` n `134` status `ready` deltaP `12.9346` edge `0.0132` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `0.0733` n `134` status `ready` deltaP `7.0158` edge `0.0621` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0584` n `134` status `ready` deltaP `3.2845` edge `0.0608` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1446` n `134` status `ready` deltaP `2.8309` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->equity_24h` score `-0.244` n `134` status `ready` deltaP `13.7075` edge `0.164` maxDD `-14.0571`
- `market_context_high->commodity_1h` score `-0.3128` n `134` status `ready` deltaP `1.6445` edge `0.0144` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6058` n `134` status `ready` deltaP `-1.9976` edge `-0.0045` maxDD `-0.4545`
- `market_context_high->equity_4h` score `-0.6625` n `134` status `ready` deltaP `0.1047` edge `0.0728` maxDD `-6.008`
- `market_context_high->crypto_alt_1h` score `-0.7051` n `134` status `ready` deltaP `3.8967` edge `0.0701` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8917` n `134` status `ready` deltaP `-2.6946` edge `-0.0005` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.3907` n `134` status `ready` deltaP `1.5418` edge `0.0069` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5305` n `134` status `ready` deltaP `3.9257` edge `0.0423` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.643` n `134` status `ready` deltaP `7.7039` edge `0.0675` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.1677` n `134` status `ready` deltaP `-4.7575` edge `-0.0169` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.026` n `134` status `ready` deltaP `5.2446` edge `0.0079` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

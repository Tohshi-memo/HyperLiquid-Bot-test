# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T15:07:32.886575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7456`

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

- `news_risk_high->unknown_1h` score `3426.1656` n `31` status `ready` deltaP `2.231` edge `285.5165` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3252.2733` n `31` status `ready` deltaP `3.634` edge `271.0042` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.5184` n `31` status `ready` deltaP `36.9151` edge `1.7971` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.4103` n `31` status `ready` deltaP `35.0087` edge `1.3008` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0316` n `31` status `ready` deltaP `29.2894` edge `0.8907` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3192` n `31` status `ready` deltaP `24.1689` edge `0.7025` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.8966` n `31` status `ready` deltaP `18.1501` edge `0.7767` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.8524` n `31` status `ready` deltaP `32.499` edge `0.3191` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0912` n `31` status `ready` deltaP `41.969` edge `0.1573` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9542` n `31` status `ready` deltaP `17.0403` edge `0.2434` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6024` n `31` status `ready` deltaP `31.7369` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4537` n `31` status `ready` deltaP `26.5165` edge `0.0277` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3439` n `31` status `ready` deltaP `28.6991` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2647` n `31` status `ready` deltaP `14.8976` edge `0.1081` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0862` n `31` status `ready` deltaP `7.0166` edge `0.2668` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.965` n `31` status `ready` deltaP `10.7591` edge `0.2159` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1449` n `31` status `ready` deltaP `24.7923` edge `0.0094` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.5059` n `53` status `ready` deltaP `9.4052` edge `0.0206` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4663` n `31` status `ready` deltaP `10.8084` edge `0.0275` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.457` n `65` status `ready` deltaP `11.8379` edge `0.0018` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

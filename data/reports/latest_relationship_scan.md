# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T02:52:40.853806+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `15570.2798` n `86` status `ready` deltaP `0.3133` edge `1297.5374` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10106.2125` n `86` status `ready` deltaP `1.3506` edge `842.1934` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1340.7009` n `31` status `ready` deltaP `4.3268` edge `111.7138` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1190.0425` n `31` status `ready` deltaP `3.9388` edge `99.1496` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.7141` n `31` status `ready` deltaP `38.4442` edge `0.7681` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.1253` n `31` status `ready` deltaP `26.1506` edge `0.8398` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6901` n `31` status `ready` deltaP `14.644` edge `0.9018` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0481` n `31` status `ready` deltaP `20.1371` edge `0.2218` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.471` n `31` status `ready` deltaP `36.31` edge `0.0732` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7477` n `31` status `ready` deltaP `32.1422` edge `0.0232` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5398` n `31` status `ready` deltaP `10.31` edge `0.303` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1477` n `31` status `ready` deltaP `8.9627` edge `0.2513` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5789` n `31` status `ready` deltaP `29.7324` edge `0.0321` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5223` n `31` status `ready` deltaP `20.894` edge `0.1116` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8257` n `31` status `ready` deltaP `18.1255` edge `0.0248` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0789` n `31` status `ready` deltaP `1.2314` edge `0.0114` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.1379` n `86` status `ready` deltaP `9.3378` edge `0.0123` maxDD `-0.7117`
- `market_context_high->metal_1h` score `-0.3967` n `86` status `ready` deltaP `2.0505` edge `0.0051` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.5144` n `86` status `ready` deltaP `0.3342` edge `0.0005` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.2097` n `86` status `ready` deltaP `-6.458` edge `-0.0185` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

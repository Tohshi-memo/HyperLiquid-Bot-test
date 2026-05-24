# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T16:22:18.174058+00:00`
- Price records: `672`
- Market context records: `1754`
- Flow alert records: `6950`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1762` n `165` status `ready` deltaP `27.2128` edge `0.6592` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9781` n `196` status `ready` deltaP `20.8188` edge `0.536` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.424` n `196` status `ready` deltaP `22.4147` edge `0.4598` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1625` n `165` status `ready` deltaP `18.7974` edge `0.3444` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.8571` n `165` status `ready` deltaP `14.9653` edge `0.7537` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1678` n `30` status `ready` deltaP `24.8703` edge `0.1299` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0443` n `196` status `ready` deltaP `16.4167` edge `0.2537` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `2.8767` n `196` status `ready` deltaP `12.7271` edge `0.382` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.8001` n `165` status `ready` deltaP `17.0675` edge `0.6094` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8807` n `196` status `ready` deltaP `11.713` edge `0.1042` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7729` n `196` status `ready` deltaP `7.4209` edge `0.1173` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.541` n `165` status `ready` deltaP `19.315` edge `0.7749` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2197` n `196` status `ready` deltaP `4.7477` edge `0.094` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.1114` n `196` status `ready` deltaP `5.4198` edge `0.054` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1784` n `196` status `ready` deltaP `4.0664` edge `0.0212` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2428` n `196` status `ready` deltaP `12.444` edge `0.1551` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.4996` n `196` status `ready` deltaP `6.095` edge `0.0289` maxDD `-6.3532`
- `news_risk_high->fx_1h` score `-0.5169` n `30` status `ready` deltaP `-5.8782` edge `-0.0009` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.5658` n `30` status `ready` deltaP `15.9581` edge `-0.1317` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.6131` n `165` status `ready` deltaP `7.0675` edge `0.0067` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T18:52:16.551949+00:00`
- Price records: `672`
- Market context records: `1765`
- Flow alert records: `6982`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1779` n `174` status `ready` deltaP `28.0592` edge `0.6537` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1798` n `195` status `ready` deltaP `21.7949` edge `0.5463` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.759` n `195` status `ready` deltaP `23.3615` edge `0.4814` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8929` n `174` status `ready` deltaP `18.5764` edge `0.3234` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2303` n `195` status `ready` deltaP `17.3608` edge `0.2629` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.1041` n `195` status `ready` deltaP `13.7844` edge `0.3939` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.1007` n `30` status `ready` deltaP `24.2715` edge `0.1283` maxDD `-1.2043`
- `market_context_high->unknown_24h` score `2.8882` n `174` status `ready` deltaP `14.4935` edge `0.6761` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.7156` n `174` status `ready` deltaP `16.972` edge `0.603` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.0618` n `195` status `ready` deltaP `13.0777` edge `0.1102` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8254` n `195` status `ready` deltaP `7.7322` edge `0.1196` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.4403` n `174` status `ready` deltaP `19.0314` edge `0.7684` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.3306` n `195` status `ready` deltaP `5.3401` edge `0.0993` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.1072` n `195` status `ready` deltaP `5.2925` edge `0.0545` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1644` n `195` status `ready` deltaP `4.2254` edge `0.0213` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2008` n `195` status `ready` deltaP `12.6056` edge `0.1594` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.4936` n `30` status `ready` deltaP `-5.4291` edge `-0.0009` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.5058` n `30` status `ready` deltaP `16.4072` edge `-0.127` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.5314` n `174` status `ready` deltaP `7.7885` edge `0.0087` maxDD `-1.3925`
- `market_context_high->metal_1h` score `-0.5421` n `195` status `ready` deltaP `5.2764` edge `0.0289` maxDD `-6.3532`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

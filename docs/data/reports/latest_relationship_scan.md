# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T09:52:25.327332+00:00`
- Price records: `672`
- Market context records: `2855`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `3.7112` n `142` status `ready` deltaP `3.3965` edge `0.6783` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.2423` n `142` status `ready` deltaP `5.3795` edge `0.2808` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `1.2224` n `142` status `ready` deltaP `13.6419` edge `0.3203` maxDD `-12.4171`
- `market_context_high->equity_24h` score `1.1225` n `142` status `ready` deltaP `4.7413` edge `0.2623` maxDD `-12.6963`
- `market_context_high->unknown_4h` score `0.8602` n `142` status `ready` deltaP `6.0331` edge `0.1368` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.7967` n `142` status `ready` deltaP `6.9396` edge `0.1182` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.3481` n `142` status `ready` deltaP `13.3009` edge `0.0401` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1342` n `142` status `ready` deltaP `4.7799` edge `0.0524` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0734` n `142` status `ready` deltaP `4.198` edge `0.012` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.5813` n `142` status `ready` deltaP `5.2459` edge `0.0665` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6257` n `142` status `ready` deltaP `-0.5819` edge `-0.001` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6952` n `142` status `ready` deltaP `-2.334` edge `0.002` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7425` n `142` status `ready` deltaP `-0.3163` edge `-0.0085` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.7892` n `142` status `ready` deltaP `4.5248` edge `0.0556` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.814` n `142` status `ready` deltaP `-2.0009` edge `0.0288` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-0.8892` n `142` status `ready` deltaP `2.7246` edge `0.0457` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.0879` n `142` status `ready` deltaP `13.7281` edge `0.2519` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2357` n `142` status `ready` deltaP `-4.5152` edge `0.005` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2807` n `142` status `ready` deltaP `2.4476` edge `0.0115` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4023` n `142` status `ready` deltaP `-1.8852` edge `-0.0171` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

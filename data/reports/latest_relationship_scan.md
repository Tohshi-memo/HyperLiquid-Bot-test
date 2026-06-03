# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T19:22:23.850794+00:00`
- Price records: `672`
- Market context records: `2793`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.0683` n `142` status `ready` deltaP `5.3795` edge `0.2663` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.118` n `142` status `ready` deltaP `2.8756` edge `0.549` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.893` n `142` status `ready` deltaP `6.338` edge `0.1375` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5809` n `142` status `ready` deltaP `11.0377` edge `0.2842` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3397` n `142` status `ready` deltaP `13.6057` edge `0.037` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0373` n `142` status `ready` deltaP `4.1811` edge `0.0421` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0992` n `142` status `ready` deltaP `4.0483` edge `0.0097` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6139` n `142` status `ready` deltaP `0.7316` edge `0.001` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6818` n `142` status `ready` deltaP `-0.7316` edge `-0.0072` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7007` n `142` status `ready` deltaP `4.9465` edge `0.0532` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.8991` n `142` status `ready` deltaP `4.0757` edge `0.0445` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9855` n `142` status `ready` deltaP `-2.7494` edge `0.0195` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1325` n `142` status `ready` deltaP `-3.6005` edge `0.0075` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.1838` n `142` status `ready` deltaP `2.2673` edge `0.0242` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.3825` n `142` status `ready` deltaP `14.1854` edge `0.2243` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.519` n `142` status `ready` deltaP `-2.5797` edge `-0.0222` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6616` n `142` status `ready` deltaP `-0.6012` edge `-0.017` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.0631` n `142` status `ready` deltaP `-0.0086` edge `-0.0094` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4262` n `142` status `ready` deltaP `5.7347` edge `0.1413` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

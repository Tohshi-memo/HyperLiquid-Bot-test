# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T16:22:27.350169+00:00`
- Price records: `672`
- Market context records: `6833`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `0.9365` n `176` status `ready` deltaP `-1.5467` edge `0.5056` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1841` n `176` status `ready` deltaP `9.8801` edge `0.1363` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3372` n `211` status `ready` deltaP `0.6861` edge `0.0007` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.341` n `211` status `ready` deltaP `4.9004` edge `0.0249` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4498` n `211` status `ready` deltaP `2.7053` edge `0.0209` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8836` n `211` status `ready` deltaP `-3.0806` edge `-0.0053` maxDD `-1.9952`
- `market_context_high->metal_1h` score `-0.9661` n `211` status `ready` deltaP `-6.0732` edge `-0.0095` maxDD `-1.9098`
- `market_context_high->fx_4h` score `-1.1367` n `201` status `ready` deltaP `8.7216` edge `0.0025` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1593` n `211` status `ready` deltaP `-3.0061` edge `-0.0081` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6291` n `211` status `ready` deltaP `-3.6538` edge `-0.0213` maxDD `-3.2083`
- `market_context_high->index_4h` score `-2.0945` n `201` status `ready` deltaP `0.7311` edge `-0.0341` maxDD `-9.8109`
- `market_context_high->commodity_4h` score `-2.3124` n `201` status `ready` deltaP `-4.2926` edge `-0.0151` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.6831` n `201` status `ready` deltaP `-2.9942` edge `-0.0257` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.8777` n `201` status `ready` deltaP `0.6272` edge `-0.0404` maxDD `-16.9508`
- `market_context_high->equity_1h` score `-2.8895` n `211` status `ready` deltaP `-0.4122` edge `-0.0417` maxDD `-11.374`
- `market_context_high->crypto_alt_4h` score `-3.0805` n `201` status `ready` deltaP `0.4664` edge `-0.0397` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2034` n `201` status `ready` deltaP `-9.9594` edge `0.036` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4528` n `176` status `ready` deltaP `-9.7853` edge `-0.0022` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.9538` n `201` status `ready` deltaP `-1.5722` edge `-0.209` maxDD `-46.7628`
- `market_context_high->metal_24h` score `-9.3826` n `176` status `ready` deltaP `-19.8864` edge `-0.2218` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T14:52:31.651717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1486.4488` n `139` status `ready` deltaP `-1.5912` edge `123.9476` maxDD `-2.9675`
- `market_context_high->unknown_4h` score `54.1855` n `139` status `ready` deltaP `6.5922` edge `4.4848` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.8323` n `139` status `ready` deltaP `23.9559` edge `0.0113` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `0.2642` n `139` status `ready` deltaP `13.1997` edge `0.0559` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.0091` n `139` status `ready` deltaP `8.8097` edge `0.0074` maxDD `-0.8642`
- `market_context_high->fx_1h` score `0.0031` n `139` status `ready` deltaP `5.3666` edge `0.0003` maxDD `-0.1986`
- `market_context_high->metal_4h` score `-0.1457` n `139` status `ready` deltaP `11.6029` edge `0.0075` maxDD `-2.9492`
- `market_context_high->fx_4h` score `-0.2614` n `139` status `ready` deltaP `3.89` edge `0.0004` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3101` n `139` status `ready` deltaP `1.6779` edge `0.0144` maxDD `-0.4475`
- `market_context_high->equity_1h` score `-0.681` n `139` status `ready` deltaP `0.3306` edge `0.021` maxDD `-4.1742`
- `market_context_high->crypto_major_1h` score `-0.7406` n `139` status `ready` deltaP `4.7678` edge `0.0249` maxDD `-6.1385`
- `market_context_high->fx_24h` score `-0.9278` n `139` status `ready` deltaP `6.3387` edge `0.0135` maxDD `-0.9792`
- `market_context_high->index_1h` score `-1.0444` n `139` status `ready` deltaP `-3.0834` edge `-0.0023` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.3696` n `139` status `ready` deltaP `1.7942` edge `0.0152` maxDD `-9.5532`
- `market_context_high->metal_24h` score `-1.907` n `139` status `ready` deltaP `2.3418` edge `0.0046` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-2.4761` n `139` status `ready` deltaP `-3.2988` edge `-0.0546` maxDD `-12.6015`
- `market_context_high->index_4h` score `-2.6298` n `139` status `ready` deltaP `-8.1341` edge `-0.0263` maxDD `-4.0901`
- `market_context_high->crypto_major_4h` score `-2.9337` n `139` status `ready` deltaP `3.3954` edge `-0.0375` maxDD `-21.5668`
- `market_context_high->equity_24h` score `-3.875` n `139` status `ready` deltaP `6.6897` edge `-0.0918` maxDD `-14.0571`
- `market_context_high->crypto_major_24h` score `-4.0298` n `139` status `ready` deltaP `-4.7749` edge `0.0009` maxDD `-29.1905`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

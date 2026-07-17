# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T14:52:37.972029+00:00`
- Price records: `672`
- Market context records: `7039`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `-0.1081` n `207` status `ready` deltaP `13.3815` edge `0.01` maxDD `-1.0452`
- `market_context_high->fx_1h` score `-0.2149` n `207` status `ready` deltaP `2.3713` edge `0.0019` maxDD `-0.2872`
- `market_context_high->crypto_alt_1h` score `-0.2889` n `207` status `ready` deltaP `2.1602` edge `0.035` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.721` n `207` status `ready` deltaP `-0.0167` edge `-0.0012` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7449` n `207` status `ready` deltaP `-2.7178` edge `-0.0006` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7742` n `207` status `ready` deltaP `-3.3035` edge `-0.0156` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.8845` n `207` status `ready` deltaP `4.0246` edge `0.0347` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0919` n `207` status `ready` deltaP `-2.861` edge `0.007` maxDD `-2.6467`
- `market_context_high->equity_1h` score `-1.7859` n `207` status `ready` deltaP `4.3992` edge `-0.016` maxDD `-14.716`
- `market_context_high->unknown_4h` score `-1.8334` n `207` status `ready` deltaP `-6.3781` edge `0.0902` maxDD `-7.3702`
- `market_context_high->unknown_24h` score `-1.9494` n `200` status `ready` deltaP `-9.5764` edge `0.2967` maxDD `-20.9557`
- `market_context_high->index_4h` score `-1.9923` n `207` status `ready` deltaP `5.0681` edge `-0.0193` maxDD `-12.2591`
- `market_context_high->commodity_4h` score `-2.024` n `207` status `ready` deltaP `-3.185` edge `-0.0314` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.0459` n `207` status `ready` deltaP `4.2197` edge `0.0079` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.2765` n `200` status `ready` deltaP `-0.2292` edge `-0.0573` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5269` n `207` status `ready` deltaP `3.0112` edge `0.0345` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7987` n `207` status `ready` deltaP `4.2072` edge `0.0416` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7406` n `200` status `ready` deltaP `-2.6111` edge `-0.0116` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.2625` n `207` status `ready` deltaP `5.3472` edge `-0.0797` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.3861` n `200` status `ready` deltaP `-14.4653` edge `-0.0686` maxDD `-42.3713`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

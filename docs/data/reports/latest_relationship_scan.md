# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T08:37:26.064144+00:00`
- Price records: `672`
- Market context records: `7121`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.3442` n `146` status `ready` deltaP `15.0037` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.087` n `151` status `ready` deltaP `4.6903` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.323` n `151` status `ready` deltaP `-1.6735` edge `0.0401` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3808` n `151` status `ready` deltaP `1.3562` edge `0.0309` maxDD `-4.7674`
- `market_context_high->index_1h` score `-0.5229` n `151` status `ready` deltaP `0.7852` edge `-0.0058` maxDD `-2.3175`
- `market_context_high->crypto_major_1h` score `-0.779` n `151` status `ready` deltaP `4.6675` edge `0.0392` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8507` n `151` status `ready` deltaP `-4.1371` edge `-0.0194` maxDD `-1.9668`
- `market_context_high->metal_1h` score `-1.3832` n `151` status `ready` deltaP `-5.0254` edge `-0.0052` maxDD `-2.1249`
- `market_context_high->commodity_4h` score `-1.3834` n `146` status `ready` deltaP `-4.5794` edge `-0.0433` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.5502` n `146` status `ready` deltaP `-6.8326` edge `0.007` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0688` n `151` status `ready` deltaP `3.0079` edge `-0.043` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0132` n `146` status `ready` deltaP `4.3414` edge `0.0132` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7412` n `146` status `ready` deltaP `-9.5082` edge `-0.1175` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0586` n `146` status `ready` deltaP `-2.8817` edge `-0.0491` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4748` n `146` status `ready` deltaP `-9.564` edge `-0.0123` maxDD `-5.414`
- `market_context_high->crypto_alt_4h` score `-4.6102` n `146` status `ready` deltaP `1.0733` edge `-0.0128` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.6845` n `146` status `ready` deltaP `-12.714` edge `-0.0229` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.4451` n `146` status `ready` deltaP `-27.9775` edge `-0.0859` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.654` n `146` status `ready` deltaP `-1.8899` edge `-0.2382` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.8607` n `146` status `ready` deltaP `-27.8919` edge `-0.1621` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

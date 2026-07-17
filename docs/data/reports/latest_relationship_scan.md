# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T13:37:25.188909+00:00`
- Price records: `672`
- Market context records: `7033`
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

- `market_context_high->fx_1h` score `-0.2469` n `212` status `ready` deltaP `2.0958` edge `0.0013` maxDD `-0.4204`
- `market_context_high->crypto_alt_1h` score `-0.3023` n `212` status `ready` deltaP `2.1269` edge `0.0335` maxDD `-4.5815`
- `market_context_high->fx_4h` score `-0.3506` n `212` status `ready` deltaP `12.5058` edge `0.0089` maxDD `-1.3107`
- `market_context_high->index_1h` score `-0.6617` n `212` status `ready` deltaP `0.8219` edge `0.0008` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.671` n `212` status `ready` deltaP `-1.627` edge `0.0016` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9226` n `212` status `ready` deltaP `3.9685` edge `0.0319` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0859` n `212` status `ready` deltaP `-2.5167` edge `0.0052` maxDD `-2.6467`
- `market_context_high->commodity_1h` score `-1.249` n `212` status `ready` deltaP `-3.6832` edge `-0.0179` maxDD `-1.9306`
- `market_context_high->unknown_24h` score `-1.2721` n `200` status `ready` deltaP `-7.9444` edge `0.35` maxDD `-19.1435`
- `market_context_high->index_4h` score `-1.9209` n `212` status `ready` deltaP `5.9595` edge `-0.0161` maxDD `-12.2591`
- `market_context_high->unknown_4h` score `-1.9536` n `212` status `ready` deltaP `-6.0486` edge `0.0856` maxDD `-7.9797`
- `market_context_high->metal_4h` score `-2.0097` n `212` status `ready` deltaP `4.7947` edge `0.0087` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0744` n `212` status `ready` deltaP `-3.7103` edge `-0.0321` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.4373` n `200` status `ready` deltaP `-1.5347` edge `-0.062` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.625` n `212` status `ready` deltaP `1.8149` edge `0.0299` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.7382` n `212` status `ready` deltaP `3.8244` edge `-0.0114` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-2.9395` n `212` status `ready` deltaP `2.9539` edge `0.0319` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7094` n `200` status `ready` deltaP `-2.6111` edge `-0.0119` maxDD `-3.718`
- `market_context_high->equity_4h` score `-7.236` n `212` status `ready` deltaP `4.8061` edge `-0.0727` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.8102` n `200` status `ready` deltaP `-12.8333` edge `-0.0594` maxDD `-40.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

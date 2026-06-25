# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T00:52:25.985257+00:00`
- Price records: `672`
- Market context records: `4675`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `75.599` n `139` status `ready` deltaP `11.276` edge `6.2665` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.6563` n `139` status `ready` deltaP `10.2847` edge `0.4405` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4779` n `139` status `ready` deltaP `9.4187` edge `0.1527` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5429` n `139` status `ready` deltaP `1.4033` edge `0.025` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5981` n `139` status `ready` deltaP `-2.5514` edge `-0.0042` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8052` n `139` status `ready` deltaP `3.2616` edge `-0.0127` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.8215` n `139` status `ready` deltaP `0.3783` edge `0.0004` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9038` n `139` status `ready` deltaP `-3.1168` edge `0.0036` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.4069` n `139` status `ready` deltaP `0.2314` edge `-0.005` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7798` n `139` status `ready` deltaP `-5.0629` edge `-0.0137` maxDD `-2.7358`
- `market_context_high->commodity_4h` score `-2.055` n `139` status `ready` deltaP `3.9459` edge `0.0132` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.7979` n `139` status `ready` deltaP `-3.8115` edge `-0.0765` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7618` n `139` status `ready` deltaP `-10.5341` edge `-0.0107` maxDD `-5.6047`
- `market_context_high->commodity_24h` score `-4.9742` n `139` status `ready` deltaP `12.9334` edge `0.0497` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6053` n `139` status `ready` deltaP `-3.1168` edge `-0.1176` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7662` n `139` status `ready` deltaP `-5.9654` edge `-0.1488` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.9739` n `139` status `ready` deltaP `-9.0166` edge `-0.0669` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.5138` n `139` status `ready` deltaP `-2.518` edge `-0.209` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.3573` n `139` status `ready` deltaP `-2.8097` edge `-0.2883` maxDD `-65.0761`
- `market_context_high->crypto_major_4h` score `-11.6394` n `139` status `ready` deltaP `-4.3286` edge `-0.369` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

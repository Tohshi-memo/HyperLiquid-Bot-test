# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T08:22:23.582440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1732.3014` n `129` status `ready` deltaP `-5.3658` edge `144.4372` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `104.8626` n `98` status `ready` deltaP `-5.7924` edge `8.8058` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `29.9776` n `129` status `ready` deltaP `2.0431` edge `2.4978` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.8281` n `129` status `ready` deltaP `21.7337` edge `0.8665` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.7295` n `96` status `ready` deltaP `20.1473` edge `0.4621` maxDD `-6.5168`
- `market_context_high->index_24h` score `4.2858` n `129` status `ready` deltaP `40.5241` edge `0.1053` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9284` n `98` status `ready` deltaP `8.2457` edge `0.1053` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.8613` n `129` status `ready` deltaP `12.8603` edge `0.0152` maxDD `-0.3325`
- `market_context_high->metal_4h` score `0.4073` n `129` status `ready` deltaP `16.1053` edge `0.0324` maxDD `-1.671`
- `market_context_high->equity_1h` score `0.3591` n `129` status `ready` deltaP `5.4879` edge `0.0809` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.3091` n `129` status `ready` deltaP `13.8058` edge `0.0556` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.2672` n `129` status `ready` deltaP `8.9147` edge `0.0656` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.0197` n `129` status `ready` deltaP `2.7392` edge `0.1427` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0372` n `129` status `ready` deltaP `4.7927` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2346` n `129` status `ready` deltaP `2.4567` edge `0.0155` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.3989` n `129` status `ready` deltaP `5.6322` edge `0.176` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4905` n `129` status `ready` deltaP `-0.0697` edge `-0.0027` maxDD `-0.4445`
- `market_context_high->index_1h` score `-0.6217` n `129` status `ready` deltaP `0.441` edge `0.0011` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7932` n `129` status `ready` deltaP `3.5313` edge `0.0523` maxDD `-7.536`
- `news_risk_high->index_1h` score `-0.8802` n `98` status `ready` deltaP `1.5642` edge `-0.0038` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T01:37:26.671834+00:00`
- Price records: `672`
- Market context records: `8045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `19.0254` n `77` status `ready` deltaP `32.6814` edge `1.4586` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.2496` n `77` status `ready` deltaP `35.8752` edge `0.4483` maxDD `0.0`
- `market_context_high->equity_4h` score `7.5015` n `90` status `ready` deltaP `30.1558` edge `0.502` maxDD `-4.233`
- `market_context_high->commodity_24h` score `5.0698` n `77` status `ready` deltaP `33.6357` edge `0.3137` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.7354` n `90` status `ready` deltaP `28.3706` edge `0.0748` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.3373` n `90` status `ready` deltaP `21.5718` edge `0.1132` maxDD `-0.979`
- `market_context_high->index_24h` score `2.2391` n `77` status `ready` deltaP `12.5121` edge `0.1702` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6441` n `90` status `ready` deltaP `14.4844` edge `0.1222` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3515` n `77` status `ready` deltaP `28.8933` edge `0.051` maxDD `-0.6283`
- `market_context_high->index_1h` score `0.7659` n `90` status `ready` deltaP `13.3101` edge `0.0181` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7295` n `90` status `ready` deltaP `10.6387` edge `0.0277` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4159` n `90` status `ready` deltaP `10.0` edge `0.0277` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.1905` n `90` status `ready` deltaP `6.3415` edge `0.1454` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.0901` n `90` status `ready` deltaP `2.7033` edge `0.1012` maxDD `-3.9374`
- `market_context_high->fx_4h` score `-0.0143` n `90` status `ready` deltaP `6.8801` edge `0.0054` maxDD `-0.5302`
- `market_context_high->crypto_alt_1h` score `-0.1839` n `90` status `ready` deltaP `0.0865` edge `0.0191` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.4192` n `90` status `ready` deltaP `1.4504` edge `-0.0011` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.7374` n `90` status `ready` deltaP `-3.6727` edge `-0.0006` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8606` n `90` status `ready` deltaP `5.0779` edge `0.006` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.0551` n `90` status `ready` deltaP `6.0279` edge `-0.1691` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

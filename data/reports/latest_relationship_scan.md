# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T13:06:06.283635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.9656` n `145` status `ready` deltaP `7.1981` edge `0.0552` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4041` n `139` status `ready` deltaP `18.5383` edge `-0.046` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1061` n `139` status `ready` deltaP `8.0782` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0069` n `145` status `ready` deltaP `4.5148` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2554` n `139` status `ready` deltaP `6.907` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3381` n `145` status `ready` deltaP `0.5265` edge `-0.005` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3469` n `145` status `ready` deltaP `4.4879` edge `0.0326` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4749` n `139` status `ready` deltaP `4.6763` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.733` n `139` status `ready` deltaP `-1.8062` edge `0.0031` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9317` n `145` status `ready` deltaP `-7.2682` edge `-0.0019` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.725` n `139` status `ready` deltaP `-1.4454` edge `0.069` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-1.7525` n `125` status `ready` deltaP `0.7569` edge `0.0099` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-1.8464` n `139` status `ready` deltaP `4.8452` edge `-0.0574` maxDD `-5.6346`
- `market_context_high->commodity_24h` score `-2.0457` n `125` status `ready` deltaP `-5.4681` edge `0.0493` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.39` n `145` status `ready` deltaP `-2.2486` edge `-0.0347` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4282` n `145` status `ready` deltaP `-4.6221` edge `-0.109` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.5282` n `125` status `ready` deltaP `-8.6792` edge `-0.0448` maxDD `-20.8968`
- `market_context_high->crypto_major_4h` score `-5.4369` n `139` status `ready` deltaP `-0.6053` edge `-0.3194` maxDD `-5.3711`
- `market_context_high->metal_24h` score `-5.4795` n `125` status `ready` deltaP `-24.8861` edge `-0.2058` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T04:06:07.008246+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `13.4571` n `38` status `ready` deltaP `29.2683` edge `0.9263` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6209` n `38` status `ready` deltaP `47.2561` edge `0.2367` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.1047` n `50` status `ready` deltaP `21.7246` edge `0.2209` maxDD `-0.5606`
- `news_risk_high->fx_4h` score `3.2224` n `38` status `ready` deltaP `37.9894` edge `0.0287` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.1988` n `38` status `ready` deltaP `28.458` edge `0.0019` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5764` n `135` status `ready` deltaP `6.6135` edge `0.11` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.3252` n `50` status `ready` deltaP `18.1078` edge `0.0067` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9131` n `50` status `ready` deltaP `19.006` edge `0.0227` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8315` n `135` status `ready` deltaP `19.6387` edge `-0.0403` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.6954` n `38` status `ready` deltaP `15.4445` edge `0.0248` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.2604` n `50` status `ready` deltaP `9.4551` edge `-0.0105` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1476` n `50` status `ready` deltaP `7.7006` edge `0.0029` maxDD `-0.1583`
- `market_context_high->fx_4h` score `0.0952` n `135` status `ready` deltaP `8.1063` edge `0.0084` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0703` n `135` status `ready` deltaP `5.9969` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->metal_1h` score `-0.0759` n `50` status `ready` deltaP `2.9521` edge `-0.0071` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1591` n `135` status `ready` deltaP `1.6634` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3237` n `135` status `ready` deltaP `4.7838` edge `0.0336` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6153` n `135` status `ready` deltaP `-0.6775` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6678` n `135` status `ready` deltaP `1.1755` edge `0.0101` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

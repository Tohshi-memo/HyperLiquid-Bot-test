# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T03:52:25.267419+00:00`
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

- `news_risk_high->unknown_4h` score `13.3361` n `37` status `ready` deltaP `29.4207` edge `0.9152` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6545` n `37` status `ready` deltaP `47.2561` edge `0.2395` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.4815` n `49` status `ready` deltaP `23.2892` edge `0.2349` maxDD `-0.3363`
- `news_risk_high->fx_4h` score `3.2125` n `37` status `ready` deltaP `37.776` edge `0.0293` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.1775` n `37` status `ready` deltaP `28.1024` edge `0.0025` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5597` n `135` status `ready` deltaP `6.4638` edge `0.1096` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.4331` n `49` status `ready` deltaP `19.4275` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0228` n `49` status `ready` deltaP `20.3257` edge `0.0238` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.876` n `135` status `ready` deltaP `19.7911` edge `-0.0376` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.6413` n `37` status `ready` deltaP `14.4488` edge `0.0245` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.208` n `49` status `ready` deltaP `8.8293` edge `-0.0107` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.103` n `49` status `ready` deltaP `6.8435` edge `0.0029` maxDD `-0.1583`
- `market_context_high->fx_4h` score `0.0952` n `135` status `ready` deltaP `8.1063` edge `0.0084` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.0163` n `49` status `ready` deltaP `4.0541` edge `-0.0068` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0703` n `135` status `ready` deltaP `5.9969` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1669` n `135` status `ready` deltaP `1.5137` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3322` n `135` status `ready` deltaP `4.6341` edge `0.0335` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6165` n `135` status `ready` deltaP `-0.6775` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6678` n `135` status `ready` deltaP `1.1755` edge `0.0101` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

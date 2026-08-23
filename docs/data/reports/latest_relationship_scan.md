# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T04:22:48.529409+00:00`
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

- `news_risk_high->unknown_4h` score `13.6921` n `39` status `ready` deltaP `29.1159` edge `0.9469` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.5777` n `39` status `ready` deltaP `47.2561` edge `0.2331` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3.7491` n `51` status `ready` deltaP `20.2272` edge `0.208` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2338` n `39` status `ready` deltaP `38.1918` edge `0.0283` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.221` n `39` status `ready` deltaP `28.7954` edge `0.0015` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5944` n `135` status `ready` deltaP `6.7632` edge `0.1105` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.2206` n `51` status `ready` deltaP `16.8457` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7994` n `51` status `ready` deltaP `17.5942` edge `0.0217` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7797` n `135` status `ready` deltaP `19.4863` edge `-0.0436` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.7469` n `39` status `ready` deltaP `16.3892` edge `0.0251` maxDD `-0.0884`
- `news_risk_high->index_1h` score `0.1834` n `51` status `ready` deltaP `8.3744` edge `0.003` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.162` n `51` status `ready` deltaP `8.2394` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.0952` n `135` status `ready` deltaP `8.1063` edge `0.0084` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0781` n `135` status `ready` deltaP `5.8472` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->metal_1h` score `-0.1247` n `51` status `ready` deltaP `2.043` edge `-0.0073` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1513` n `135` status `ready` deltaP `1.8131` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3229` n `135` status `ready` deltaP `4.7838` edge `0.0337` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6034` n `135` status `ready` deltaP `-0.5278` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6678` n `135` status `ready` deltaP `1.1755` edge `0.0101` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

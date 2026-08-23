# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T04:51:05.088891+00:00`
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

- `news_risk_high->unknown_4h` score `15.5397` n `41` status `ready` deltaP `28.811` edge `1.1029` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9611` n `41` status `ready` deltaP `42.683` edge `0.2223` maxDD `-0.1408`
- `news_risk_high->unknown_1h` score `3.7958` n `51` status `ready` deltaP `20.5266` edge `0.2099` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2286` n `41` status `ready` deltaP `38.2622` edge `0.0274` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `1.8823` n `41` status `ready` deltaP `24.8475` edge `-0.0003` maxDD `-0.0129`
- `market_context_high->unknown_1h` score `1.3923` n `135` status `ready` deltaP `5.5811` edge `0.1032` maxDD `-0.6175`
- `news_risk_high->index_4h` score `1.2916` n `41` status `ready` deltaP `18.1403` edge `0.0253` maxDD `-0.0884`
- `news_risk_high->fx_1h` score `1.2206` n `51` status `ready` deltaP `16.8457` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.808` n `51` status `ready` deltaP `17.7439` edge `0.0218` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7952` n `133` status `ready` deltaP `20.5403` edge `-0.0535` maxDD `-0.3736`
- `news_risk_high->index_1h` score `0.1912` n `51` status `ready` deltaP `8.5241` edge `0.003` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1608` n `51` status `ready` deltaP `8.2394` edge `-0.0107` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1287` n `133` status `ready` deltaP `8.7372` edge `0.0085` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.1096` n `135` status `ready` deltaP `5.2562` edge `0.004` maxDD `-0.9144`
- `news_risk_high->metal_1h` score `-0.1162` n `51` status `ready` deltaP `2.1927` edge `-0.0072` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.2328` n `135` status `ready` deltaP `1.8131` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3583` n `135` status `ready` deltaP `4.1927` edge `0.0331` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4755` n `133` status `ready` deltaP `5.8305` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.653` n `135` status `ready` deltaP `-1.1189` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.7109` n `133` status `ready` deltaP `0.4069` edge `0.0097` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

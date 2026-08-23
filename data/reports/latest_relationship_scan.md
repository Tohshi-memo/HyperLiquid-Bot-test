# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T04:37:26.644478+00:00`
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

- `news_risk_high->unknown_4h` score `13.9991` n `40` status `ready` deltaP `28.9634` edge `0.9735` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.2813` n `40` status `ready` deltaP `44.9085` edge `0.2286` maxDD `-0.0306`
- `news_risk_high->unknown_1h` score `3.7754` n `51` status `ready` deltaP `20.3769` edge `0.2092` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2309` n `40` status `ready` deltaP `38.2317` edge `0.0278` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.0492` n `40` status `ready` deltaP `26.7683` edge `0.0007` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.4931` n `135` status `ready` deltaP `6.1721` edge `0.106` maxDD `-0.4843`
- `news_risk_high->index_4h` score `1.2221` n `40` status `ready` deltaP `17.2866` edge `0.0252` maxDD `-0.0884`
- `news_risk_high->fx_1h` score `1.2206` n `51` status `ready` deltaP `16.8457` edge `0.0064` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `0.851` n `134` status `ready` deltaP `20.0082` edge `-0.0453` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.7994` n `51` status `ready` deltaP `17.5942` edge `0.0217` maxDD `-0.9204`
- `news_risk_high->index_1h` score `0.1834` n `51` status `ready` deltaP `8.3744` edge `0.003` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.162` n `51` status `ready` deltaP `8.2394` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1114` n `134` status `ready` deltaP `8.4183` edge `0.0084` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0781` n `135` status `ready` deltaP `5.8472` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->metal_1h` score `-0.1247` n `51` status `ready` deltaP `2.043` edge `-0.0073` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1513` n `135` status `ready` deltaP `1.8131` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3237` n `135` status `ready` deltaP `4.7838` edge `0.0336` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4649` n `134` status `ready` deltaP `5.9474` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6034` n `135` status `ready` deltaP `-0.5278` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6892` n `134` status `ready` deltaP `0.7941` edge `0.0099` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

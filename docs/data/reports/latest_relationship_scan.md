# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T14:07:38.306478+00:00`
- Price records: `672`
- Market context records: `4628`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `70.0068` n `146` status `ready` deltaP `8.1597` edge `5.8254` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4091` n `146` status `ready` deltaP `9.5807` edge `0.4246` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3125` n `146` status `ready` deltaP `3.398` edge `0.0309` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5652` n `146` status `ready` deltaP `-1.9502` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7618` n `146` status `ready` deltaP `1.6017` edge `-0.0001` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8289` n `146` status `ready` deltaP `-1.7964` edge `0.0044` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9061` n `146` status `ready` deltaP `1.5912` edge `-0.0145` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0219` n `146` status `ready` deltaP `5.4961` edge `0.0431` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.5002` n `144` status `ready` deltaP `5.2083` edge `-0.0674` maxDD `-4.7201`
- `market_context_high->index_1h` score `-1.7011` n `146` status `ready` deltaP `-4.2142` edge `-0.0128` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7072` n `146` status `ready` deltaP `-0.9982` edge `-0.0353` maxDD `-8.8203`
- `market_context_high->metal_1h` score `-2.9541` n `146` status `ready` deltaP `-4.3905` edge `-0.0843` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6925` n `144` status `ready` deltaP `11.9791` edge `0.054` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.1307` n `144` status `ready` deltaP `-10.0694` edge `-0.0092` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5392` n `146` status `ready` deltaP `-2.0958` edge `-0.1189` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7996` n `146` status `ready` deltaP `-5.9921` edge `-0.1514` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.208` n `144` status `ready` deltaP `-8.507` edge `-0.0898` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1963` n `146` status `ready` deltaP `-3.6585` edge `-0.2889` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2533` n `146` status `ready` deltaP `-6.9955` edge `-0.3465` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3571` n `146` status `ready` deltaP `-5.7113` edge `-0.4518` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T21:07:32.761245+00:00`
- Price records: `672`
- Market context records: `2800`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.8501` n `142` status `ready` deltaP `4.5114` edge `0.2539` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.4082` n `142` status `ready` deltaP `1.834` edge `0.4968` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.0296` n `142` status `ready` deltaP `7.1002` edge `0.1438` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5833` n `142` status `ready` deltaP `11.0377` edge `0.2844` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3176` n `142` status `ready` deltaP `13.3009` edge `0.0362` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.067` n `142` status `ready` deltaP `4.9296` edge `0.0458` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0524` n `142` status `ready` deltaP `4.6471` edge `0.0117` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5514` n `142` status `ready` deltaP `-0.6873` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5835` n `142` status `ready` deltaP `1.031` edge `0.0029` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6974` n `142` status `ready` deltaP `-0.8813` edge `-0.0082` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7015` n `142` status `ready` deltaP `5.0962` edge `0.0521` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8871` n `142` status `ready` deltaP `-2.3003` edge `0.0247` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8913` n `142` status `ready` deltaP `4.0757` edge `0.0455` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.1778` n `142` status `ready` deltaP `2.2673` edge `0.0247` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1837` n `142` status `ready` deltaP `-4.2103` edge `0.0073` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.5819` n `142` status `ready` deltaP `14.0329` edge `0.2087` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.6271` n `142` status `ready` deltaP `-3.795` edge `-0.0231` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6373` n `142` status `ready` deltaP `-0.4488` edge `-0.0149` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.0279` n `142` status `ready` deltaP `0.1439` edge `-0.0059` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.2829` n `142` status `ready` deltaP `-1.9146` edge `-0.0794` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

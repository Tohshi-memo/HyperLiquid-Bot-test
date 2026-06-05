# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T04:07:20.637865+00:00`
- Price records: `672`
- Market context records: `2934`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6940`

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

- `market_context_high->crypto_alt_24h` score `15.6441` n `142` status `ready` deltaP `15.202` edge `1.594` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.5411` n `142` status `ready` deltaP `17.4149` edge `0.7127` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.5372` n `142` status `ready` deltaP `15.2753` edge `0.4894` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.6323` n `142` status `ready` deltaP `13.1896` edge `0.2295` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8077` n `142` status `ready` deltaP `15.378` edge `0.3575` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8804` n `143` status `ready` deltaP `8.6592` edge `0.1536` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7282` n `143` status `ready` deltaP `14.9721` edge `0.0777` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0609` n `143` status `ready` deltaP `4.0519` edge `0.0834` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0056` n `143` status `ready` deltaP `4.6973` edge `0.0188` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.1653` n `143` status `ready` deltaP `15.7535` edge `0.3415` maxDD `-30.8239`
- `market_context_high->equity_1h` score `-0.3417` n `143` status `ready` deltaP `1.2029` edge `0.0468` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4431` n `143` status `ready` deltaP `5.8949` edge `0.0799` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5639` n `143` status `ready` deltaP `2.9993` edge `0.0061` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.571` n `143` status `ready` deltaP `-0.9463` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6125` n `143` status `ready` deltaP `5.942` edge `0.0688` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6263` n `143` status `ready` deltaP `0.5464` edge `0.0048` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6797` n `143` status `ready` deltaP `-1.5451` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.982` n `143` status `ready` deltaP `-1.5692` edge `0.0065` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2981` n `143` status `ready` deltaP `1.4242` edge `0.0161` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3032` n `142` status `ready` deltaP `-1.7116` edge `-0.01` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

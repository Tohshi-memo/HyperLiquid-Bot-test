# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T04:22:25.216227+00:00`
- Price records: `672`
- Market context records: `2935`
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

- `market_context_high->crypto_alt_24h` score `15.8308` n `142` status `ready` deltaP `15.3756` edge `1.6084` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.6102` n `142` status `ready` deltaP `17.5885` edge `0.7173` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.6051` n `142` status `ready` deltaP `15.4489` edge `0.4939` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.6594` n `142` status `ready` deltaP `13.3632` edge `0.2306` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8101` n `142` status `ready` deltaP `15.378` edge `0.3577` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8974` n `143` status `ready` deltaP `8.8116` edge `0.154` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7385` n `143` status `ready` deltaP `15.1245` edge `0.078` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0801` n `143` status `ready` deltaP `4.0519` edge `0.085` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0149` n `143` status `ready` deltaP `4.847` edge `0.019` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0955` n `143` status `ready` deltaP `15.9059` edge `0.3463` maxDD `-30.8239`
- `market_context_high->equity_1h` score `-0.3225` n `143` status `ready` deltaP `1.3526` edge `0.0474` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4384` n `143` status `ready` deltaP `5.8949` edge `0.0805` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5687` n `143` status `ready` deltaP `2.9993` edge `0.0057` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.571` n `143` status `ready` deltaP `-0.9463` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.5969` n `143` status `ready` deltaP `6.0917` edge `0.0698` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6263` n `143` status `ready` deltaP `0.5464` edge `0.0048` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6711` n `143` status `ready` deltaP `-1.3954` edge `-0.0014` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.9832` n `143` status `ready` deltaP `-1.5692` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2918` n `143` status `ready` deltaP `1.4242` edge `0.0169` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3044` n `142` status `ready` deltaP `-1.7116` edge `-0.0101` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

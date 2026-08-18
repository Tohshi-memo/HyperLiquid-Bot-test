# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T02:22:27.428704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `5.0084` n `73` status `ready` deltaP `18.0836` edge `0.4176` maxDD `-4.9964`
- `market_context_high->equity_24h` score `1.7025` n `73` status `ready` deltaP `15.7878` edge `0.046` maxDD `-0.4171`
- `market_context_high->commodity_4h` score `0.5899` n `110` status `ready` deltaP `12.2533` edge `0.0525` maxDD `-2.4692`
- `market_context_high->index_24h` score `0.5387` n `73` status `ready` deltaP `14.1046` edge `-0.033` maxDD `-0.2911`
- `market_context_high->commodity_24h` score `0.3767` n `73` status `ready` deltaP `12.6469` edge `0.1304` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.194` n `110` status `ready` deltaP `8.0648` edge `-0.0117` maxDD `-0.7386`
- `market_context_high->metal_24h` score `0.1778` n `73` status `ready` deltaP `4.8384` edge `0.0733` maxDD `-1.954`
- `market_context_high->index_1h` score `0.1546` n `110` status `ready` deltaP `7.809` edge `0.0028` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.0835` n `110` status `ready` deltaP `4.3876` edge `0.0203` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.2534` n `110` status `ready` deltaP `4.2295` edge `0.0014` maxDD `-0.3904`
- `market_context_high->crypto_major_4h` score `-0.4615` n `110` status `ready` deltaP `2.1065` edge `0.0475` maxDD `-4.6572`
- `market_context_high->metal_4h` score `-0.6291` n `110` status `ready` deltaP `5.7538` edge `-0.0131` maxDD `-3.8063`
- `market_context_high->metal_1h` score `-0.7282` n `110` status `ready` deltaP `-2.4279` edge `-0.0063` maxDD `-1.6698`
- `market_context_high->commodity_1h` score `-0.7662` n `110` status `ready` deltaP `-5.6042` edge `0.0004` maxDD `-1.5684`
- `market_context_high->fx_1h` score `-0.8342` n `110` status `ready` deltaP `-5.0163` edge `0.0001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.9029` n `110` status `ready` deltaP `-6.2944` edge `-0.0054` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-0.9195` n `110` status `ready` deltaP `-2.8661` edge `-0.0032` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-1.3084` n `73` status `ready` deltaP `-0.971` edge `-0.0911` maxDD `-1.6132`
- `market_context_high->crypto_alt_1h` score `-1.5218` n `110` status `ready` deltaP `-4.2461` edge `-0.0034` maxDD `-3.6085`
- `market_context_high->equity_4h` score `-1.9071` n `110` status `ready` deltaP `-9.806` edge `-0.0448` maxDD `-5.4127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

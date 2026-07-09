# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T15:37:27.081808+00:00`
- Price records: `672`
- Market context records: `6194`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.7046` n `32` status `ready` deltaP `42.2194` edge `0.792` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.8691` n `32` status `ready` deltaP `60.034` edge `0.1722` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0715` n `32` status `ready` deltaP `42.4487` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3739` n `32` status `ready` deltaP `28.5928` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1146` n `32` status `ready` deltaP `15.625` edge `0.2449` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8057` n `192` status `ready` deltaP `0.9138` edge `0.2452` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4086` n `32` status `ready` deltaP `14.4274` edge `0.1311` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7585` n `32` status `ready` deltaP `9.5247` edge `0.0799` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3115` n `192` status `ready` deltaP `-2.2813` edge `0.2944` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `0.1913` n `32` status `ready` deltaP `16.858` edge `-0.0759` maxDD `-0.3101`
- `market_context_high->metal_24h` score `0.052` n `192` status `ready` deltaP `19.8023` edge `0.1315` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1878` n `32` status `ready` deltaP `9.3112` edge `0.001` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2739` n `192` status `ready` deltaP `1.5095` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.5126` n `192` status `ready` deltaP `1.3203` edge `0.0402` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.6653` n `192` status `ready` deltaP `3.3831` edge `0.0109` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7273` n `192` status `ready` deltaP `-2.2455` edge `-0.001` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8151` n `32` status `ready` deltaP `-3.8922` edge `-0.0288` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.8911` n `192` status `ready` deltaP `4.5316` edge `0.0323` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9052` n `192` status `ready` deltaP `3.7955` edge `0.0339` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9132` n `192` status `ready` deltaP `1.3161` edge `-0.005` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

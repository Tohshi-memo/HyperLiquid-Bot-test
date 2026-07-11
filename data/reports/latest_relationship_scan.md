# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T17:22:28.198082+00:00`
- Price records: `672`
- Market context records: `6413`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5865`

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

- `news_risk_high->crypto_alt_24h` score `13.036` n `32` status `ready` deltaP `33.5069` edge `0.8777` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6895` n `32` status `ready` deltaP `56.4236` edge `0.1813` maxDD `0.0`
- `market_context_high->unknown_24h` score `4.6624` n `146` status `ready` deltaP `13.1492` edge `0.6309` maxDD `-15.0689`
- `news_risk_high->commodity_24h` score `4.2091` n `32` status `ready` deltaP `36.2847` edge `0.1294` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.2045` n `32` status `ready` deltaP `43.8262` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9089` n `32` status `ready` deltaP `15.1042` edge `0.4784` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5022` n `32` status `ready` deltaP `14.4274` edge `0.1431` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8497` n `32` status `ready` deltaP `10.2732` edge `0.0866` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.7062` n `206` status `ready` deltaP `-5.5709` edge `0.1968` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3796` n `206` status `ready` deltaP `11.1532` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1112` n `206` status `ready` deltaP `8.2051` edge `0.0222` maxDD `-0.4108`
- `market_context_high->metal_24h` score `-0.2859` n `146` status `ready` deltaP `18.5978` edge `0.0962` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.286` n `32` status `ready` deltaP `6.2313` edge `-0.0309` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.4831` n `206` status `ready` deltaP `2.0144` edge `0.0024` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6282` n `32` status `ready` deltaP `-0.8982` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7131` n `206` status `ready` deltaP `-3.0623` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7354` n `206` status `ready` deltaP `-0.8851` edge `-0.002` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.7469` n `206` status `ready` deltaP `-3.9605` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T20:07:16.898927+00:00`
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

- `market_context_high->unknown_1h` score `1.4652` n `149` status `ready` deltaP `6.1086` edge `0.1041` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8391` n `149` status `ready` deltaP `18.7418` edge `-0.0111` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0899` n `149` status `ready` deltaP `7.9022` edge `0.0091` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0204` n `149` status `ready` deltaP `6.8973` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1355` n `149` status `ready` deltaP `2.1169` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3291` n `149` status `ready` deltaP `4.8738` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3483` n `149` status `ready` deltaP `0.3306` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3557` n `149` status `ready` deltaP `7.3877` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5206` n `149` status `ready` deltaP `3.7823` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9039` n `149` status `ready` deltaP `-4.5384` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1219` n `149` status `ready` deltaP `-8.3219` edge `-0.0026` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.1682` n `133` status `ready` deltaP `0.0927` edge `0.0106` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.6989` n `149` status `ready` deltaP `-0.8226` edge `0.0693` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1159` n `133` status `ready` deltaP `-4.3794` edge `0.0362` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.5232` n `149` status `ready` deltaP `-2.5338` edge `-0.0439` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.7099` n `149` status `ready` deltaP `2.084` edge `-0.0929` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.6628` n `149` status `ready` deltaP `-5.6574` edge `-0.1198` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3156` n `133` status `ready` deltaP `-5.694` edge `-0.0346` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3499` n `133` status `ready` deltaP `-22.7679` edge `-0.2033` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.894` n `149` status `ready` deltaP `-1.151` edge `-0.3505` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T13:54:22.983266+00:00`
- Price records: `672`
- Market context records: `7146`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.5327` n `147` status `ready` deltaP `15.0583` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.182` n `157` status `ready` deltaP `4.102` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4462` n `157` status `ready` deltaP `-1.334` edge `0.0359` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6363` n `157` status `ready` deltaP `-0.3948` edge `0.0241` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6618` n `157` status `ready` deltaP `3.465` edge `0.0331` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.717` n `157` status `ready` deltaP `-2.0004` edge `-0.0165` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7654` n `157` status `ready` deltaP `1.1375` edge `-0.0049` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4101` n `157` status `ready` deltaP `-5.4579` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.6157` n `147` status `ready` deltaP `-5.8321` edge `0.0154` maxDD `-5.6933`
- `market_context_high->commodity_4h` score `-2.0129` n `147` status `ready` deltaP `-4.1262` edge `-0.0367` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8716` n `147` status `ready` deltaP `-9.2107` edge `-0.0119` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5753` n `157` status `ready` deltaP `-0.738` edge `-0.0438` maxDD `-15.2709`
- `market_context_high->index_4h` score `-3.8983` n `147` status `ready` deltaP `-1.2682` edge `-0.0465` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5` n `133` status `ready` deltaP `-13.4581` edge `-0.1544` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2165` n `147` status `ready` deltaP `0.3038` edge `-0.0024` maxDD `-25.0799`
- `market_context_high->crypto_alt_4h` score `-5.6303` n `147` status `ready` deltaP `-4.3533` edge `-0.0391` maxDD `-24.0853`
- `market_context_high->unknown_24h` score `-10.1203` n `133` status `ready` deltaP `-32.8765` edge `-0.1095` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.3845` n `147` status `ready` deltaP `-3.7435` edge `-0.2394` maxDD `-65.4151`
- `market_context_high->metal_24h` score `-14.6019` n `133` status `ready` deltaP `-30.7343` edge `-0.1938` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

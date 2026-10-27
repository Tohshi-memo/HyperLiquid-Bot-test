# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T07:37:28.572074+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9638`

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

- `market_context_high->unknown_4h` score `81.32` n `137` status `ready` deltaP `3.8377` edge `6.7786` maxDD `-0.8681`
- `market_context_high->unknown_1h` score `25.3097` n `137` status `ready` deltaP `0.7453` edge `2.1531` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.3899` n `120` status `ready` deltaP `24.4338` edge `0.0313` maxDD `-2.2694`
- `market_context_high->fx_1h` score `0.5203` n `137` status `ready` deltaP `11.351` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4704` n `137` status `ready` deltaP `13.3278` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1048` n `137` status `ready` deltaP `11.4625` edge `0.0117` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.2077` n `120` status `ready` deltaP `17.344` edge `0.1103` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.2485` n `137` status `ready` deltaP `2.6487` edge `0.0117` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4852` n `137` status `ready` deltaP `5.5487` edge `0.0291` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4912` n `120` status `ready` deltaP `10.9128` edge `0.0215` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.5468` n `137` status `ready` deltaP `0.1213` edge `-0.0018` maxDD `-1.5288`
- `market_context_high->commodity_4h` score `-0.6241` n `137` status `ready` deltaP `4.6154` edge `0.0391` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.7715` n `137` status `ready` deltaP `9.4234` edge `0.0017` maxDD `-4.7416`
- `market_context_high->equity_1h` score `-1.4097` n `137` status `ready` deltaP `2.5351` edge `0.0028` maxDD `-10.0347`
- `market_context_high->crypto_alt_1h` score `-2.063` n `137` status `ready` deltaP `-1.6577` edge `-0.009` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-2.2911` n `120` status `ready` deltaP `3.0142` edge `-0.0108` maxDD `-16.2421`
- `market_context_high->index_4h` score `-2.6501` n `137` status `ready` deltaP `-3.7654` edge `-0.0235` maxDD `-5.779`
- `market_context_high->crypto_major_4h` score `-3.6378` n `137` status `ready` deltaP `3.7742` edge `-0.0596` maxDD `-27.2224`
- `market_context_high->crypto_major_24h` score `-4.6445` n `120` status `ready` deltaP `-0.4997` edge `-0.1064` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.9844` n `137` status `ready` deltaP `3.2057` edge `-0.1146` maxDD `-36.3301`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

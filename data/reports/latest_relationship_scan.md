# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T16:07:38.108060+00:00`
- Price records: `672`
- Market context records: `8425`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6253.9032` n `52` status `ready` deltaP `41.7869` edge `520.9221` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.598` n `52` status `ready` deltaP `23.4756` edge `0.3697` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3067` n `52` status `ready` deltaP `19.1847` edge `0.0952` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1376` n `52` status `ready` deltaP `18.5976` edge `0.0732` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.574` n `52` status `ready` deltaP `12.4597` edge `0.0915` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.3209` n `52` status `ready` deltaP `9.6154` edge `0.0857` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.3013` n `52` status `ready` deltaP `5.1008` edge `0.2022` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0453` n `52` status `ready` deltaP `14.13` edge `0.179` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.1597` n `52` status `ready` deltaP `3.0605` edge `0.0397` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1335` n `52` status `ready` deltaP `6.0917` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0371` n `52` status `ready` deltaP `2.7983` edge `0.0133` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3952` n `52` status `ready` deltaP `5.1126` edge `0.011` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4194` n `52` status `ready` deltaP `0.5528` edge `0.0017` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9501` n `52` status `ready` deltaP `-6.4717` edge `-0.0408` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7325` n `52` status `ready` deltaP `-27.7244` edge `-0.0607` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3657` n `52` status `ready` deltaP `-25.9029` edge `-0.1937` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.6584` n `52` status `ready` deltaP `-34.7088` edge `-0.2131` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.5408` n `52` status `ready` deltaP `-12.4332` edge `-0.3682` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.6548` n `52` status `ready` deltaP `-27.0299` edge `-0.3241` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-36.059` n `52` status `ready` deltaP `-25.1202` edge `-1.0499` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

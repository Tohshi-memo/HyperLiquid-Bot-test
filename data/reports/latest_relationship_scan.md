# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T21:07:32.024254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->metal_24h` score `1.3557` n `118` status `ready` deltaP `7.3152` edge `0.1218` maxDD `-2.2743`
- `market_context_high->equity_24h` score `1.1796` n `118` status `ready` deltaP `3.1486` edge `0.3833` maxDD `-21.1456`
- `market_context_high->commodity_4h` score `1.1316` n `143` status `ready` deltaP `14.5947` edge `0.0643` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7572` n `151` status `ready` deltaP `10.4553` edge `0.0277` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6015` n `118` status `ready` deltaP `20.7274` edge `0.0256` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.0582` n `118` status `ready` deltaP `5.6115` edge `0.1232` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4937` n `151` status `ready` deltaP `1.846` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.5911` n `151` status `ready` deltaP `-3.0307` edge `-0.006` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7404` n `143` status `ready` deltaP `2.7791` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.8318` n `151` status `ready` deltaP `-3.7336` edge `-0.0055` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.9574` n `143` status `ready` deltaP `-1.5254` edge `-0.0091` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9707` n `151` status `ready` deltaP `-0.4095` edge `0.0047` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0209` n `143` status `ready` deltaP `-1.9657` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.871` n `151` status `ready` deltaP `-9.44` edge `-0.0288` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5782` n `143` status `ready` deltaP `-2.0286` edge `-0.0676` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3109` n `151` status `ready` deltaP `-12.2972` edge `-0.0606` maxDD `-7.333`
- `market_context_high->crypto_alt_4h` score `-4.1316` n `143` status `ready` deltaP `-9.0387` edge `-0.1184` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.2509` n `118` status `ready` deltaP `2.0069` edge `-0.1182` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.569` n `118` status `ready` deltaP `-16.0164` edge `-0.213` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.945` n `151` status `ready` deltaP `-7.6159` edge `-0.5666` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

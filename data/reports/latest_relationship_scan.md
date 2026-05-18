# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T01:07:15.159251+00:00`
- Price records: `672`
- Market context records: `1069`
- Flow alert records: `4981`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.6768` n `168` status `ready` deltaP `34.6428` edge `1.1218` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.33` n `168` status `ready` deltaP `11.9048` edge `0.4882` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.6348` n `168` status `ready` deltaP `13.619` edge `0.3451` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.979` n `168` status `ready` deltaP `14.1428` edge `0.2681` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.6188` n `168` status `ready` deltaP `-3.8571` edge `0.494` maxDD `-6.3373`
- `market_context_high->equity_4h` score `0.9715` n `170` status `ready` deltaP `5.6976` edge `0.1218` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.3851` n `170` status `ready` deltaP `4.2594` edge `0.072` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.1717` n `170` status `ready` deltaP `10.59` edge `0.1316` maxDD `-8.0311`
- `market_context_high->index_1h` score `0.0532` n `170` status `ready` deltaP `5.6287` edge `0.0184` maxDD `-1.7857`
- `market_context_high->fx_1h` score `-0.0671` n `170` status `ready` deltaP `5.5301` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.0723` n `170` status `ready` deltaP `8.6316` edge `0.0288` maxDD `-5.3898`
- `market_context_high->equity_1h` score `-0.2013` n `170` status `ready` deltaP `1.6291` edge `0.0384` maxDD `-3.6162`
- `market_context_high->metal_1h` score `-0.3865` n `170` status `ready` deltaP `6.0655` edge `-0.014` maxDD `-3.4119`
- `market_context_high->fx_4h` score `-0.7026` n `170` status `ready` deltaP `1.0904` edge `0.0023` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-0.8071` n `170` status `ready` deltaP `2.825` edge `0.0225` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-1.0169` n `170` status `ready` deltaP `-1.4336` edge `0.0056` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.3433` n `170` status `ready` deltaP `4.3633` edge `0.1094` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.2029` n `170` status `ready` deltaP `2.2919` edge `-0.1023` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.713` n `170` status `ready` deltaP `-8.108` edge `0.023` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0414` n `168` status `ready` deltaP `5.7619` edge `-0.0207` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

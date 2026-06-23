# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T18:52:37.202694+00:00`
- Price records: `672`
- Market context records: `4544`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `56.4846` n `170` status `ready` deltaP `7.3495` edge `4.7081` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.3219` n `168` status `ready` deltaP `8.268` edge `2.6283` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4386` n `168` status `ready` deltaP `7.4115` edge `0.0026` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6498` n `170` status `ready` deltaP `-0.6429` edge `0.0129` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.6713` n `170` status `ready` deltaP `0.3628` edge `-0.0029` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.9569` n `168` status `ready` deltaP `3.7021` edge `0.0725` maxDD `-8.8203`
- `market_context_high->index_4h` score `-1.0002` n `168` status `ready` deltaP `0.9364` edge `-0.0097` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-1.0678` n `170` status `ready` deltaP `-1.9778` edge `0.0229` maxDD `-5.5624`
- `market_context_high->index_1h` score `-1.0717` n `170` status `ready` deltaP `-3.7108` edge `-0.0118` maxDD `-2.7358`
- `market_context_high->commodity_4h` score `-1.3594` n `168` status `ready` deltaP `2.1269` edge `0.0223` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.6953` n `168` status `ready` deltaP `2.5545` edge `-0.1493` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.5824` n `170` status `ready` deltaP `-4.8239` edge `-0.0818` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.42` n `170` status `ready` deltaP `-3.4114` edge `-0.1002` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4201` n `168` status `ready` deltaP `-12.8473` edge `-0.0148` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6852` n `168` status `ready` deltaP `-8.9534` edge `-0.1317` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.372` n `170` status `ready` deltaP `-4.727` edge `-0.1242` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3406` n `168` status `ready` deltaP `4.7371` edge `0.0105` maxDD `-46.3041`
- `market_context_high->crypto_alt_4h` score `-13.3056` n `168` status `ready` deltaP `-1.6623` edge `-0.232` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.3908` n `168` status `ready` deltaP `-0.9176` edge `-0.2427` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.6193` n `168` status `ready` deltaP `-6.9759` edge `-0.3202` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

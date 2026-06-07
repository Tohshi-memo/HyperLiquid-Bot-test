# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T14:07:22.619572+00:00`
- Price records: `672`
- Market context records: `3184`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.7581` n `105` status `ready` deltaP `47.4206` edge `0.8732` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.6749` n `105` status `ready` deltaP `15.0893` edge `2.3938` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.6016` n `105` status `ready` deltaP `19.4296` edge `0.9093` maxDD `-3.7624`
- `market_context_high->index_24h` score `6.2736` n `105` status `ready` deltaP `30.2777` edge `0.8579` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6374` n `105` status `ready` deltaP `13.2391` edge `1.3479` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1508` n `136` status `ready` deltaP `20.2295` edge `0.1735` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6715` n `105` status `ready` deltaP `11.4931` edge `0.0021` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5575` n `136` status `ready` deltaP `11.3971` edge `0.1927` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3612` n `140` status `ready` deltaP `6.1292` edge `0.0315` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3346` n `140` status `ready` deltaP `6.4628` edge `0.0203` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5086` n `140` status `ready` deltaP `5.633` edge `0.1102` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7704` n `136` status `ready` deltaP `17.3153` edge `0.0767` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0687` n `140` status `ready` deltaP `3.1309` edge `0.0684` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2717` n `140` status `ready` deltaP `4.1702` edge `0.0148` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3196` n `136` status `ready` deltaP `-11.1012` edge `-0.0067` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6359` n `140` status `ready` deltaP `-9.367` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0966` n `140` status `ready` deltaP `-4.1018` edge `-0.008` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3717` n `136` status `ready` deltaP `16.6517` edge `0.3894` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1075` n `140` status `ready` deltaP `2.6519` edge `-0.074` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7375` n `136` status `ready` deltaP `9.765` edge `0.2481` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T14:22:21.689268+00:00`
- Price records: `672`
- Market context records: `3186`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9761`

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

- `market_context_high->commodity_24h` score `13.7809` n `105` status `ready` deltaP `47.4206` edge `0.8751` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.7631` n `105` status `ready` deltaP `19.6032` edge `0.9216` maxDD `-3.7624`
- `market_context_high->crypto_alt_24h` score `11.6371` n `105` status `ready` deltaP `14.9157` edge `2.3901` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2712` n `105` status `ready` deltaP `30.2777` edge `0.8576` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5933` n `105` status `ready` deltaP `13.0655` edge `1.3434` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1719` n `137` status `ready` deltaP `20.4335` edge `0.1739` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6552` n `105` status `ready` deltaP `11.3195` edge `0.0019` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5402` n `137` status `ready` deltaP `11.4808` edge `0.1907` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3744` n `140` status `ready` deltaP `6.2789` edge `0.0316` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3369` n `140` status `ready` deltaP `6.4628` edge `0.02` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5156` n `140` status `ready` deltaP `5.633` edge `0.1093` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7366` n `137` status `ready` deltaP `17.546` edge `0.0795` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0758` n `140` status `ready` deltaP `3.1309` edge `0.0675` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2825` n `140` status `ready` deltaP `4.1702` edge `0.0139` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3028` n `137` status `ready` deltaP `-10.792` edge `-0.0066` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6359` n `140` status `ready` deltaP `-9.367` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.1109` n `140` status `ready` deltaP `-4.2515` edge `-0.0082` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.4083` n `137` status `ready` deltaP `16.2331` edge `0.3875` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1075` n `140` status `ready` deltaP `2.6519` edge `-0.074` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.7681` n `137` status `ready` deltaP `9.4323` edge `0.2464` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

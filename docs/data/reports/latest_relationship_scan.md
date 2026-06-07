# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T21:22:20.102071+00:00`
- Price records: `672`
- Market context records: `3217`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11250`

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

- `market_context_high->commodity_24h` score `13.6623` n `102` status `ready` deltaP `47.9473` edge `0.8617` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1714` n `102` status `ready` deltaP `15.0225` edge `2.4579` maxDD `-71.142`
- `market_context_high->index_24h` score `9.3722` n `102` status `ready` deltaP `29.3198` edge `0.841` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.4984` n `102` status `ready` deltaP `14.2872` edge `1.4513` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4052` n `128` status `ready` deltaP `22.8849` edge `0.177` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.2964` n `140` status `ready` deltaP `5.9795` edge `0.0271` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.4655` n `102` status `ready` deltaP `3.9012` edge `-0.0107` maxDD `-1.3328`
- `market_context_high->unknown_4h` score `-0.6653` n `128` status `ready` deltaP `8.2317` edge `0.0864` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.8878` n `140` status `ready` deltaP `3.3747` edge `0.0098` maxDD `-4.5023`
- `market_context_high->crypto_major_1h` score `-1.0628` n `140` status `ready` deltaP `3.9948` edge `0.0634` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0766` n `128` status `ready` deltaP `-6.593` edge `-0.0056` maxDD `-1.4115`
- `market_context_high->crypto_alt_1h` score `-1.4292` n `140` status `ready` deltaP `4.3884` edge `0.0771` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.6656` n `140` status `ready` deltaP `2.6262` edge `0.0006` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.7358` n `140` status `ready` deltaP `-10.6459` edge `-0.005` maxDD `-0.8278`
- `market_context_high->index_4h` score `-1.9479` n `128` status `ready` deltaP `11.5473` edge `0.0516` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.2736` n `140` status `ready` deltaP `-4.5509` edge `-0.011` maxDD `-8.1833`
- `market_context_high->unknown_1h` score `-2.7802` n `140` status `ready` deltaP `1.5227` edge `-0.1187` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-2.89` n `102` status `ready` deltaP `15.0021` edge `1.796` maxDD `-164.3217`
- `market_context_high->crypto_major_4h` score `-5.0284` n `128` status `ready` deltaP `2.8963` edge `0.1284` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-5.2719` n `128` status `ready` deltaP `10.8804` edge `0.0187` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

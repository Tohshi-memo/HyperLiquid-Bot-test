# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T14:37:15.846440+00:00`
- Price records: `672`
- Market context records: `1021`
- Flow alert records: `4848`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `13.6849` n `192` status `ready` deltaP `32.5448` edge `0.9823` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3741` n `192` status `ready` deltaP `11.1614` edge `0.4135` maxDD `-9.5387`
- `market_context_high->equity_24h` score `1.4235` n `192` status `ready` deltaP `8.3723` edge `0.2223` maxDD `-6.7591`
- `market_context_high->index_24h` score `1.0136` n `192` status `ready` deltaP `7.6957` edge `0.1797` maxDD `-4.0567`
- `market_context_high->fx_1h` score `-0.1391` n `192` status `ready` deltaP `4.07` edge `0.0006` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4994` n `192` status `ready` deltaP `2.3952` edge `0.0232` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6975` n `192` status `ready` deltaP `2.5168` edge `0.0062` maxDD `-2.4884`
- `market_context_high->equity_1h` score `-0.7493` n `192` status `ready` deltaP `-0.5365` edge `0.018` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.8704` n `192` status `ready` deltaP `3.5569` edge `0.0034` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2654` n `192` status `ready` deltaP `4.675` edge `-0.0211` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3287` n `192` status `ready` deltaP `2.1723` edge `0.09` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3515` n `192` status `ready` deltaP `-1.0791` edge `-0.0221` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.3825` n `192` status `ready` deltaP `0.3049` edge `0.0304` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.7391` n `192` status `ready` deltaP `0.9325` edge `-0.0389` maxDD `-8.5553`
- `market_context_high->crypto_alt_4h` score `-2.6531` n `192` status `ready` deltaP `0.813` edge `0.0513` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.723` n `192` status `ready` deltaP `7.6473` edge `0.0927` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2644` n `192` status `ready` deltaP `1.3678` edge `-0.02` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.3659` n `192` status `ready` deltaP `-3.125` edge `0.0571` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.1045` n `192` status `ready` deltaP `-2.0707` edge `-0.1579` maxDD `-21.6945`
- `market_context_high->metal_24h` score `-4.5364` n `192` status `ready` deltaP `-8.2506` edge `0.2755` maxDD `-38.2156`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

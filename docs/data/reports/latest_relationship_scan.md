# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T05:22:34.513580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `76.9215` n `146` status `ready` deltaP `3.4477` edge `6.4207` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `15.925` n `146` status `ready` deltaP `0.8408` edge `1.3704` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.493` n `122` status `ready` deltaP `20.9109` edge `0.0246` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4323` n `146` status `ready` deltaP `12.9406` edge `0.0096` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3991` n `146` status `ready` deltaP `9.8659` edge `0.0033` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1228` n `122` status `ready` deltaP `21.0898` edge `0.1277` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0553` n `146` status `ready` deltaP `10.719` edge `0.0103` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `0.0111` n `146` status `ready` deltaP `4.9032` edge `0.0183` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2129` n `122` status `ready` deltaP `15.8011` edge `0.0246` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4101` n `146` status `ready` deltaP `6.6927` edge `0.0441` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.5766` n `146` status `ready` deltaP `5.4343` edge `0.0297` maxDD `-7.8544`
- `market_context_high->index_1h` score `-0.6188` n `146` status `ready` deltaP `-0.5578` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.742` n `146` status `ready` deltaP `10.1361` edge `0.0015` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.6448` n `146` status `ready` deltaP `2.2865` edge `0.0015` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.8703` n `146` status `ready` deltaP `-0.1128` edge `0.0054` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-3.1769` n `122` status `ready` deltaP `-0.8409` edge `-0.0575` maxDD `-19.5349`
- `market_context_high->index_4h` score `-3.3774` n `146` status `ready` deltaP `-5.9326` edge `-0.0267` maxDD `-6.5496`
- `market_context_high->crypto_major_24h` score `-3.8258` n `122` status `ready` deltaP `2.0584` edge `-0.0185` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.0558` n `146` status `ready` deltaP `1.0671` edge `-0.0697` maxDD `-29.2576`
- `market_context_high->equity_4h` score `-6.2932` n `146` status `ready` deltaP `0.236` edge `-0.1528` maxDD `-42.1141`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

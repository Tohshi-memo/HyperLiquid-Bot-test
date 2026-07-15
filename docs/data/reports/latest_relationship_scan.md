# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T18:22:33.705313+00:00`
- Price records: `672`
- Market context records: `6841`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `0.9935` n `176` status `ready` deltaP `-1.5467` edge `0.5129` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.0458` n `176` status `ready` deltaP `8.4912` edge `0.1264` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2463` n `218` status `ready` deltaP `2.284` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5223` n `218` status `ready` deltaP `2.3993` edge `0.0169` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5247` n `218` status `ready` deltaP `4.3839` edge `0.0172` maxDD `-4.2122`
- `market_context_high->index_1h` score `-0.8791` n `218` status `ready` deltaP `-2.593` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0082` n `218` status `ready` deltaP `-6.3108` edge `-0.0104` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0483` n `207` status `ready` deltaP `10.0772` edge `0.0048` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0532` n `218` status `ready` deltaP `-2.2647` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6911` n `218` status `ready` deltaP `-3.7082` edge `-0.0261` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.976` n `218` status `ready` deltaP `-0.092` edge `-0.0347` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2482` n `207` status `ready` deltaP `0.6518` edge `-0.0346` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-2.3677` n `207` status `ready` deltaP `-4.7138` edge `-0.0169` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7271` n `207` status `ready` deltaP `-3.5267` edge `-0.0278` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9373` n `207` status `ready` deltaP `0.1708` edge `-0.045` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1433` n `207` status `ready` deltaP `-0.1104` edge `-0.0439` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3048` n `207` status `ready` deltaP `-10.086` edge `0.0284` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4684` n `176` status `ready` deltaP `-9.7853` edge `-0.0035` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9906` n `207` status `ready` deltaP `-1.8669` edge `-0.2222` maxDD `-56.1828`
- `market_context_high->metal_24h` score `-9.2278` n `176` status `ready` deltaP `-18.8447` edge `-0.2089` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

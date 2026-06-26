# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T05:52:35.252417+00:00`
- Price records: `672`
- Market context records: `4798`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7619` n `122` status `ready` deltaP `19.3298` edge `0.639` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4128` n `115` status `ready` deltaP `13.6654` edge `0.2023` maxDD `-4.7201`
- `market_context_high->unknown_1h` score `0.4621` n `122` status `ready` deltaP `12.2804` edge `-0.0016` maxDD `-1.674`
- `market_context_high->commodity_1h` score `0.0758` n `122` status `ready` deltaP `5.3818` edge `0.0292` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.037` n `122` status `ready` deltaP `11.6628` edge `0.0442` maxDD `-4.377`
- `market_context_high->equity_4h` score `0.0319` n `122` status `ready` deltaP `8.9964` edge `0.1127` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.2946` n `122` status `ready` deltaP `7.7569` edge `0.0174` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4068` n `122` status `ready` deltaP `3.4311` edge `0.0026` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6815` n `122` status `ready` deltaP `1.8676` edge `0.0075` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8597` n `122` status `ready` deltaP `-0.5841` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.35` n `122` status `ready` deltaP `-1.0479` edge `-0.0051` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.028` n `115` status `ready` deltaP `20.5918` edge `0.1136` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2143` n `122` status `ready` deltaP `-0.4982` edge `-0.063` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.0668` n `122` status `ready` deltaP `1.3473` edge `-0.0406` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.1262` n `115` status `ready` deltaP `-12.9529` edge `-0.0192` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4012` n `122` status `ready` deltaP `1.1338` edge `-0.0653` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.67` n `122` status `ready` deltaP `5.5078` edge `0.007` maxDD `-46.0617`
- `market_context_high->index_24h` score `-7.0676` n `115` status `ready` deltaP `-8.9388` edge `-0.132` maxDD `-23.7901`
- `market_context_high->crypto_major_4h` score `-7.9587` n `122` status `ready` deltaP `4.2683` edge `-0.1257` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2207` n `122` status `ready` deltaP `7.2971` edge `-0.2785` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

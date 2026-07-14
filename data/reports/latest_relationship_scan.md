# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T00:07:31.884303+00:00`
- Price records: `672`
- Market context records: `6656`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.3954` n `202` status `ready` deltaP `-5.4114` edge `0.3258` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1751` n `202` status `ready` deltaP `12.1416` edge `0.2038` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1037` n `202` status `ready` deltaP `8.6115` edge `0.0502` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0361` n `202` status `ready` deltaP `6.1822` edge `0.0447` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.2275` n `202` status `ready` deltaP `-3.9364` edge `0.3723` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2513` n `202` status `ready` deltaP `2.6724` edge `0.0007` maxDD `-0.7249`
- `market_context_high->unknown_4h` score `-0.4463` n `202` status `ready` deltaP `-14.6583` edge `0.3011` maxDD `-10.5788`
- `market_context_high->index_1h` score `-0.4611` n `202` status `ready` deltaP `1.0138` edge `0.0059` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6953` n `202` status `ready` deltaP `-1.6704` edge `-0.0097` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7558` n `202` status `ready` deltaP `11.5009` edge `0.0144` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.792` n `202` status `ready` deltaP `3.615` edge `0.0126` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9348` n `202` status `ready` deltaP `11.7318` edge `0.1334` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1253` n `202` status `ready` deltaP `-3.1882` edge `0.0016` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.2363` n `202` status `ready` deltaP `9.0271` edge `0.1215` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4122` n `202` status `ready` deltaP `5.9481` edge `0.0005` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4489` n `202` status `ready` deltaP `-1.3765` edge `-0.0271` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9478` n `202` status `ready` deltaP `0.7697` edge `0.0312` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3558` n `202` status `ready` deltaP `8.9139` edge `0.0045` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3776` n `202` status `ready` deltaP `-12.1895` edge `-0.0103` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.7788` n `202` status `ready` deltaP `-4.5531` edge `0.0098` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

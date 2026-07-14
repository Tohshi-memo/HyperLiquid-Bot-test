# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T00:22:25.880686+00:00`
- Price records: `672`
- Market context records: `6657`
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

- `market_context_high->unknown_1h` score `2.3942` n `202` status `ready` deltaP `-5.4114` edge `0.3257` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1679` n `202` status `ready` deltaP `12.1416` edge `0.2032` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1044` n `202` status `ready` deltaP `8.6115` edge `0.0503` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0337` n `202` status `ready` deltaP `6.1822` edge `0.0449` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.2251` n `202` status `ready` deltaP `-3.9364` edge `0.3726` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2513` n `202` status `ready` deltaP `2.6724` edge `0.0007` maxDD `-0.7249`
- `market_context_high->unknown_4h` score `-0.4077` n `202` status `ready` deltaP `-14.5058` edge `0.3033` maxDD `-10.5788`
- `market_context_high->index_1h` score `-0.4533` n `202` status `ready` deltaP `1.1635` edge `0.0059` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6977` n `202` status `ready` deltaP `-1.6704` edge `-0.01` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7574` n `202` status `ready` deltaP `11.5009` edge `0.0142` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.7956` n `202` status `ready` deltaP `3.615` edge `0.0123` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9371` n `202` status `ready` deltaP `11.7318` edge `0.1331` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1122` n `202` status `ready` deltaP `-3.0385` edge `0.0017` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.2363` n `202` status `ready` deltaP `9.0271` edge `0.1215` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4035` n `202` status `ready` deltaP `6.1006` edge `0.0006` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4535` n `202` status `ready` deltaP `-1.3765` edge `-0.0277` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9486` n `202` status `ready` deltaP `0.7697` edge `0.0311` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.369` n `202` status `ready` deltaP `8.9139` edge `0.0034` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3812` n `202` status `ready` deltaP `-12.1895` edge `-0.0106` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.7803` n `202` status `ready` deltaP `-4.5531` edge `0.0096` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

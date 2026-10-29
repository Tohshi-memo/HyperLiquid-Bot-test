# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T14:22:30.940871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7060`

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

- `market_context_high->unknown_24h` score `1434.3233` n `141` status `ready` deltaP `-2.438` edge `119.6231` maxDD `-4.0588`
- `market_context_high->unknown_4h` score `49.7603` n `141` status `ready` deltaP `6.117` edge `4.1192` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.6692` n `141` status `ready` deltaP `22.6803` edge `0.008` maxDD `-0.2748`
- `market_context_high->commodity_4h` score `0.2715` n `141` status `ready` deltaP `13.4255` edge `0.055` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.0589` n `141` status `ready` deltaP `5.9891` edge `0.0008` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0195` n `141` status `ready` deltaP `8.8727` edge `0.0077` maxDD `-0.881`
- `market_context_high->fx_4h` score `-0.2209` n `141` status `ready` deltaP `4.5635` edge `0.0011` maxDD `-0.4545`
- `market_context_high->metal_4h` score `-0.2226` n `141` status `ready` deltaP `10.8069` edge `0.0061` maxDD `-3.2012`
- `market_context_high->commodity_1h` score `-0.3843` n `141` status `ready` deltaP `1.1031` edge `0.0128` maxDD `-0.5075`
- `market_context_high->index_1h` score `-0.702` n `141` status `ready` deltaP `-3.4983` edge `-0.0025` maxDD `-1.1344`
- `market_context_high->crypto_major_1h` score `-0.8739` n `141` status `ready` deltaP `4.2712` edge `0.024` maxDD `-6.6905`
- `market_context_high->equity_1h` score `-0.9553` n `141` status `ready` deltaP `-0.0945` edge `0.0131` maxDD `-5.7954`
- `market_context_high->fx_24h` score `-0.9737` n `141` status `ready` deltaP `5.8695` edge `0.0128` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.558` n `141` status `ready` deltaP `1.4099` edge `0.0103` maxDD `-10.889`
- `market_context_high->metal_24h` score `-2.043` n `141` status `ready` deltaP `1.7398` edge `-0.0005` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.7367` n `141` status `ready` deltaP `-8.8382` edge `-0.0276` maxDD `-4.323`
- `market_context_high->equity_4h` score `-3.0631` n `141` status `ready` deltaP `-3.7083` edge `-0.0764` maxDD `-16.6602`
- `market_context_high->crypto_major_4h` score `-3.17` n `141` status `ready` deltaP `2.8736` edge `-0.0416` maxDD `-23.3842`
- `market_context_high->crypto_major_24h` score `-3.9566` n `141` status `ready` deltaP `-4.5656` edge `0.0089` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.1494` n `141` status `ready` deltaP `5.659` edge `-0.1078` maxDD `-14.0571`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

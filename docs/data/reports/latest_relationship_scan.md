# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T10:22:25.358372+00:00`
- Price records: `672`
- Market context records: `6699`
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

- `market_context_high->unknown_24h` score `0.8709` n `184` status `ready` deltaP `0.5208` edge `0.4834` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1651` n `184` status `ready` deltaP `8.9788` edge `0.0473` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0607` n `184` status `ready` deltaP `5.9067` edge `0.0421` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `0.0604` n `184` status `ready` deltaP `9.4279` edge `0.129` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3756` n `184` status `ready` deltaP `0.1985` edge `0.0004` maxDD `-0.6567`
- `market_context_high->unknown_1h` score `-0.5257` n `184` status `ready` deltaP `-6.7658` edge `0.0914` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.5461` n `184` status `ready` deltaP `-0.2831` edge `0.0033` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.563` n `184` status `ready` deltaP `-3.1893` edge `0.0016` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6771` n `184` status `ready` deltaP `-0.9307` edge `-0.0123` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9927` n `184` status `ready` deltaP `9.3452` edge `-0.0016` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0331` n `184` status `ready` deltaP `2.7011` edge `-0.0014` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3214` n `184` status `ready` deltaP `6.9923` edge `-0.0011` maxDD `-2.8612`
- `market_context_high->crypto_major_4h` score `-1.6488` n `184` status `ready` deltaP `7.0454` edge `0.0731` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8088` n `184` status `ready` deltaP `-5.4481` edge `-0.0461` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8695` n `184` status `ready` deltaP `5.1299` edge `0.0663` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2871` n `184` status `ready` deltaP `-3.4001` edge `0.0155` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.0502` n `184` status `ready` deltaP `-17.4245` edge `0.0152` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.6712` n `184` status `ready` deltaP `-9.3825` edge `-0.0025` maxDD `-7.2707`
- `market_context_high->equity_4h` score `-5.5115` n `184` status `ready` deltaP `5.9584` edge `-0.0721` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.1032` n `184` status `ready` deltaP `-7.1332` edge `-0.0146` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

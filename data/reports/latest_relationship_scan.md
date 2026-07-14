# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T06:07:28.468631+00:00`
- Price records: `672`
- Market context records: `6681`
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

- `market_context_high->unknown_1h` score `2.4377` n `200` status `ready` deltaP `-4.7485` edge `0.3249` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.0972` n `200` status `ready` deltaP `11.9931` edge `0.1983` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.788` n `200` status `ready` deltaP `-13.3598` edge `0.3953` maxDD `-10.5788`
- `market_context_high->crypto_major_1h` score `0.0832` n `200` status `ready` deltaP `7.7036` edge `0.0453` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0811` n `200` status `ready` deltaP `5.1048` edge `0.0398` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.1171` n `200` status `ready` deltaP `-3.4792` edge `0.3834` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2589` n `200` status `ready` deltaP `2.3892` edge `0.0011` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.537` n `200` status `ready` deltaP `-0.003` edge `0.0026` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6016` n `200` status `ready` deltaP `-0.0928` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.88` n `200` status `ready` deltaP `10.4329` edge `0.0056` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9747` n `200` status `ready` deltaP `3.1018` edge `0.0008` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.138` n `200` status `ready` deltaP `-4.5539` edge `-0.0011` maxDD `-1.4032`
- `market_context_high->fx_4h` score `-1.393` n `200` status `ready` deltaP `6.4085` edge `-0.0001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4026` n `200` status `ready` deltaP `9.1098` edge `0.0909` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.4959` n `200` status `ready` deltaP `-1.8171` edge `-0.0302` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6752` n `200` status `ready` deltaP `6.5427` edge `0.0818` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1523` n `200` status `ready` deltaP `-1.5732` edge `0.0206` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1591` n `200` status `ready` deltaP `7.6341` edge `-0.029` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.2196` n `200` status `ready` deltaP `-12.0347` edge `-0.0117` maxDD `-10.4428`
- `market_context_high->metal_24h` score `-6.9952` n `200` status `ready` deltaP `-6.2847` edge `-0.0064` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

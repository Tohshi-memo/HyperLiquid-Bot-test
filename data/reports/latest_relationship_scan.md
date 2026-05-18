# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T23:07:13.809388+00:00`
- Price records: `672`
- Market context records: `1164`
- Flow alert records: `5252`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.8221` n `140` status `ready` deltaP `45.5804` edge `1.5445` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1791` n `140` status `ready` deltaP `21.989` edge `0.9033` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7138` n `140` status `ready` deltaP `21.4682` edge `0.5927` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.8209` n `140` status `ready` deltaP `20.0793` edge `0.407` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5` n `140` status `ready` deltaP `-3.4127` edge `0.6478` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4418` n `156` status `ready` deltaP `12.242` edge `0.1882` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0931` n `156` status `ready` deltaP `8.6695` edge `0.1016` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.4825` n `140` status `ready` deltaP `3.0556` edge `0.2928` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.4332` n `156` status `ready` deltaP `7.1242` edge `0.0203` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2292` n `156` status `ready` deltaP `2.5295` edge `0.04` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1902` n `156` status `ready` deltaP `9.078` edge `0.0009` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1717` n `156` status `ready` deltaP `8.9744` edge `0.1543` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.0016` n `156` status `ready` deltaP `6.986` edge `0.0302` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3282` n `156` status `ready` deltaP `2.7944` edge `0.0383` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.4225` n `156` status `ready` deltaP `5.8691` edge `-0.0133` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.8534` n `156` status `ready` deltaP `-3.589` edge `-0.0047` maxDD `-3.7959`
- `market_context_high->unknown_4h` score `-0.8832` n `156` status `ready` deltaP `6.3829` edge `0.0055` maxDD `-6.7322`
- `market_context_high->fx_4h` score `-0.9764` n `156` status `ready` deltaP `-3.2598` edge `-0.0038` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.2129` n `156` status `ready` deltaP `4.4989` edge `0.111` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.869` n `156` status `ready` deltaP `5.2338` edge `-0.0791` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

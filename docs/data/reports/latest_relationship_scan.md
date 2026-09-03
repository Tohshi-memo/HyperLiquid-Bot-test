# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T08:22:27.919161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11569`

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

- `risk_on_high->unknown_4h` score `36.7879` n `123` status `ready` deltaP `15.1931` edge `3.0262` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.7879` n `123` status `ready` deltaP `15.1931` edge `3.0262` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.6267` n `162` status `ready` deltaP `12.6788` edge `2.2039` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.763` n `133` status `ready` deltaP `2.5392` edge `1.6877` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.763` n `133` status `ready` deltaP `2.5392` edge `1.6877` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.8492` n `174` status `ready` deltaP `1.4935` edge `1.2072` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.5527` n `107` status `ready` deltaP `21.2714` edge `0.6521` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.5527` n `107` status `ready` deltaP `21.2714` edge `0.6521` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3213` n `107` status `ready` deltaP `21.4304` edge `0.8451` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3213` n `107` status `ready` deltaP `21.4304` edge `0.8451` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2923` n `59` status `ready` deltaP `21.3512` edge `0.445` maxDD `-19.4761`
- `market_context_high->equity_24h` score `1.6811` n `144` status `ready` deltaP `18.4027` edge `0.5477` maxDD `-22.3889`
- `news_risk_high->crypto_major_24h` score `1.6721` n `59` status `ready` deltaP `14.6952` edge `0.4797` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.5528` n `59` status `ready` deltaP `7.221` edge `0.328` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.9345` n `107` status `ready` deltaP `21.0313` edge `0.854` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9345` n `107` status `ready` deltaP `21.0313` edge `0.854` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5786` n `144` status `ready` deltaP `23.2639` edge `0.8655` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.5302` n `144` status `ready` deltaP `15.2777` edge `0.716` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.251` n `67` status `ready` deltaP `5.4901` edge `0.0315` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.3649` edge `0.0031` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

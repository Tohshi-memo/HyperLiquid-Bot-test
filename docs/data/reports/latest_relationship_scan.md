# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T10:22:27.363706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `37.1021` n `131` status `ready` deltaP `13.9906` edge `3.0604` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `37.1021` n `131` status `ready` deltaP `13.9906` edge `3.0604` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.647` n `164` status `ready` deltaP `11.128` edge `2.3826` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7246` n `133` status `ready` deltaP `2.5392` edge `1.6845` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7246` n `133` status `ready` deltaP `2.5392` edge `1.6845` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7076` n `176` status `ready` deltaP `1.8984` edge `1.1927` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.9796` n `107` status `ready` deltaP `19.8825` edge `0.6136` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.9796` n `107` status `ready` deltaP `19.8825` edge `0.6136` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.056` n `138` status `ready` deltaP `19.4897` edge `0.5593` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `1.9457` n `107` status `ready` deltaP `20.0416` edge `0.8062` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.9457` n `107` status `ready` deltaP `20.0416` edge `0.8062` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.9167` n `59` status `ready` deltaP `19.9624` edge `0.4061` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.2347` n `59` status `ready` deltaP `13.6535` edge `0.4502` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `0.9797` n `59` status `ready` deltaP `5.8321` edge `0.2895` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `0.8535` n `138` status `ready` deltaP `16.4252` edge `0.7498` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.6502` n `107` status `ready` deltaP `19.9896` edge `0.8245` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.6502` n `107` status `ready` deltaP `19.9896` edge `0.8245` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5849` n `138` status `ready` deltaP `23.4299` edge `0.8652` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2629` n `67` status `ready` deltaP `5.6425` edge `0.032` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0595` n `133` status `ready` deltaP `11.3649` edge `0.0031` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

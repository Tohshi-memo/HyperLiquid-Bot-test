# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T06:52:25.973600+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11527`

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

- `risk_on_high->unknown_4h` score `38.3776` n `117` status `ready` deltaP `17.8145` edge `3.1412` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `38.3776` n `117` status `ready` deltaP `17.8145` edge `3.1412` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.6739` n `159` status `ready` deltaP `14.1538` edge `2.198` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `20.804` n `129` status `ready` deltaP `1.6165` edge `1.7806` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `20.804` n `129` status `ready` deltaP `1.6165` edge `1.7806` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.8856` n `171` status `ready` deltaP `0.4333` edge `1.2173` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.8652` n `107` status `ready` deltaP `22.3131` edge `0.6712` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.8652` n `107` status `ready` deltaP `22.3131` edge `0.6712` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3717` n `107` status `ready` deltaP `21.6041` edge `0.8504` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3717` n `107` status `ready` deltaP `21.6041` edge `0.8504` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3427` n `59` status `ready` deltaP `21.5249` edge `0.4503` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `1.8654` n `59` status `ready` deltaP `8.2627` edge `0.3471` maxDD `-15.4056`
- `news_risk_high->crypto_major_24h` score `1.5929` n `59` status `ready` deltaP `14.6952` edge `0.4731` maxDD `-30.7329`
- `market_context_high->equity_24h` score `1.5078` n `147` status `ready` deltaP `18.2823` edge `0.5523` maxDD `-24.4698`
- `risk_on_high->crypto_major_24h` score `0.883` n `107` status `ready` deltaP `21.0313` edge `0.8474` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.883` n `107` status `ready` deltaP `21.0313` edge `0.8474` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.7205` n `147` status `ready` deltaP `24.0576` edge `0.8784` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.5184` n `147` status `ready` deltaP `15.6215` edge `0.7122` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.1699` n `67` status `ready` deltaP `4.5754` edge `0.0272` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0595` n `129` status `ready` deltaP `11.3204` edge `0.0034` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

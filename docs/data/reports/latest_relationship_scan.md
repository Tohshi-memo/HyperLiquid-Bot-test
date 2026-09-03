# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T11:07:26.984593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11584`

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

- `risk_on_high->unknown_4h` score `36.2474` n `133` status `ready` deltaP `13.2668` edge `2.994` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.2474` n `133` status `ready` deltaP `13.2668` edge `2.994` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.7358` n `164` status `ready` deltaP `12.0427` edge `2.3839` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7462` n `133` status `ready` deltaP `2.6889` edge `1.6853` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7462` n `133` status `ready` deltaP `2.6889` edge `1.6853` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.8439` n `175` status `ready` deltaP `1.8468` edge `1.2044` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.7699` n `107` status `ready` deltaP `19.3617` edge `0.5996` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.7699` n `107` status `ready` deltaP `19.3617` edge `0.5996` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.2339` n `135` status `ready` deltaP `20.2893` edge `0.5688` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.0858` n `60` status `ready` deltaP `20.0347` edge `0.4273` maxDD `-19.4761`
- `risk_on_high->crypto_alt_24h` score `1.8117` n `107` status `ready` deltaP `19.5207` edge `0.7925` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.8117` n `107` status `ready` deltaP `19.5207` edge `0.7925` maxDD `-42.8959`
- `news_risk_high->crypto_major_24h` score `1.6009` n `60` status `ready` deltaP `14.2708` edge `0.4766` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.9607` n `135` status `ready` deltaP `17.2569` edge `0.758` maxDD `-46.3234`
- `news_risk_high->equity_24h` score `0.8276` n `60` status `ready` deltaP `6.2153` edge `0.3114` maxDD `-15.4056`
- `market_context_high->crypto_major_24h` score `0.5591` n `135` status `ready` deltaP `23.1597` edge `0.8637` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.5531` n `107` status `ready` deltaP `19.816` edge `0.8132` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.5531` n `107` status `ready` deltaP `19.816` edge `0.8132` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2535` n `67` status `ready` deltaP `5.6425` edge `0.0308` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0875` n `133` status `ready` deltaP `11.814` edge `0.0037` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

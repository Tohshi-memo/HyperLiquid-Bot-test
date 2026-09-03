# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T09:07:34.286248+00:00`
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

- `risk_on_high->unknown_4h` score `36.73` n `126` status `ready` deltaP `14.3946` edge `3.0267` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.73` n `126` status `ready` deltaP `14.3946` edge `3.0267` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.1917` n `163` status `ready` deltaP `11.8968` edge `2.2562` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7343` n `133` status `ready` deltaP `2.3895` edge `1.6863` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7343` n `133` status `ready` deltaP `2.3895` edge `1.6863` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7924` n `175` status `ready` deltaP `2.1189` edge `1.1983` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.343` n `107` status `ready` deltaP `20.7506` edge `0.6381` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.343` n `107` status `ready` deltaP `20.7506` edge `0.6381` maxDD `-19.828`
- `market_context_high->equity_24h` score `2.8631` n `142` status `ready` deltaP `18.684` edge `0.5486` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `2.2061` n `107` status `ready` deltaP `20.9096` edge `0.8338` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.2061` n `107` status `ready` deltaP `20.9096` edge `0.8338` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.1771` n `59` status `ready` deltaP `20.8304` edge `0.4337` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.5778` n `59` status `ready` deltaP `14.5216` edge `0.473` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.3432` n `59` status `ready` deltaP `6.7002` edge `0.314` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.8732` n `107` status `ready` deltaP `20.8577` edge `0.8473` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.8732` n `107` status `ready` deltaP `20.8577` edge `0.8473` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.5911` n `142` status `ready` deltaP `15.5785` edge `0.7218` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.4639` n `142` status `ready` deltaP `22.5426` edge `0.8556` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2668` n `67` status `ready` deltaP `5.6425` edge `0.0325` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0408` n `133` status `ready` deltaP `11.0655` edge `0.0027` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

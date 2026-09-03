# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T11:22:25.245673+00:00`
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

- `risk_on_high->unknown_4h` score `36.2064` n `133` status `ready` deltaP `13.1143` edge `2.9916` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.2064` n `133` status `ready` deltaP `13.1143` edge `2.9916` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.8587` n `164` status `ready` deltaP `12.5` edge `2.3911` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.745` n `133` status `ready` deltaP `2.6889` edge `1.6852` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.745` n `133` status `ready` deltaP `2.6889` edge `1.6852` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.9824` n `174` status `ready` deltaP `1.6432` edge `1.2173` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.7008` n `107` status `ready` deltaP `19.1881` edge `0.595` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.7008` n `107` status `ready` deltaP `19.1881` edge `0.595` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.2995` n `134` status `ready` deltaP `20.569` edge `0.5724` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.3453` n `61` status `ready` deltaP `20.4349` edge `0.4579` maxDD `-19.4761`
- `risk_on_high->crypto_alt_24h` score `1.7692` n `107` status `ready` deltaP `19.3471` edge `0.7882` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.7692` n `107` status `ready` deltaP `19.3471` edge `0.7882` maxDD `-42.8959`
- `news_risk_high->crypto_major_24h` score `1.3666` n `61` status `ready` deltaP `15.0359` edge `0.5133` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.0621` n `61` status `ready` deltaP `6.916` edge `0.3368` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `0.9829` n `134` status `ready` deltaP `17.5477` edge `0.7589` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.5242` n `107` status `ready` deltaP `19.816` edge `0.8095` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.5242` n `107` status `ready` deltaP `19.816` edge `0.8095` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5203` n `134` status `ready` deltaP `22.8778` edge `0.8606` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2504` n `67` status `ready` deltaP `5.6425` edge `0.0304` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0875` n `133` status `ready` deltaP `11.814` edge `0.0037` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

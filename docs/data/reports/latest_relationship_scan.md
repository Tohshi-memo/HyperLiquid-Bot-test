# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T12:22:29.384895+00:00`
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

- `risk_on_high->unknown_4h` score `36.1604` n `133` status `ready` deltaP `12.8095` edge `2.9898` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.1604` n `133` status `ready` deltaP `12.8095` edge `2.9898` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.9931` n `164` status `ready` deltaP `13.4147` edge `2.3962` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.5891` n `133` status `ready` deltaP `2.3895` edge `1.6742` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.5891` n `133` status `ready` deltaP `2.3895` edge `1.6742` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.4931` n `170` status `ready` deltaP `1.6819` edge `1.2596` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.5758` n `130` status `ready` deltaP `21.7575` edge `0.5875` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `3.4737` n `107` status `ready` deltaP `18.4937` edge `0.5807` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.4737` n `107` status `ready` deltaP `18.4937` edge `0.5807` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `3.2313` n `65` status `ready` deltaP `21.859` edge `0.562` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `2.5026` n `65` status `ready` deltaP `17.8606` edge `0.6401` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.7243` n `65` status `ready` deltaP `9.4498` edge `0.4048` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.6083` n `107` status `ready` deltaP `18.6527` edge `0.7722` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.6083` n `107` status `ready` deltaP `18.6527` edge `0.7722` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.0775` n `130` status `ready` deltaP `18.7821` edge `0.7628` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.4205` n `107` status `ready` deltaP `19.816` edge `0.7962` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4205` n `107` status `ready` deltaP `19.816` edge `0.7962` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.3533` n `130` status `ready` deltaP `21.7067` edge `0.847` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2222` n `67` status `ready` deltaP `5.4901` edge `0.0278` maxDD `-0.8733`
- `news_risk_high->commodity_24h` score `0.0596` n `65` status `ready` deltaP `5.7184` edge `-0.0139` maxDD `-0.2074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

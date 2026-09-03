# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T08:52:30.483080+00:00`
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

- `risk_on_high->unknown_4h` score `35.8691` n `125` status `ready` deltaP `14.2232` edge `2.9561` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.8691` n `125` status `ready` deltaP `14.2232` edge `2.9561` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.5367` n `162` status `ready` deltaP `11.7491` edge `2.2026` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7355` n `133` status `ready` deltaP `2.3895` edge `1.6864` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7355` n `133` status `ready` deltaP `2.3895` edge `1.6864` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.9276` n `174` status `ready` deltaP `1.9185` edge `1.2109` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.4157` n `107` status `ready` deltaP `20.9242` edge `0.643` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.4157` n `107` status `ready` deltaP `20.9242` edge `0.643` maxDD `-19.828`
- `market_context_high->equity_24h` score `2.9358` n `142` status `ready` deltaP `18.8576` edge `0.5535` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `2.2494` n `107` status `ready` deltaP `21.0832` edge `0.8382` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.2494` n `107` status `ready` deltaP `21.0832` edge `0.8382` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2205` n `59` status `ready` deltaP `21.004` edge `0.4381` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.6265` n `59` status `ready` deltaP `14.6952` edge `0.4759` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.4159` n `59` status `ready` deltaP `6.8738` edge `0.3189` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.9049` n `107` status `ready` deltaP `21.0313` edge `0.8502` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9049` n `107` status `ready` deltaP `21.0313` edge `0.8502` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.6344` n `142` status `ready` deltaP `15.7521` edge `0.7262` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.4955` n `142` status `ready` deltaP `22.7162` edge `0.8585` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2644` n `67` status `ready` deltaP `5.6425` edge `0.0322` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0408` n `133` status `ready` deltaP `11.0655` edge `0.0027` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

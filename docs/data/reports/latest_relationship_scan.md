# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T07:52:25.713241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11563`

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

- `risk_on_high->unknown_4h` score `37.7415` n `121` status `ready` deltaP `16.3576` edge `3.0979` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `37.7415` n `121` status `ready` deltaP `16.3576` edge `3.0979` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.6674` n `162` status `ready` deltaP `13.1437` edge `2.2042` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.8938` n `133` status `ready` deltaP `2.6889` edge `1.6976` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.8938` n `133` status `ready` deltaP `2.6889` edge `1.6976` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.478` n `174` status `ready` deltaP `1.0685` edge `1.1791` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.6765` n `107` status `ready` deltaP `21.6187` edge `0.6601` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.6765` n `107` status `ready` deltaP `21.6187` edge `0.6601` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3569` n `107` status `ready` deltaP `21.6041` edge `0.8485` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3569` n `107` status `ready` deltaP `21.6041` edge `0.8485` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3279` n `59` status `ready` deltaP `21.5249` edge `0.4484` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `1.6766` n `59` status `ready` deltaP `7.5683` edge `0.336` maxDD `-15.4056`
- `news_risk_high->crypto_major_24h` score `1.6721` n `59` status `ready` deltaP `14.6952` edge `0.4797` maxDD `-30.7329`
- `market_context_high->equity_24h` score `1.478` n `146` status `ready` deltaP `17.97` edge `0.5445` maxDD `-23.9855`
- `risk_on_high->crypto_major_24h` score `0.9345` n `107` status `ready` deltaP `21.0313` edge `0.854` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9345` n `107` status `ready` deltaP `21.0313` edge `0.854` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.6913` n `146` status `ready` deltaP `23.7966` edge `0.8764` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.5005` n `146` status `ready` deltaP `15.3373` edge `0.7118` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2227` n `67` status `ready` deltaP `5.1852` edge `0.0299` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0712` n `133` status `ready` deltaP `11.5146` edge `0.0036` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

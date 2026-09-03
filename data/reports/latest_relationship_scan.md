# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T05:52:34.365694+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11719`

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

- `risk_on_high->unknown_4h` score `40.2812` n `113` status `ready` deltaP `18.6745` edge `3.2941` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `40.2812` n `113` status `ready` deltaP `18.6745` edge `3.2941` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.7514` n `155` status `ready` deltaP `14.6037` edge `2.2848` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.3444` n `125` status `ready` deltaP `1.1257` edge `1.5789` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.3444` n `125` status `ready` deltaP `1.1257` edge `1.5789` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.0773` n `167` status `ready` deltaP `0.0` edge `1.0695` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `5.0372` n `107` status `ready` deltaP `23.0075` edge `0.6809` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.0372` n `107` status `ready` deltaP `23.0075` edge `0.6809` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3631` n `107` status `ready` deltaP `21.6041` edge `0.8493` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3631` n `107` status `ready` deltaP `21.6041` edge `0.8493` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3341` n `59` status `ready` deltaP `21.5249` edge `0.4492` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.0373` n `59` status `ready` deltaP `8.9571` edge `0.3568` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.6196` n `147` status `ready` deltaP `18.9767` edge `0.562` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.4885` n `59` status `ready` deltaP `14.6952` edge `0.4644` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.8152` n `107` status `ready` deltaP `21.0313` edge `0.8387` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.8152` n `107` status `ready` deltaP `21.0313` edge `0.8387` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.6526` n `147` status `ready` deltaP `24.0576` edge `0.8697` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.5099` n `147` status `ready` deltaP `15.6215` edge `0.7111` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.1203` n `67` status `ready` deltaP `3.9657` edge `0.0249` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0545` n `125` status `ready` deltaP `11.2539` edge `0.0032` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

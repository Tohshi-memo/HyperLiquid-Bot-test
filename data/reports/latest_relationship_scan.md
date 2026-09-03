# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T14:07:27.370938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11565`

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

- `risk_on_high->unknown_4h` score `35.8026` n `133` status `ready` deltaP `12.657` edge `2.961` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.8026` n `133` status `ready` deltaP `12.657` edge `2.961` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.0376` n `167` status `ready` deltaP `14.2553` edge `2.3943` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.6712` n `133` status `ready` deltaP `1.7907` edge `1.6017` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.6712` n `133` status `ready` deltaP `1.7907` edge `1.6017` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.1913` n `167` status `ready` deltaP `2.2455` edge `1.2307` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.557` n `127` status `ready` deltaP `22.0322` edge `0.5841` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.1741` n `66` status `ready` deltaP `21.1332` edge `0.5595` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `3.0741` n `107` status `ready` deltaP `17.2784` edge `0.5555` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.0741` n `107` status `ready` deltaP `17.2784` edge `0.5555` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.5861` n `66` status `ready` deltaP `17.4716` edge `0.6534` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6328` n `66` status `ready` deltaP `8.9805` edge `0.3962` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.2791` n `107` status `ready` deltaP `17.4374` edge `0.7381` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.2791` n `107` status `ready` deltaP `17.4374` edge `0.7381` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.0` n `127` status `ready` deltaP `19.0931` edge `0.7508` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2317` n `67` status `ready` deltaP `5.6425` edge `0.028` maxDD `-0.8733`
- `market_context_high->crypto_major_24h` score `0.1749` n `127` status `ready` deltaP `22.1005` edge `0.8215` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.1284` n `107` status `ready` deltaP `18.7743` edge `0.7657` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1284` n `107` status `ready` deltaP `18.7743` edge `0.7657` maxDD `-56.9519`
- `risk_on_high->metal_1h` score `0.0338` n `133` status `ready` deltaP `11.0655` edge `0.0018` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

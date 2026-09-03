# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T14:22:33.669503+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11619`

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

- `risk_on_high->unknown_4h` score `35.571` n `133` status `ready` deltaP `12.657` edge `2.9417` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.571` n `133` status `ready` deltaP `12.657` edge `2.9417` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.806` n `167` status `ready` deltaP `14.2553` edge `2.375` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.6172` n `133` status `ready` deltaP `1.641` edge `1.5982` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.6172` n `133` status `ready` deltaP `1.641` edge `1.5982` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.1374` n `167` status `ready` deltaP `2.0958` edge `1.2272` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.5035` n `127` status `ready` deltaP `21.8586` edge `0.5808` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.1105` n `66` status `ready` deltaP `20.9596` edge `0.5525` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `3.0206` n `107` status `ready` deltaP `17.1048` edge `0.5522` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.0206` n `107` status `ready` deltaP `17.1048` edge `0.5522` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.5279` n `66` status `ready` deltaP `17.298` edge `0.6471` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.598` n `66` status `ready` deltaP `8.8069` edge `0.3929` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.2154` n `107` status `ready` deltaP `17.2638` edge `0.7311` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.2154` n `107` status `ready` deltaP `17.2638` edge `0.7311` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.9364` n `127` status `ready` deltaP `18.9195` edge `0.7438` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2427` n `67` status `ready` deltaP `5.795` edge `0.0284` maxDD `-0.8733`
- `market_context_high->crypto_major_24h` score `0.1167` n `127` status `ready` deltaP `21.9269` edge `0.8152` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.0702` n `107` status `ready` deltaP `18.6007` edge `0.7594` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.0702` n `107` status `ready` deltaP `18.6007` edge `0.7594` maxDD `-56.9519`
- `risk_on_high->metal_1h` score `0.0431` n `133` status `ready` deltaP `11.2152` edge `0.002` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

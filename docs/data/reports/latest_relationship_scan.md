# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T00:52:27.527706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1642.0406` n `134` status `ready` deltaP `-2.7908` edge `136.8983` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `41.7774` n `134` status `ready` deltaP `5.7517` edge `3.4564` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.6471` n `134` status `ready` deltaP `30.7499` edge `0.0339` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.28` n `134` status `ready` deltaP `9.5563` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1461` n `134` status `ready` deltaP `12.4135` edge `0.0513` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0523` n `134` status `ready` deltaP `12.6297` edge `0.0121` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `0.0433` n `134` status `ready` deltaP `6.8661` edge `0.0606` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.1243` n `134` status `ready` deltaP `2.9851` edge `0.0573` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1532` n `134` status `ready` deltaP `2.6812` edge `-0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3427` n `134` status `ready` deltaP `1.3451` edge `0.0139` maxDD `-0.4475`
- `market_context_high->equity_24h` score `-0.5868` n `134` status `ready` deltaP `13.1867` edge `0.1389` maxDD `-14.0571`
- `market_context_high->fx_4h` score `-0.6073` n `134` status `ready` deltaP `-1.9976` edge `-0.0047` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7355` n `134` status `ready` deltaP `3.747` edge `0.0672` maxDD `-8.251`
- `market_context_high->equity_4h` score `-0.7627` n `134` status `ready` deltaP `-0.3527` edge `0.063` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.8965` n `134` status `ready` deltaP `-2.6946` edge `-0.0009` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.351` n `134` status `ready` deltaP `1.889` edge `0.0079` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5578` n `134` status `ready` deltaP `3.9257` edge `0.0388` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.7744` n `134` status `ready` deltaP `7.2466` edge `0.0537` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2175` n `134` status `ready` deltaP `-5.2148` edge `-0.018` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.0835` n `134` status `ready` deltaP `4.7238` edge `0.004` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

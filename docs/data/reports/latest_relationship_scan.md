# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T16:37:28.919569+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `32.175` n `133` status `ready` deltaP `12.657` edge `2.6587` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `32.175` n `133` status `ready` deltaP `12.657` edge `2.6587` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `25.41` n `167` status `ready` deltaP `14.2553` edge `2.092` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `17.3549` n `133` status `ready` deltaP `1.0422` edge `1.497` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `17.3549` n `133` status `ready` deltaP `1.0422` edge `1.497` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.8751` n `167` status `ready` deltaP `1.497` edge `1.126` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.8649` n `127` status `ready` deltaP `20.2961` edge `0.538` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.7131` n `67` status `ready` deltaP `19.872` edge `0.5088` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.382` n `107` status `ready` deltaP `15.5423` edge `0.5094` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.382` n `107` status `ready` deltaP `15.5423` edge `0.5094` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.177` n `67` status `ready` deltaP `16.3687` edge `0.6083` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.3469` n `67` status `ready` deltaP `7.968` edge `0.3663` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `0.4603` n `107` status `ready` deltaP `15.7013` edge `0.6447` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.4603` n `107` status `ready` deltaP `15.7013` edge `0.6447` maxDD `-42.8959`
- `news_risk_high->commodity_4h` score `0.3654` n `67` status `ready` deltaP `7.0145` edge `0.036` maxDD `-0.8733`
- `market_context_high->crypto_alt_24h` score `0.1813` n `127` status `ready` deltaP `17.357` edge `0.6574` maxDD `-46.3234`
- `news_risk_high->fx_4h` score `0.0921` n `67` status `ready` deltaP `10.2612` edge `0.0049` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0509` n `133` status `ready` deltaP `11.5146` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0509` n `133` status `ready` deltaP `11.5146` edge `0.001` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0485` n `67` status `ready` deltaP `4.7748` edge `-0.0027` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

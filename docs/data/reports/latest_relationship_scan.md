# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T12:22:25.856232+00:00`
- Price records: `672`
- Market context records: `3279`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10506`

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

- `risk_on_high->crypto_major_4h` score `16.0549` n `32` status `ready` deltaP `30.3354` edge `1.2479` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0549` n `32` status `ready` deltaP `30.3354` edge `1.2479` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9419` n `109` status `ready` deltaP `17.7705` edge `2.6531` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `11.9041` n `109` status `ready` deltaP `42.7099` edge `0.7501` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2743` n `109` status `ready` deltaP `29.9408` edge `0.8287` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.3649` n `32` status `ready` deltaP `10.8994` edge `0.7255` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3649` n `32` status `ready` deltaP `10.8994` edge `0.7255` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.758` n `109` status `ready` deltaP `19.8506` edge `1.5757` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.774` n `32` status `ready` deltaP `15.0152` edge `0.4972` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.774` n `32` status `ready` deltaP `15.0152` edge `0.4972` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.464` n `165` status `ready` deltaP `20.753` edge `0.1628` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.139` n `32` status `ready` deltaP `7.4663` edge `0.3314` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.139` n `32` status `ready` deltaP `7.4663` edge `0.3314` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.3014` n `109` status `ready` deltaP `19.2103` edge `2.1087` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.1755` n `32` status `ready` deltaP `1.4482` edge `0.1998` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1755` n `32` status `ready` deltaP `1.4482` edge `0.1998` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2611` n `32` status `ready` deltaP `6.1003` edge `0.0613` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2611` n `32` status `ready` deltaP `6.1003` edge `0.0613` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2095` n `32` status `ready` deltaP `0.5988` edge `0.1666` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2095` n `32` status `ready` deltaP `0.5988` edge `0.1666` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

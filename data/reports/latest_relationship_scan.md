# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T04:07:28.084224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11337`

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

- `market_context_high->unknown_24h` score `771.5739` n `139` status `ready` deltaP `14.0126` edge `64.2096` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.4637` n `82` status `ready` deltaP `-3.4541` edge `32.0205` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.4821` n `87` status `ready` deltaP `42.864` edge `1.7774` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.4821` n `87` status `ready` deltaP `42.864` edge `1.7774` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.7448` n `57` status `ready` deltaP `54.2672` edge `1.707` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.4204` n `139` status `ready` deltaP `37.1003` edge `1.5371` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.1231` n `57` status `ready` deltaP `29.3129` edge `1.2803` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0215` n `57` status `ready` deltaP `33.4704` edge `0.7885` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.1071` n `87` status `ready` deltaP `36.9792` edge `0.5124` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1071` n `87` status `ready` deltaP `36.9792` edge `0.5124` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7927` n `139` status `ready` deltaP `36.9792` edge `0.4862` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6548` n `87` status `ready` deltaP `43.7255` edge `0.4669` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6548` n `87` status `ready` deltaP `43.7255` edge `0.4669` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1957` n `57` status `ready` deltaP `51.0417` edge `0.3427` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9502` n `57` status `ready` deltaP `51.3523` edge `0.3295` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `7.194` n `87` status `ready` deltaP `23.3537` edge `1.1734` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.194` n `87` status `ready` deltaP `23.3537` edge `1.1734` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.652` n `87` status `ready` deltaP `31.1396` edge `0.4326` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.652` n `87` status `ready` deltaP `31.1396` edge `0.4326` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2335` n `87` status `ready` deltaP `51.4128` edge `0.0976` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

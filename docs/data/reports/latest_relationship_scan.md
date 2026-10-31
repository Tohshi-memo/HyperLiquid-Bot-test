# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T09:37:26.726715+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1857.6101` n `125` status `ready` deltaP `-5.7875` edge `154.8824` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `98.0395` n `98` status `ready` deltaP `-5.9422` edge `8.2382` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `32.4117` n `125` status `ready` deltaP `1.8695` edge `2.7018` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.662` n `32` status `ready` deltaP `49.1319` edge `1.2324` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.3793` n `125` status `ready` deltaP `23.4639` edge `0.9009` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.2084` n `98` status `ready` deltaP `18.7905` edge `0.4474` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.395` n `125` status `ready` deltaP `41.0944` edge `0.1106` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9252` n `125` status `ready` deltaP `13.5461` edge `0.0158` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.902` n `98` status `ready` deltaP `8.096` edge `0.1041` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.4607` n `125` status `ready` deltaP `17.0878` edge `0.0327` maxDD `-1.671`
- `market_context_high->equity_1h` score `0.4576` n `125` status `ready` deltaP `6.1497` edge `0.0847` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.4489` n `125` status `ready` deltaP `9.7006` edge `0.0755` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.2063` n `125` status `ready` deltaP `12.8207` edge `0.0536` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.0183` n `125` status `ready` deltaP `2.0378` edge `0.1425` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0608` n `125` status `ready` deltaP `4.3533` edge `-0.001` maxDD `-0.1986`
- `market_context_high->metal_24h` score `-0.2823` n `125` status `ready` deltaP `7.0958` edge `0.1812` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.3008` n `125` status `ready` deltaP `1.6443` edge `0.0154` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4724` n `125` status `ready` deltaP `0.2854` edge `-0.0028` maxDD `-0.44`
- `market_context_high->index_1h` score `-0.4851` n `125` status `ready` deltaP `2.103` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7785` n `125` status `ready` deltaP `3.394` edge `0.0551` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

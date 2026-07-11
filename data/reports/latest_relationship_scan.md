# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T19:52:29.563086+00:00`
- Price records: `672`
- Market context records: `6423`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.3607` n `32` status `ready` deltaP `31.7708` edge `0.833` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.851` n `146` status `ready` deltaP `17.7511` edge `0.7826` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.6159` n `32` status `ready` deltaP `55.7292` edge `0.1798` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1997` n `32` status `ready` deltaP `43.8262` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1276` n `32` status `ready` deltaP `35.4167` edge `0.1284` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.6017` n `32` status `ready` deltaP `13.3681` edge `0.4506` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.5081` n `32` status `ready` deltaP `30.2395` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5037` n `32` status `ready` deltaP `14.2777` edge `0.1443` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.87` n `32` status `ready` deltaP `10.2732` edge `0.0892` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6278` n `202` status `ready` deltaP `-7.196` edge `0.2011` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3346` n `196` status `ready` deltaP `10.5152` edge `0.0416` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2482` n `196` status `ready` deltaP `9.7375` edge `0.0234` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1866` n `32` status `ready` deltaP `7.1295` edge `-0.0286` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2836` n `146` status `ready` deltaP `18.5978` edge `0.0965` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5277` n `202` status `ready` deltaP `1.1857` edge `0.0022` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.577` n `196` status `ready` deltaP `7.2611` edge `0.0475` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.597` n `32` status `ready` deltaP `-0.2994` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6607` n `202` status `ready` deltaP `-2.0839` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6827` n `202` status `ready` deltaP `-2.7865` edge `0.003` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7495` n `32` status `ready` deltaP `0.5208` edge `-0.0124` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

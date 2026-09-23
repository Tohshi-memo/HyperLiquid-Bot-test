# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T20:52:30.336260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9547`

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

- `market_context_high->unknown_1h` score `72.2119` n `47` status `ready` deltaP `9.8166` edge `5.9593` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.6126` n `46` status `ready` deltaP `19.9578` edge `2.6836` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.3036` n `46` status `ready` deltaP `17.3536` edge `1.503` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.756` n `46` status `ready` deltaP `14.9306` edge `1.2968` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.919` n `96` status `ready` deltaP `-2.7777` edge `1.4476` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.5144` n `46` status `ready` deltaP `26.3814` edge `0.3757` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.467` n `103` status `ready` deltaP `17.128` edge `0.3158` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.3924` n `103` status `ready` deltaP `12.8597` edge `0.3801` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.8651` n `96` status `ready` deltaP `-4.8611` edge `0.8426` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7358` n `96` status `ready` deltaP `26.2153` edge `0.1711` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.5006` n `103` status `ready` deltaP `13.3074` edge `0.1687` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3872` n `47` status `ready` deltaP `28.3861` edge `0.0251` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0253` n `103` status `ready` deltaP `15.7026` edge `0.1076` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4296` n `103` status `ready` deltaP `21.3948` edge `0.0401` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.2076` n `46` status `ready` deltaP `20.3578` edge `-0.0117` maxDD `-0.2042`
- `news_risk_high->fx_24h` score `1.2022` n `96` status `ready` deltaP `28.6458` edge `0.1221` maxDD `-1.7159`
- `market_context_high->equity_4h` score `1.089` n `47` status `ready` deltaP `9.2177` edge `0.0711` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6959` n `47` status `ready` deltaP `11.7658` edge `0.0074` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6159` n `96` status `ready` deltaP `17.1875` edge `0.0488` maxDD `-2.4203`
- `news_risk_high->metal_1h` score `0.6062` n `103` status `ready` deltaP `15.0529` edge `0.0095` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

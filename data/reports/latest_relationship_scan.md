# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T17:52:29.639806+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9882`

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

- `market_context_high->unknown_1h` score `82.3723` n `47` status `ready` deltaP `9.8166` edge `6.806` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.0995` n `46` status `ready` deltaP `17.8744` edge `2.5714` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.1445` n `46` status `ready` deltaP `15.2703` edge `1.4203` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.679` n `46` status `ready` deltaP `12.8472` edge `1.1376` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.4059` n `96` status `ready` deltaP `-4.8611` edge `1.3354` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.1437` n `46` status `ready` deltaP `24.298` edge `0.3587` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.2754` n `103` status `ready` deltaP `16.5182` edge `0.3039` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.7893` n `103` status `ready` deltaP `11.3353` edge `0.34` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0638` n `96` status `ready` deltaP `28.125` edge `0.1857` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.3075` n `103` status `ready` deltaP `12.2595` edge `0.1596` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2585` n `47` status `ready` deltaP `27.1666` edge `0.0225` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0025` n `103` status `ready` deltaP `15.7026` edge `0.1057` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.788` n `96` status `ready` deltaP `-6.9445` edge `0.6834` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.3237` n `103` status `ready` deltaP `20.1753` edge `0.0394` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1802` n `96` status `ready` deltaP `28.2986` edge `0.1216` maxDD `-1.7159`
- `market_context_high->equity_4h` score `0.797` n `47` status `ready` deltaP `7.9981` edge `0.0549` maxDD `-1.3444`
- `market_context_high->metal_24h` score `0.6989` n `46` status `ready` deltaP `18.2745` edge `-0.0402` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.6948` n `47` status `ready` deltaP `11.6161` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6278` n `103` status `ready` deltaP `15.0529` edge `0.0113` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.4165` n `47` status `ready` deltaP `7.2748` edge `0.0265` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

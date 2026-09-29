# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T19:37:43.009019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2591.2855` n `139` status `ready` deltaP `1.3889` edge `215.9312` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4203` n `139` status `ready` deltaP `30.3308` edge `1.478` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.4032` n `139` status `ready` deltaP `31.8382` edge `0.826` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.3723` n `139` status `ready` deltaP `24.7202` edge `0.893` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0331` n `139` status `ready` deltaP `37.8173` edge `0.1535` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.5232` n `139` status `ready` deltaP `30.718` edge `0.2743` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.0547` n `142` status `ready` deltaP `30.2667` edge `0.2129` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.0494` n `142` status `ready` deltaP `11.3771` edge `0.3609` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0055` n `142` status `ready` deltaP `8.0185` edge `0.1214` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7054` n `142` status `ready` deltaP `8.1513` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.509` n `142` status `ready` deltaP `9.0495` edge `0.0111` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.24` n `142` status `ready` deltaP `10.9692` edge `0.0322` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2761` n `142` status `ready` deltaP `3.0383` edge `0.0726` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4882` n `142` status `ready` deltaP `1.3135` edge `0.0135` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2169` n `142` status `ready` deltaP `-6.4776` edge `0.0366` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2827` n `142` status `ready` deltaP `9.4362` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.304` n `142` status `ready` deltaP `-2.5486` edge `0.1213` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8073` n `142` status `ready` deltaP `-8.845` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8643` n `142` status `ready` deltaP `-9.3046` edge `-0.0095` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3255` n `142` status `ready` deltaP `-9.6122` edge `0.0078` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

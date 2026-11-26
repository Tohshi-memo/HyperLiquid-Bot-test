# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T12:22:35.828229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3467`

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

- `news_risk_high->unknown_1h` score `3231.036` n `31` status `ready` deltaP `1.7819` edge `269.2587` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3220.0267` n `31` status `ready` deltaP `3.4815` edge `268.318` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `100.7442` n `31` status `ready` deltaP `1.7819` edge `8.3929` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `35.6686` n `31` status `ready` deltaP `44.0972` edge `2.6784` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.4407` n `31` status `ready` deltaP `43.2292` edge `2.6652` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.8326` n `31` status `ready` deltaP `43.4028` edge `2.1967` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8267` n `31` status `ready` deltaP `27.2177` edge `0.8078` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6564` n `31` status `ready` deltaP `39.3588` edge `0.6737` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.5708` n `31` status `ready` deltaP `29.7771` edge `0.5432` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9906` n `31` status `ready` deltaP `19.6744` edge `0.9068` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9178` n `31` status `ready` deltaP `44.6181` edge `0.1957` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0019` n `31` status `ready` deltaP `42.2323` edge `0.1481` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8022` n `31` status `ready` deltaP `20.7359` edge `0.1973` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5188` n `31` status `ready` deltaP `37.9869` edge `0.066` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7621` n `31` status `ready` deltaP `32.5913` edge `0.0214` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5109` n `31` status `ready` deltaP `10.1603` edge `0.3003` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.265` n `31` status `ready` deltaP `13.0046` edge `0.2394` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9728` n `31` status `ready` deltaP `25.2853` edge `0.0243` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4861` n `31` status `ready` deltaP `29.1336` edge `0.0242` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0172` n `31` status `ready` deltaP `15.711` edge `0.0814` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

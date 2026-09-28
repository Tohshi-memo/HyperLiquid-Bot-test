# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T14:52:31.737668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7782`

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

- `news_risk_high->unknown_24h` score `1987.5648` n `139` status `ready` deltaP `1.2153` edge `165.6223` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.1941` n `139` status `ready` deltaP `21.8238` edge `0.8492` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.5278` n `139` status `ready` deltaP `17.9493` edge `0.7011` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.166` n `139` status `ready` deltaP `21.4216` edge `0.46` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.8132` n `139` status `ready` deltaP `27.0534` edge `0.1236` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.001` n `139` status `ready` deltaP `23.6675` edge `0.1699` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.6597` n `139` status `ready` deltaP `20.4749` edge `0.1873` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.6662` n `139` status `ready` deltaP `7.1673` edge `0.0988` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.456` n `139` status `ready` deltaP `6.6689` edge `0.2595` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.4481` n `139` status `ready` deltaP `6.8055` edge `0.0581` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4036` n `139` status `ready` deltaP `8.1528` edge `0.0083` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.3363` n `139` status `ready` deltaP `4.9812` edge `0.0241` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5292` n `139` status `ready` deltaP `1.3408` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6261` n `139` status `ready` deltaP `0.1475` edge `0.047` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1555` n `139` status `ready` deltaP `-8.6687` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1613` n `139` status `ready` deltaP `11.0491` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5582` n `139` status `ready` deltaP `-10.9854` edge `0.0229` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0303` n `139` status `ready` deltaP `-11.7165` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1168` n `139` status `ready` deltaP `-6.6152` edge `0.0442` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0197` n `139` status `ready` deltaP `-12.5417` edge `-0.0095` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

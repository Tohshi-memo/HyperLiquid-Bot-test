# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T09:37:31.589337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7522`

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

- `news_risk_high->unknown_24h` score `2607.0288` n `139` status `ready` deltaP `1.2153` edge `217.2443` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.507` n `139` status `ready` deltaP `32.9349` edge `1.5512` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.3029` n `139` status `ready` deltaP `34.4424` edge `0.8846` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.0998` n `139` status `ready` deltaP `27.3243` edge `1.0196` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2501` n `139` status `ready` deltaP `38.6853` edge `0.1658` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9336` n `139` status `ready` deltaP `31.9332` edge `0.3004` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6808` n `142` status `ready` deltaP `27.9801` edge `0.1978` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1869` n `142` status `ready` deltaP `8.7857` edge `0.3063` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7897` n `142` status `ready` deltaP `6.9706` edge `0.1104` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7081` n `142` status `ready` deltaP `8.7501` edge `0.0668` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4898` n `142` status `ready` deltaP `8.8998` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0163` n `142` status `ready` deltaP `8.6826` edge `0.0288` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4195` n `142` status `ready` deltaP `1.5413` edge `0.0642` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5038` n `142` status `ready` deltaP `1.3135` edge `0.0122` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.3309` n `142` status `ready` deltaP `-7.5446` edge `0.0291` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.3546` n `142` status `ready` deltaP `8.2167` edge `-0.0071` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.711` n `142` status `ready` deltaP `-4.2254` edge `0.0803` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8948` n `142` status `ready` deltaP `-9.8929` edge `-0.0039` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.073` n `142` status `ready` deltaP `-12.2986` edge `-0.0163` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.7176` n `142` status `ready` deltaP `-12.9659` edge `-0.0201` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

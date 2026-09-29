# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T08:43:53.250512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7346`

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

- `news_risk_high->unknown_24h` score `2611.098` n `139` status `ready` deltaP `1.2153` edge `217.5834` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3546` n `139` status `ready` deltaP `32.9349` edge `1.5385` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.1442` n `139` status `ready` deltaP `33.748` edge `0.876` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.1413` n `139` status `ready` deltaP `27.498` edge `1.0219` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1965` n `139` status `ready` deltaP `38.1645` edge `0.1648` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.895` n `139` status `ready` deltaP `31.586` edge `0.2995` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4739` n `139` status `ready` deltaP `27.4785` edge `0.1839` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.8401` n `142` status `ready` deltaP `7.27` edge `0.1126` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.8119` n `139` status `ready` deltaP `8.1933` edge `0.279` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.6529` n `142` status `ready` deltaP `8.4507` edge `0.0642` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4598` n `142` status `ready` deltaP `8.6004` edge `0.01` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0867` n `139` status `ready` deltaP `7.7251` edge `0.0266` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4258` n `142` status `ready` deltaP `1.5413` edge `0.0634` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4942` n `142` status `ready` deltaP `1.4632` edge `0.012` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3319` n `139` status `ready` deltaP `8.61` edge `-0.0068` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4325` n `139` status `ready` deltaP `-9.0037` edge `0.0258` maxDD `-3.6214`
- `news_risk_high->fx_1h` score `-1.9067` n `142` status `ready` deltaP `-10.0426` edge `-0.0039` maxDD `-1.0436`
- `news_risk_high->crypto_major_4h` score `-1.9254` n `139` status `ready` deltaP `-5.2433` edge `0.0596` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0684` n `142` status `ready` deltaP `-12.2986` edge `-0.0157` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0289` n `139` status `ready` deltaP `-12.2368` edge `-0.0123` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

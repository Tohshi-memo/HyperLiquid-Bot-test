# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T22:22:25.202180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2667.9828` n `139` status `ready` deltaP `1.2153` edge `222.3238` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.9672` n `139` status `ready` deltaP `27.0321` edge `1.1289` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.1003` n `139` status `ready` deltaP `26.6299` edge `0.6698` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.5569` n `139` status `ready` deltaP `22.4632` edge `0.8401` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.4902` n `139` status `ready` deltaP `32.2617` edge `0.1453` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.7514` n `139` status `ready` deltaP `24.6416` edge `0.2505` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5887` n `139` status `ready` deltaP `27.1736` edge `0.1955` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0311` n `139` status `ready` deltaP `8.8031` edge `0.2932` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7358` n `139` status `ready` deltaP `7.317` edge `0.1036` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5715` n `139` status `ready` deltaP `7.8534` edge `0.0614` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4707` n `139` status `ready` deltaP `8.9013` edge `0.0089` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0747` n `139` status `ready` deltaP `7.7251` edge `0.0276` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4681` n `139` status `ready` deltaP `1.9396` edge `0.011` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.4975` n `139` status `ready` deltaP `1.0457` edge `0.0575` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2045` n `139` status `ready` deltaP `-9.5669` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3124` n `139` status `ready` deltaP `8.61` edge `-0.0043` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3909` n `139` status `ready` deltaP `-8.6988` edge `0.0291` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8154` n `139` status `ready` deltaP `-5.2433` edge `0.0737` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0754` n `139` status `ready` deltaP `-12.6147` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8042` n `139` status `ready` deltaP `-11.0173` edge `-0.0017` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T21:22:33.161250+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7310`

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

- `news_risk_high->unknown_24h` score `2670.1788` n `139` status `ready` deltaP `1.2153` edge `222.5068` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.38` n `139` status `ready` deltaP `26.3377` edge `1.0846` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.7064` n `139` status `ready` deltaP `25.9355` edge `0.6416` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.3371` n `139` status `ready` deltaP `22.116` edge `0.8241` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.4011` n `139` status `ready` deltaP `31.5673` edge `0.1425` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.5843` n `139` status `ready` deltaP `23.9471` edge `0.2412` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4991` n `139` status `ready` deltaP `26.5639` edge `0.1921` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.8563` n `139` status `ready` deltaP `8.1933` edge `0.2827` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6351` n `139` status `ready` deltaP `6.8679` edge `0.0982` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5392` n `139` status `ready` deltaP `7.554` edge `0.0607` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4695` n `139` status `ready` deltaP `8.9013` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1295` n `139` status `ready` deltaP `7.1153` edge `0.0271` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4836` n `139` status `ready` deltaP `1.7899` edge `0.0107` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.549` n `139` status `ready` deltaP `0.5966` edge `0.0539` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1967` n `139` status `ready` deltaP `-9.4172` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2895` n `139` status `ready` deltaP `8.9149` edge `-0.0034` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4154` n `139` status `ready` deltaP `-9.0037` edge `0.028` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8279` n `139` status `ready` deltaP `-5.2433` edge `0.0721` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0746` n `139` status `ready` deltaP `-12.6147` edge `-0.0144` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7958` n `139` status `ready` deltaP `-11.0173` edge `-0.001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

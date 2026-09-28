# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T22:07:28.316477+00:00`
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

- `news_risk_high->unknown_24h` score `2668.6092` n `139` status `ready` deltaP `1.2153` edge `222.376` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.8201` n `139` status `ready` deltaP `26.8585` edge `1.1178` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.0048` n `139` status `ready` deltaP `26.4563` edge `0.663` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.5125` n `139` status `ready` deltaP `22.4632` edge `0.8364` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.4703` n `139` status `ready` deltaP `32.0881` edge `0.1448` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.7124` n `139` status `ready` deltaP `24.468` edge `0.2484` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5669` n `139` status `ready` deltaP `27.0212` edge `0.1947` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9853` n `139` status `ready` deltaP `8.6506` edge `0.2904` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7058` n `139` status `ready` deltaP `7.1673` edge `0.1021` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5559` n `139` status `ready` deltaP `7.7037` edge `0.0611` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4707` n `139` status `ready` deltaP `8.9013` edge `0.0089` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0881` n `139` status `ready` deltaP `7.5726` edge `0.0275` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4681` n `139` status `ready` deltaP `1.9396` edge `0.011` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5022` n `139` status `ready` deltaP `1.0457` edge `0.0569` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2123` n `139` status `ready` deltaP `-9.7166` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3029` n `139` status `ready` deltaP `8.7625` edge `-0.0041` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3917` n `139` status `ready` deltaP `-8.6988` edge `0.029` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8177` n `139` status `ready` deltaP `-5.2433` edge `0.0734` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0754` n `139` status `ready` deltaP `-12.6147` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.803` n `139` status `ready` deltaP `-11.0173` edge `-0.0016` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

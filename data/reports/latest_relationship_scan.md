# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T13:07:35.856946+00:00`
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

- `news_risk_high->unknown_24h` score `2590.1652` n `139` status `ready` deltaP `1.2153` edge `215.839` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9786` n `139` status `ready` deltaP `32.9349` edge `1.5905` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.6223` n `139` status `ready` deltaP `36.0049` edge `0.9008` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.8455` n `139` status `ready` deltaP `26.4563` edge `1.0042` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3443` n `139` status `ready` deltaP `39.727` edge `0.1667` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9156` n `139` status `ready` deltaP `31.9332` edge `0.2989` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7408` n `142` status `ready` deltaP `27.9801` edge `0.2028` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0259` n `142` status `ready` deltaP `8.6332` edge `0.2939` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7669` n `142` status `ready` deltaP `6.9706` edge `0.1085` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.641` n `142` status `ready` deltaP `7.8519` edge `0.0672` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4658` n `142` status `ready` deltaP `8.6004` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0235` n `142` status `ready` deltaP `8.6826` edge `0.0294` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4203` n `142` status `ready` deltaP `1.8407` edge `0.0621` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5085` n `142` status `ready` deltaP `1.1638` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.327` n `142` status `ready` deltaP `8.674` edge `-0.0066` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3594` n `142` status `ready` deltaP `-8.0019` edge `0.0285` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.77` n `142` status `ready` deltaP `-4.8352` edge `0.0768` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.7942` n `142` status `ready` deltaP `-8.6953` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9624` n `142` status `ready` deltaP `-10.6519` edge `-0.0131` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.4607` n `142` status `ready` deltaP `-10.8317` edge `-0.0014` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

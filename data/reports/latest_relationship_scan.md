# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T12:22:30.333230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `1135.2756` n `139` status `ready` deltaP `1.2153` edge `94.5982` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.363` n `139` status `ready` deltaP `20.4349` edge `0.7892` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.6797` n `139` status `ready` deltaP `16.2132` edge `0.642` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.1992` n `139` status `ready` deltaP `19.6855` edge `0.391` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.5687` n `139` status `ready` deltaP `25.3173` edge `0.1148` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.7948` n `139` status `ready` deltaP `22.9053` edge `0.1578` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.4586` n `139` status `ready` deltaP `20.3013` edge `0.1717` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7909` n `139` status `ready` deltaP `7.736` edge `0.2803` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6171` n `139` status `ready` deltaP `7.0176` edge `0.0957` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.2874` n `139` status `ready` deltaP `6.9552` edge `0.0066` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2539` n `139` status `ready` deltaP `5.7576` edge `0.0489` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4088` n `139` status `ready` deltaP `4.5239` edge `0.0211` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.528` n `139` status `ready` deltaP `1.3408` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6986` n `139` status `ready` deltaP `-0.3016` edge `0.0407` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1235` n `139` status `ready` deltaP `-8.0699` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1447` n `139` status `ready` deltaP `11.354` edge `-0.0011` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5243` n `139` status `ready` deltaP `-10.5281` edge `0.0242` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0381` n `139` status `ready` deltaP `-11.8662` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.0943` n `139` status `ready` deltaP `-6.7677` edge `0.0481` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0659` n `139` status `ready` deltaP `-12.999` edge `-0.0103` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

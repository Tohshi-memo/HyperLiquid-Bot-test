# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T00:22:30.023531+00:00`
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

- `news_risk_high->unknown_24h` score `2653.9548` n `139` status `ready` deltaP `1.2153` edge `221.1548` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.1379` n `139` status `ready` deltaP `28.421` edge `1.2172` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.8234` n `139` status `ready` deltaP `28.0188` edge `0.7208` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.0261` n `139` status `ready` deltaP `23.6785` edge `0.8711` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.6553` n `139` status `ready` deltaP `33.6506` edge `0.1498` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.0534` n `139` status `ready` deltaP `26.0305` edge `0.2664` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6117` n `139` status `ready` deltaP `27.3261` edge `0.1964` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9901` n `139` status `ready` deltaP `8.6506` edge `0.2908` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6614` n `139` status `ready` deltaP `7.1673` edge `0.0984` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5859` n `139` status `ready` deltaP `7.8534` edge `0.0626` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4851` n `139` status `ready` deltaP `9.051` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1015` n `139` status `ready` deltaP `7.4202` edge `0.0274` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.48` n `139` status `ready` deltaP `1.7899` edge `0.011` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5841` n `139` status `ready` deltaP `0.4469` edge `0.0504` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2341` n `139` status `ready` deltaP `-10.016` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3486` n `139` status `ready` deltaP `8.1527` edge `-0.0059` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4067` n `139` status `ready` deltaP `-8.8513` edge `0.0281` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9016` n `139` status `ready` deltaP `-5.7006` edge `0.0657` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0108` n `139` status `ready` deltaP `-11.5668` edge `-0.0132` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7812` n `139` status `ready` deltaP `-10.8649` edge `-0.0008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

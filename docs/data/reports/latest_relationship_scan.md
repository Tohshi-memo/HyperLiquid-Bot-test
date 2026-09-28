# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T22:52:34.053811+00:00`
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

- `news_risk_high->unknown_24h` score `2664.804` n `139` status `ready` deltaP `1.2153` edge `222.0589` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.2541` n `139` status `ready` deltaP `27.3794` edge `1.1505` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.2865` n `139` status `ready` deltaP `26.9771` edge `0.683` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.6464` n `139` status `ready` deltaP `22.6368` edge `0.8464` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.5312` n `139` status `ready` deltaP `32.6089` edge `0.1464` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.8284` n `139` status `ready` deltaP `24.9888` edge `0.2546` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6335` n `139` status `ready` deltaP `27.4785` edge `0.1972` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1047` n `139` status `ready` deltaP `9.108` edge `0.2973` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7502` n `139` status `ready` deltaP `7.4667` edge `0.1038` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5775` n `139` status `ready` deltaP `7.8534` edge `0.0619` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4707` n `139` status `ready` deltaP `8.9013` edge `0.0089` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0613` n `139` status `ready` deltaP `7.8775` edge `0.0277` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4669` n `139` status `ready` deltaP `1.9396` edge `0.0111` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5147` n `139` status `ready` deltaP `0.896` edge `0.0563` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2201` n `139` status `ready` deltaP `-9.8663` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3321` n `139` status `ready` deltaP `8.3052` edge `-0.0048` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3886` n `139` status `ready` deltaP `-8.6988` edge `0.0294` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8154` n `139` status `ready` deltaP `-5.2433` edge `0.0737` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0567` n `139` status `ready` deltaP `-12.3153` edge `-0.0141` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8066` n `139` status `ready` deltaP `-11.0173` edge `-0.0019` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

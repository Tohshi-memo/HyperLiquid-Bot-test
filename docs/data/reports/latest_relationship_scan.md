# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T13:52:34.033242+00:00`
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

- `news_risk_high->unknown_24h` score `2583.6336` n `139` status `ready` deltaP `1.2153` edge `215.2947` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0062` n `139` status `ready` deltaP `32.9349` edge `1.5928` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.6012` n `139` status `ready` deltaP `35.8313` edge `0.9002` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.7259` n `139` status `ready` deltaP `25.9355` edge `0.9977` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3533` n `139` status `ready` deltaP `39.9006` edge `0.1663` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8904` n `139` status `ready` deltaP `31.9332` edge `0.2968` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.748` n `142` status `ready` deltaP `27.9801` edge `0.2034` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0163` n `142` status `ready` deltaP `8.6332` edge `0.2931` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7022` n `142` status `ready` deltaP `6.6712` edge `0.1051` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6662` n `142` status `ready` deltaP `7.8519` edge `0.0693` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4946` n `142` status `ready` deltaP `8.8998` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0235` n `142` status `ready` deltaP `8.6826` edge `0.0294` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4367` n `142` status `ready` deltaP `1.8407` edge `0.06` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5229` n `142` status `ready` deltaP `1.0141` edge `0.0126` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3277` n `142` status `ready` deltaP `8.674` edge `-0.0067` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3768` n `142` status `ready` deltaP `-8.3068` edge `0.0283` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.784` n `142` status `ready` deltaP `-4.8352` edge `0.075` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8217` n `142` status `ready` deltaP `-8.9947` edge `-0.0038` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9235` n `142` status `ready` deltaP `-10.2028` edge `-0.0111` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.4089` n `142` status `ready` deltaP `-10.3744` edge `0.0022` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

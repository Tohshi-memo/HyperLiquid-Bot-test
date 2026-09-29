# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T00:07:28.222692+00:00`
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

- `news_risk_high->unknown_24h` score `2655.7224` n `139` status `ready` deltaP `1.2153` edge `221.3021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9752` n `139` status `ready` deltaP `28.2474` edge `1.2048` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.7327` n `139` status `ready` deltaP `27.8452` edge `0.7144` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.9438` n `139` status `ready` deltaP `23.5049` edge `0.8654` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.6343` n `139` status `ready` deltaP `33.477` edge `0.1492` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.0155` n `139` status `ready` deltaP `25.8569` edge `0.2644` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6347` n `139` status `ready` deltaP `27.4785` edge `0.1973` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0107` n `139` status `ready` deltaP `8.8031` edge `0.2915` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6698` n `139` status `ready` deltaP `7.1673` edge `0.0991` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5895` n `139` status `ready` deltaP `7.8534` edge `0.0629` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4851` n `139` status `ready` deltaP `9.051` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1003` n `139` status `ready` deltaP `7.4202` edge `0.0275` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4788` n `139` status `ready` deltaP `1.7899` edge `0.0111` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5724` n `139` status `ready` deltaP `0.4469` edge `0.0519` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2255` n `139` status `ready` deltaP `-9.8663` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3478` n `139` status `ready` deltaP `8.1527` edge `-0.0058` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4051` n `139` status `ready` deltaP `-8.8513` edge `0.0283` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8992` n `139` status `ready` deltaP `-5.7006` edge `0.066` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0194` n `139` status `ready` deltaP `-11.7165` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7836` n `139` status `ready` deltaP `-10.8649` edge `-0.001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

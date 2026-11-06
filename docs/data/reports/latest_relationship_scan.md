# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T22:22:27.768222+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4102`

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

- `news_risk_high->equity_4h` score `1.298` n `81` status `ready` deltaP `11.5609` edge `0.1799` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.3657` n `81` status `ready` deltaP `11.4235` edge `0.0185` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.3014` n `81` status `ready` deltaP `5.4428` edge `0.0573` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.2696` n `81` status `ready` deltaP `11.3551` edge `0.0042` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.138` n `81` status `ready` deltaP `7.9777` edge `0.0029` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.1347` n `81` status `ready` deltaP `1.4614` edge `0.1398` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.1873` n `81` status `ready` deltaP `-0.8173` edge `0.0341` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2602` n `81` status `ready` deltaP `2.2991` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.409` n `81` status `ready` deltaP `-1.6652` edge `-0.0056` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.7786` n `81` status `ready` deltaP `-1.9258` edge `0.0069` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-0.9209` n `81` status `ready` deltaP `0.5433` edge `0.0011` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-1.1572` n `81` status `ready` deltaP `-2.8117` edge `0.039` maxDD `-9.1553`
- `news_risk_high->metal_4h` score `-1.2076` n `81` status `ready` deltaP `-3.9408` edge `-0.038` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-2.1028` n `81` status `ready` deltaP `24.4432` edge `0.7261` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-2.6197` n `81` status `ready` deltaP `-6.3328` edge `-0.03` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.9887` n `81` status `ready` deltaP `-18.6497` edge `-0.007` maxDD `-1.7518`
- `news_risk_high->metal_24h` score `-3.0835` n `81` status `ready` deltaP `2.758` edge `-0.2241` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9871` n `81` status `ready` deltaP `-25.6286` edge `-0.0016` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-9.3969` n `81` status `ready` deltaP `-26.1934` edge `-0.0358` maxDD `-28.4791`
- `news_risk_high->crypto_major_24h` score `-11.8941` n `81` status `ready` deltaP `-24.7876` edge `0.0244` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

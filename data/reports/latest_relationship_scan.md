# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T21:37:35.689215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7484`

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

- `market_context_high->fx_1h` score `0.8135` n `72` status `ready` deltaP `13.2485` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.5991` n `66` status `ready` deltaP `11.9872` edge `0.0096` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2414` n `72` status `ready` deltaP `7.2438` edge `0.0041` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.028` n `72` status `ready` deltaP `3.3766` edge `0.0085` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2072` n `72` status `ready` deltaP `6.2375` edge `-0.0079` maxDD `-2.1532`
- `market_context_high->index_1h` score `-0.4472` n `72` status `ready` deltaP `-0.7485` edge `-0.003` maxDD `-0.2813`
- `market_context_high->metal_4h` score `-0.4526` n `66` status `ready` deltaP `0.9146` edge `0.0081` maxDD `-0.4441`
- `market_context_high->crypto_major_1h` score `-1.2166` n `72` status `ready` deltaP `-4.4661` edge `0.0013` maxDD `-7.5329`
- `market_context_high->equity_4h` score `-3.8796` n `66` status `ready` deltaP `-19.697` edge `-0.1624` maxDD `-6.9605`
- `market_context_high->commodity_4h` score `-4.1127` n `66` status `ready` deltaP `-25.1294` edge `-0.0174` maxDD `-2.9572`
- `market_context_high->crypto_alt_1h` score `-4.4006` n `72` status `ready` deltaP `-9.506` edge `-0.108` maxDD `-11.9607`
- `market_context_high->index_4h` score `-4.466` n `66` status `ready` deltaP `-26.2149` edge `-0.0226` maxDD `-0.984`
- `market_context_high->crypto_major_4h` score `-9.6178` n `66` status `ready` deltaP `-11.9226` edge `-0.2715` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-20.1381` n `66` status `ready` deltaP `-34.9732` edge `-0.6904` maxDD `-49.3697`
- `market_context_high->unknown_4h` score `-543.0783` n `66` status `ready` deltaP `4.4299` edge `-45.2811` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1319.0203` n `72` status `ready` deltaP `1.4388` edge `-109.9163` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2947.2194` n `27` status `thin_sample` deltaP `8.3832` edge `272.8348` maxDD `0.0`
- `news_risk_high->unknown_4h` score `267.5239` n `27` status `thin_sample` deltaP `5.9451` edge `24.7311` maxDD `0.0`
- `risk_on_high->unknown_4h` score `27.0347` n `2` status `thin_sample` deltaP `5.9451` edge `33.7537` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `27.0347` n `2` status `thin_sample` deltaP `5.9451` edge `33.7537` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

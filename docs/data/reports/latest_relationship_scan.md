# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T21:52:34.873790+00:00`
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

- `market_context_high->fx_1h` score `0.8146` n `72` status `ready` deltaP `13.2485` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.6467` n `67` status `ready` deltaP `12.5978` edge `0.0095` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2283` n `72` status `ready` deltaP `7.0941` edge `0.004` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0373` n `72` status `ready` deltaP `3.2269` edge `0.0083` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2158` n `72` status `ready` deltaP `6.0878` edge `-0.008` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.4217` n `67` status `ready` deltaP `1.5085` edge `0.0081` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.455` n `72` status `ready` deltaP `-0.8982` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2181` n `72` status `ready` deltaP `-4.4661` edge `0.0011` maxDD `-7.5329`
- `market_context_high->equity_4h` score `-3.7998` n `67` status `ready` deltaP `-18.6567` edge `-0.1591` maxDD `-6.9605`
- `market_context_high->commodity_4h` score `-3.9816` n `67` status `ready` deltaP `-24.1058` edge `-0.0133` maxDD `-2.9572`
- `market_context_high->index_4h` score `-4.3707` n `67` status `ready` deltaP `-25.0842` edge `-0.0222` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3862` n `72` status `ready` deltaP `-9.3563` edge `-0.1078` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.4964` n `67` status `ready` deltaP `-11.0347` edge `-0.2673` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-20.078` n `67` status `ready` deltaP `-34.979` edge `-0.6805` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-552.1412` n `67` status `ready` deltaP `4.4526` edge `-46.0365` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1315.2115` n `72` status `ready` deltaP `1.4388` edge `-109.5989` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2924.7284` n `26` status `thin_sample` deltaP `8.3832` edge `281.168` maxDD `0.0`
- `news_risk_high->unknown_4h` score `251.7178` n `26` status `thin_sample` deltaP `5.9451` edge `24.164` maxDD `0.0`
- `risk_on_high->unknown_4h` score `27.2271` n `2` status `thin_sample` deltaP `5.9451` edge `33.9942` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `27.2271` n `2` status `thin_sample` deltaP `5.9451` edge `33.9942` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

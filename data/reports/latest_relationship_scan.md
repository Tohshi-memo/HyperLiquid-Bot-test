# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T12:37:26.850985+00:00`
- Price records: `672`
- Market context records: `6918`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1701` n `224` status `ready` deltaP `3.5848` edge `0.0028` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2283` n `202` status `ready` deltaP `-4.8646` edge `0.4048` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3767` n `224` status `ready` deltaP `3.109` edge `0.0243` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4651` n `224` status `ready` deltaP `4.5953` edge `0.021` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6104` n `224` status `ready` deltaP `-0.5988` edge `-0.0058` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7238` n `224` status `ready` deltaP `-0.131` edge `-0.0008` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7378` n `224` status `ready` deltaP `15.2222` edge `0.0103` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.795` n `224` status `ready` deltaP `-3.2453` edge `-0.0035` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4151` n `224` status `ready` deltaP `-2.6459` edge `-0.0148` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5367` n `224` status `ready` deltaP `-2.3631` edge `-0.0222` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6391` n `224` status `ready` deltaP `3.4324` edge `-0.015` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7894` n `224` status `ready` deltaP `6.6856` edge `-0.016` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.0717` n `224` status `ready` deltaP `3.8436` edge `0.0071` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6486` n `224` status `ready` deltaP `2.6677` edge `0.001` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7634` n `224` status `ready` deltaP `0.0653` edge `-0.022` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.8787` n `202` status `ready` deltaP `-2.5156` edge `-0.0363` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9135` n `224` status `ready` deltaP `-7.0558` edge `0.0408` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0388` n `202` status `ready` deltaP `-4.0711` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.8856` n `224` status `ready` deltaP `4.0832` edge `-0.1155` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2412` n `202` status `ready` deltaP `-11.8426` edge `-0.1114` maxDD `-28.9634`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

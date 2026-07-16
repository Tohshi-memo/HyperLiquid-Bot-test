# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T17:07:31.316982+00:00`
- Price records: `672`
- Market context records: `6939`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2573` n `235` status `ready` deltaP `2.0563` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5224` n `235` status `ready` deltaP `2.3016` edge `0.0187` maxDD `-3.8726`
- `market_context_high->metal_1h` score `-0.7312` n `235` status `ready` deltaP `-2.3334` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7404` n `235` status `ready` deltaP `-0.4498` edge `-0.0008` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8202` n `224` status `ready` deltaP `13.6978` edge `0.0099` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-0.9887` n `235` status `ready` deltaP `2.7507` edge `0.0123` maxDD `-6.0423`
- `market_context_high->unknown_24h` score `-1.1104` n `217` status `ready` deltaP `-7.6983` edge `0.3332` maxDD `-16.2722`
- `market_context_high->commodity_1h` score `-1.2209` n `235` status `ready` deltaP `-2.5373` edge `-0.0144` maxDD `-2.3006`
- `market_context_high->commodity_4h` score `-1.5846` n `224` status `ready` deltaP `-3.8655` edge `-0.0284` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6069` n `235` status `ready` deltaP `-2.1754` edge `-0.0293` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6188` n `224` status `ready` deltaP `9.1246` edge `-0.0104` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9403` n `224` status `ready` deltaP `5.2156` edge `0.0148` maxDD `-5.5324`
- `market_context_high->equity_1h` score `-1.9567` n `235` status `ready` deltaP `2.206` edge `-0.0193` maxDD `-15.3676`
- `market_context_high->crypto_major_4h` score `-2.7659` n `224` status `ready` deltaP `-0.0871` edge `-0.0213` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-2.7805` n `224` status `ready` deltaP `1.6006` edge `-0.0088` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-2.9827` n `224` status `ready` deltaP `-7.6655` edge `0.0391` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.433` n `217` status `ready` deltaP `-4.4493` edge `-0.0696` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.2461` n `217` status `ready` deltaP `-5.9573` edge `-0.0105` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4267` n `224` status `ready` deltaP `6.2173` edge `-0.0709` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9083` n `217` status `ready` deltaP `-13.3737` edge `-0.1189` maxDD `-34.3887`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

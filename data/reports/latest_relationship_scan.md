# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T22:37:21.090079+00:00`
- Price records: `672`
- Market context records: `3223`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->commodity_24h` score `13.8718` n `102` status `ready` deltaP `49.5609` edge `0.8684` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.1975` n `102` status `ready` deltaP `17.4429` edge `2.5656` maxDD `-70.5257`
- `market_context_high->index_24h` score `9.6678` n `102` status `ready` deltaP `31.7402` edge `0.8495` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.1093` n `102` status `ready` deltaP `17.5143` edge `1.5081` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3788` n `128` status `ready` deltaP `22.8849` edge `0.1748` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.3524` n `140` status `ready` deltaP `6.5441` edge `0.028` maxDD `-1.7142`
- `market_context_high->crypto_major_24h` score `-0.1779` n `102` status `ready` deltaP `19.0359` edge `2.0098` maxDD `-157.4278`
- `market_context_high->crypto_alt_1h` score `-0.8375` n `140` status `ready` deltaP `3.8238` edge `0.0926` maxDD `-14.7034`
- `market_context_high->unknown_4h` score `-0.8501` n `128` status `ready` deltaP `7.6029` edge `0.0669` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.8818` n `140` status `ready` deltaP `3.3747` edge `0.0103` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.8999` n `102` status `ready` deltaP `-0.1328` edge `-0.0149` maxDD `-1.6335`
- `market_context_high->crypto_major_1h` score `-0.924` n `140` status `ready` deltaP `3.9948` edge `0.0812` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.0065` n `140` status `ready` deltaP `3.1908` edge `0.0066` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.8386` n `140` status `ready` deltaP `-11.775` edge `-0.0055` maxDD `-0.8706`
- `market_context_high->index_4h` score `-1.9263` n `128` status `ready` deltaP `11.5473` edge `0.0534` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.9487` n `128` status `ready` deltaP `-9.7371` edge `-0.009` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.366` n `140` status `ready` deltaP `-4.5509` edge `-0.0173` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.9547` n `140` status `ready` deltaP `0.9581` edge `-0.1373` maxDD `-17.8311`
- `market_context_high->crypto_alt_4h` score `-4.5325` n `128` status `ready` deltaP `7.6792` edge `0.1722` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.9259` n `128` status `ready` deltaP `3.5251` edge `0.1358` maxDD `-54.2659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

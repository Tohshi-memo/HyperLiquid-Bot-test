# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T15:52:25.424287+00:00`
- Price records: `672`
- Market context records: `3088`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.966` n `86` status `ready` deltaP `12.7664` edge `2.5312` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.051` n `86` status `ready` deltaP `45.6113` edge `0.993` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.1401` n `86` status `ready` deltaP `21.1362` edge `1.0839` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.8532` n `86` status `ready` deltaP `34.5203` edge `0.939` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.2483` n `86` status `ready` deltaP `22.4443` edge `1.4705` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `2.9668` n `120` status `ready` deltaP `18.1402` edge `0.1721` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.0698` n `120` status `ready` deltaP `3.6077` edge `0.0871` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.1669` n `125` status `ready` deltaP `0.503` edge `0.025` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5231` n `125` status `ready` deltaP `3.497` edge `0.0159` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.757` n `125` status `ready` deltaP `3.7964` edge `0.0906` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-1.0277` n `86` status `ready` deltaP `0.8277` edge `-0.0053` maxDD `-0.5357`
- `market_context_high->fx_1h` score `-1.1646` n `125` status `ready` deltaP `-8.6527` edge `-0.0021` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2408` n `125` status `ready` deltaP `-1.4994` edge `-0.0005` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3139` n `120` status `ready` deltaP `-11.7277` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4219` n `120` status `ready` deltaP `9.4817` edge `0.0454` maxDD `-17.6057`
- `market_context_high->unknown_1h` score `-1.6736` n `125` status `ready` deltaP `1.1581` edge `-0.0427` maxDD `-5.6925`
- `market_context_high->crypto_major_1h` score `-2.0108` n `125` status `ready` deltaP `-0.012` edge `0.0588` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3372` n `125` status `ready` deltaP `-6.6599` edge `-0.011` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-3.2802` n `120` status `ready` deltaP `16.5955` edge `0.2733` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8121` n `120` status `ready` deltaP `8.0284` edge `-0.0184` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

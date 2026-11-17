# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T16:52:55.568222+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1495.4636` n `98` status `ready` deltaP `3.4602` edge `124.5989` maxDD `0.0`
- `news_risk_high->equity_24h` score `60.6243` n `45` status `ready` deltaP `67.4625` edge `4.6729` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `18.4817` n `45` status `ready` deltaP `52.6558` edge `1.2173` maxDD `-1.9227`
- `news_risk_high->crypto_major_24h` score `18.2177` n `45` status `ready` deltaP `34.3406` edge `2.221` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8525` n `98` status `ready` deltaP `44.386` edge `1.9353` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0838` n `98` status `ready` deltaP `30.4463` edge `1.815` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.4612` n `45` status `ready` deltaP `58.812` edge `0.4267` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.5502` n `45` status `ready` deltaP `19.1311` edge `1.4192` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.5227` n `45` status `ready` deltaP `54.4983` edge `0.3469` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.3813` n `45` status `ready` deltaP `32.5678` edge `0.4747` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `6.8453` n `45` status `ready` deltaP `25.5962` edge `0.4425` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.3562` n `45` status `ready` deltaP `52.8727` edge `0.1836` maxDD `-0.1787`
- `news_risk_high->equity_1h` score `4.8104` n `45` status `ready` deltaP `24.2548` edge `0.2777` maxDD `-1.7492`
- `news_risk_high->index_4h` score `4.1496` n `45` status `ready` deltaP `36.8191` edge `0.1236` maxDD `-0.1941`
- `news_risk_high->crypto_major_1h` score `3.0576` n `45` status `ready` deltaP `20.835` edge `0.1562` maxDD `-1.8907`
- `news_risk_high->commodity_4h` score `3.0278` n `45` status `ready` deltaP `31.5244` edge `0.0675` maxDD `-0.3611`
- `news_risk_high->crypto_alt_1h` score `2.6232` n `45` status `ready` deltaP `19.6607` edge `0.1402` maxDD `-2.5469`
- `news_risk_high->metal_1h` score `2.4897` n `45` status `ready` deltaP `27.5017` edge `0.0481` maxDD `-0.2506`
- `news_risk_high->index_1h` score `1.6538` n `45` status `ready` deltaP `20.1098` edge `0.0273` maxDD `-0.217`
- `news_risk_high->metal_24h` score `0.4454` n `45` status `ready` deltaP `14.8481` edge `0.1754` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

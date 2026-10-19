# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T16:22:36.875982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8290`

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

- `market_context_high->commodity_24h` score `2.1506` n `76` status `ready` deltaP `19.3896` edge `0.1351` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.4828` n `43` status `ready` deltaP `13.8978` edge `0.0054` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.4828` n `43` status `ready` deltaP `13.8978` edge `0.0054` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4387` n `43` status `ready` deltaP `10.1553` edge `-0.0008` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4387` n `43` status `ready` deltaP `10.1553` edge `-0.0008` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.2998` n `43` status `ready` deltaP `14.7691` edge `0.0063` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2998` n `43` status `ready` deltaP `14.7691` edge `0.0063` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1653` n `43` status `ready` deltaP `1.0104` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1653` n `43` status `ready` deltaP `1.0104` edge `0.0059` maxDD `-0.1126`
- `market_context_high->crypto_major_4h` score `-0.2009` n `79` status `ready` deltaP `1.7134` edge `0.3123` maxDD `-15.9584`
- `risk_on_high->fx_1h` score `-0.2566` n `43` status `ready` deltaP `0.4143` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2566` n `43` status `ready` deltaP `0.4143` edge `-0.001` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.2808` n `90` status `ready` deltaP `1.3007` edge `0.057` maxDD `-4.8007`
- `market_context_high->index_1h` score `-0.359` n `90` status `ready` deltaP `3.2302` edge `-0.0008` maxDD `-1.0073`
- `market_context_high->crypto_major_24h` score `-0.4207` n `76` status `ready` deltaP `-2.4214` edge `0.5719` maxDD `-35.1086`
- `market_context_high->metal_1h` score `-0.4218` n `90` status `ready` deltaP `-2.7113` edge `0.0015` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.58` n `79` status `ready` deltaP `-2.0511` edge `0.0032` maxDD `-0.777`
- `risk_on_high->index_4h` score `-0.679` n `43` status `ready` deltaP `4.1726` edge `0.0023` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.679` n `43` status `ready` deltaP `4.1726` edge `0.0023` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.7008` n `79` status `ready` deltaP `-1.5341` edge `0.0459` maxDD `-1.0418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

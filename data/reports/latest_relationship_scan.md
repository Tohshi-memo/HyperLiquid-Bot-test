# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T18:37:30.285216+00:00`
- Price records: `672`
- Market context records: `6418`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.7361` n `32` status `ready` deltaP `32.6389` edge `0.8585` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6521` n `32` status `ready` deltaP `56.0764` edge `0.1805` maxDD `0.0`
- `market_context_high->unknown_24h` score `5.9073` n `146` status `ready` deltaP `15.7059` edge `0.7176` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2289` n `32` status `ready` deltaP `44.1311` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1415` n `32` status `ready` deltaP `35.5903` edge `0.1284` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.7701` n `32` status `ready` deltaP `14.2361` edge `0.4664` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4991` n `32` status `ready` deltaP `14.2777` edge `0.1437` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8653` n `32` status `ready` deltaP `10.2732` edge `0.0886` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.681` n `204` status `ready` deltaP `-6.2757` edge `0.1994` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3717` n `201` status `ready` deltaP `11.0098` edge `0.0414` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1939` n `201` status `ready` deltaP `9.1334` edge `0.0229` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2549` n `32` status `ready` deltaP `6.5307` edge `-0.0303` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2883` n `146` status `ready` deltaP `18.5978` edge `0.0959` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.5339` n `201` status `ready` deltaP `7.8805` edge `0.0489` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.5462` n `204` status `ready` deltaP `0.8307` edge `0.0022` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5885` n `32` status `ready` deltaP `-0.1497` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7039` n `204` status `ready` deltaP `-2.9001` edge `-0.0026` maxDD `-2.1314`
- `market_context_high->commodity_24h` score `-0.7091` n `146` status `ready` deltaP `-2.2094` edge `0.1158` maxDD `-5.6914`
- `market_context_high->fx_1h` score `-0.7097` n `204` status `ready` deltaP `-0.6018` edge `-0.0019` maxDD `-0.9252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

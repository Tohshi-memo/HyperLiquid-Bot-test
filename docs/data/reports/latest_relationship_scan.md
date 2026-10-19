# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T15:07:38.155617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `2.0211` n `76` status `ready` deltaP `18.5215` edge `0.1301` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5259` n `43` status `ready` deltaP `14.0475` edge `0.008` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5259` n `43` status `ready` deltaP `14.0475` edge `0.008` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4435` n `43` status `ready` deltaP `10.1553` edge `-0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4435` n `43` status `ready` deltaP `10.1553` edge `-0.0004` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.1704` n `43` status `ready` deltaP `13.901` edge `0.0013` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1704` n `43` status `ready` deltaP `13.901` edge `0.0013` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.1062` n `77` status `ready` deltaP `3.2348` edge `0.3325` maxDD `-15.2359`
- `risk_on_high->fx_4h` score `-0.1141` n `43` status `ready` deltaP `1.6201` edge `0.0061` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1141` n `43` status `ready` deltaP `1.6201` edge `0.0061` maxDD `-0.1126`
- `market_context_high->crypto_major_1h` score `-0.2039` n `85` status `ready` deltaP `2.1504` edge `0.0612` maxDD `-4.8007`
- `market_context_high->crypto_major_24h` score `-0.2071` n `76` status `ready` deltaP `-1.5534` edge `0.5935` maxDD `-35.1086`
- `risk_on_high->fx_1h` score `-0.2395` n `43` status `ready` deltaP `0.7137` edge `-0.0008` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2395` n `43` status `ready` deltaP `0.7137` edge `-0.0008` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.4764` n `85` status `ready` deltaP `-3.6263` edge `0.0006` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5448` n `77` status `ready` deltaP `-1.4908` edge `0.0038` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.5802` n `77` status `ready` deltaP `-0.3505` edge `0.0502` maxDD `-0.7797`
- `risk_on_high->index_4h` score `-0.6048` n `43` status `ready` deltaP `4.9348` edge `0.0034` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6048` n `43` status `ready` deltaP `4.9348` edge `0.0034` maxDD `-0.9359`
- `market_context_high->index_1h` score `-0.6394` n `85` status `ready` deltaP `2.5766` edge `-0.0037` maxDD `-1.0073`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

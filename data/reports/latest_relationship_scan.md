# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T08:37:24.982717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.7104` n `51` status `ready` deltaP `26.5453` edge `1.0535` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9977` n `33` status `ready` deltaP `-8.1791` edge `0.7401` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9977` n `33` status `ready` deltaP `-8.1791` edge `0.7401` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7264` n `51` status `ready` deltaP `19.6283` edge `0.2101` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9452` n `51` status `ready` deltaP `24.9462` edge `0.1564` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.8452` n `51` status `ready` deltaP `33.8146` edge `0.0251` maxDD `-0.0746`
- `risk_on_high->metal_4h` score `2.3466` n `31` status `ready` deltaP `30.8468` edge `-0.0013` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3466` n `31` status `ready` deltaP `30.8468` edge `-0.0013` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6568` n `31` status `ready` deltaP `-3.1373` edge `0.2764` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6568` n `31` status `ready` deltaP `-3.1373` edge `0.2764` maxDD `-0.7794`
- `risk_on_high->fx_4h` score `1.4802` n `31` status `ready` deltaP `19.7728` edge `0.0055` maxDD `-0.1176`
- `risk_on_and_context->fx_4h` score `1.4802` n `31` status `ready` deltaP `19.7728` edge `0.0055` maxDD `-0.1176`
- `market_context_high->unknown_1h` score `1.4244` n `134` status `ready` deltaP `8.9172` edge `0.1041` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.211` n `51` status `ready` deltaP `16.696` edge `0.0066` maxDD `-0.0257`
- `market_context_high->commodity_24h` score `1.172` n `106` status `ready` deltaP `2.3356` edge `0.1159` maxDD `-0.7042`
- `market_context_high->unknown_4h` score `0.9481` n `123` status `ready` deltaP `22.002` edge `-0.0505` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.8454` n `51` status `ready` deltaP `18.3427` edge `0.0226` maxDD `-0.9204`
- `risk_on_high->index_4h` score `0.7923` n `31` status `ready` deltaP `14.1866` edge `0.0463` maxDD `-0.1441`
- `risk_on_and_context->index_4h` score `0.7923` n `31` status `ready` deltaP `14.1866` edge `0.0463` maxDD `-0.1441`
- `news_risk_high->index_4h` score `0.7056` n `51` status `ready` deltaP `11.7198` edge `0.0204` maxDD `-0.1788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

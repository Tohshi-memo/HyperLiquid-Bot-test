# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T08:22:26.266853+00:00`
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

- `news_risk_high->unknown_4h` score `14.7176` n `51` status `ready` deltaP `26.5453` edge `1.0541` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9985` n `33` status `ready` deltaP `-8.1791` edge `0.7402` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9985` n `33` status `ready` deltaP `-8.1791` edge `0.7402` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7276` n `51` status `ready` deltaP `19.6283` edge `0.2102` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9586` n `51` status `ready` deltaP `25.0986` edge `0.1565` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.8452` n `51` status `ready` deltaP `33.8146` edge `0.0251` maxDD `-0.0746`
- `risk_on_high->metal_4h` score `2.5775` n `30` status `ready` deltaP `33.5976` edge `-0.0004` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.5775` n `30` status `ready` deltaP `33.5976` edge `-0.0004` maxDD `-0.0367`
- `risk_on_high->fx_4h` score `1.7553` n `30` status `ready` deltaP `22.246` edge `0.0072` maxDD `-0.0719`
- `risk_on_and_context->fx_4h` score `1.7553` n `30` status `ready` deltaP `22.246` edge `0.0072` maxDD `-0.0719`
- `risk_on_high->equity_4h` score `1.6283` n `30` status `ready` deltaP `-4.7053` edge `0.2832` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6283` n `30` status `ready` deltaP `-4.7053` edge `0.2832` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4172` n `135` status `ready` deltaP `9.1273` edge `0.1021` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1966` n `51` status `ready` deltaP `16.5463` edge `0.0064` maxDD `-0.0257`
- `market_context_high->commodity_24h` score `1.0757` n `106` status `ready` deltaP `2.3356` edge `0.1146` maxDD `-0.9093`
- `risk_on_high->index_4h` score `0.9462` n `30` status `ready` deltaP `16.2296` edge `0.048` maxDD `-0.1248`
- `risk_on_and_context->index_4h` score `0.9462` n `30` status `ready` deltaP `16.2296` edge `0.048` maxDD `-0.1248`
- `market_context_high->unknown_4h` score `0.9133` n `123` status `ready` deltaP `22.002` edge `-0.0534` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.8547` n `51` status `ready` deltaP `18.4924` edge `0.0228` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.7056` n `51` status `ready` deltaP `11.7198` edge `0.0204` maxDD `-0.1788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

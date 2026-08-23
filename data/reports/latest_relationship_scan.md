# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T09:07:25.441950+00:00`
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

- `news_risk_high->unknown_4h` score `14.6924` n `51` status `ready` deltaP `26.5453` edge `1.052` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9969` n `33` status `ready` deltaP `-8.1791` edge `0.74` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9969` n `33` status `ready` deltaP `-8.1791` edge `0.74` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7252` n `51` status `ready` deltaP `19.6283` edge `0.21` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9148` n `51` status `ready` deltaP `24.6413` edge `0.1559` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.8464` n `51` status `ready` deltaP `33.8146` edge `0.0252` maxDD `-0.0746`
- `risk_on_high->metal_4h` score `2.3924` n `33` status `ready` deltaP `31.6288` edge `-0.0027` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3924` n `33` status `ready` deltaP `31.6288` edge `-0.0027` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.7318` n `33` status `ready` deltaP `-0.3141` edge `0.2672` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.7318` n `33` status `ready` deltaP `-0.3141` edge `0.2672` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4477` n `132` status `ready` deltaP `8.4875` edge `0.1089` maxDD `-1.5876`
- `market_context_high->commodity_24h` score `1.2503` n `106` status `ready` deltaP `2.3356` edge `0.1182` maxDD `-0.6996`
- `news_risk_high->fx_1h` score `1.2242` n `51` status `ready` deltaP `16.8457` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.0261` n `123` status `ready` deltaP `22.002` edge `-0.044` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.836` n `51` status `ready` deltaP `18.193` edge `0.0224` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.7056` n `51` status `ready` deltaP `11.7198` edge `0.0204` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6367` n `33` status `ready` deltaP `15.2763` edge `0.003` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6367` n `33` status `ready` deltaP `15.2763` edge `0.003` maxDD `-0.1905`
- `risk_on_high->unknown_4h` score `0.5393` n `33` status `ready` deltaP `28.5061` edge `-0.1451` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `0.5393` n `33` status `ready` deltaP `28.5061` edge `-0.1451` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

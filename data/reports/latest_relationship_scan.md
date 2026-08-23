# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T07:52:24.689213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `news_risk_high->unknown_4h` score `14.7416` n `51` status `ready` deltaP `26.5453` edge `1.0561` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0249` n `33` status `ready` deltaP `-7.8796` edge `0.7416` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0249` n `33` status `ready` deltaP `-7.8796` edge `0.7416` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7683` n `51` status `ready` deltaP `19.9278` edge `0.2116` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9586` n `51` status `ready` deltaP `25.0986` edge `0.1565` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.844` n `51` status `ready` deltaP `33.8146` edge `0.025` maxDD `-0.0746`
- `market_context_high->unknown_1h` score `1.2579` n `135` status `ready` deltaP `7.9453` edge `0.0967` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.193` n `51` status `ready` deltaP `16.5463` edge `0.0061` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.857` n `51` status `ready` deltaP `18.4924` edge `0.0231` maxDD `-0.9204`
- `market_context_high->commodity_24h` score `0.816` n `106` status `ready` deltaP `1.5658` edge `0.1115` maxDD `-1.315`
- `market_context_high->unknown_4h` score `0.8089` n `123` status `ready` deltaP `22.002` edge `-0.0621` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.7044` n `51` status `ready` deltaP `11.7198` edge `0.0203` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.248` n `51` status `ready` deltaP `9.572` edge `0.0033` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2278` n `33` status `ready` deltaP `6.5642` edge `0.0031` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2278` n `33` status `ready` deltaP `6.5642` edge `0.0031` maxDD `-0.0796`
- `market_context_high->fx_4h` score `0.2151` n `123` status `ready` deltaP `8.1809` edge `0.0093` maxDD `-0.3395`
- `news_risk_high->commodity_1h` score `0.1488` n `51` status `ready` deltaP `8.0897` edge `-0.0107` maxDD `-0.4666`
- `news_risk_high->metal_4h` score `0.0638` n `51` status `ready` deltaP `10.2643` edge `-0.01` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1006` n `51` status `ready` deltaP `2.4921` edge `-0.0072` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1204` n `135` status `ready` deltaP `2.9951` edge `0.0058` maxDD `-0.1974`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

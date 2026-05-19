# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T05:52:16.684401+00:00`
- Price records: `672`
- Market context records: `1191`
- Flow alert records: `5335`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.471` n `138` status `ready` deltaP `44.4067` edge `1.3564` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.7245` n `138` status `ready` deltaP `22.1317` edge `0.6978` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `4.2896` n `138` status `ready` deltaP `4.233` edge `0.4509` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.2411` n `138` status `ready` deltaP `-3.744` edge `0.5451` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8643` n `138` status `ready` deltaP `15.1975` edge `0.2037` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.289` n `138` status `ready` deltaP `16.01` edge `0.3167` maxDD `-14.2815`
- `market_context_high->index_24h` score `2.1082` n `138` status `ready` deltaP `15.7232` edge `0.1795` maxDD `-5.3574`
- `market_context_high->index_4h` score `1.0166` n `138` status `ready` deltaP `10.7723` edge `0.0812` maxDD `-2.1308`
- `market_context_high->commodity_24h` score `0.6278` n `138` status `ready` deltaP `-3.827` edge `0.5244` maxDD `-28.4719`
- `market_context_high->index_1h` score `0.5718` n `138` status `ready` deltaP `8.9907` edge `0.0194` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5084` n `138` status `ready` deltaP `4.5951` edge `0.0495` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0285` n `138` status `ready` deltaP `7.7788` edge `0.1366` maxDD `-8.3693`
- `market_context_high->fx_24h` score `-0.0482` n `138` status `ready` deltaP `7.9181` edge `0.0454` maxDD `-5.0163`
- `market_context_high->fx_1h` score `-0.127` n `138` status `ready` deltaP `4.5279` edge `-0.0009` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2021` n `138` status `ready` deltaP `8.3551` edge `-0.0115` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.2959` n `138` status `ready` deltaP `4.0246` edge `0.0118` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.4305` n `138` status `ready` deltaP `-0.0173` edge `0.0292` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.7596` n `138` status `ready` deltaP `2.6495` edge `0.192` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.9109` n `138` status `ready` deltaP `-3.0483` edge `0.0059` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1119` n `138` status `ready` deltaP `4.9266` edge `0.1211` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

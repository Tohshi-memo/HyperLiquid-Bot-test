# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T14:22:25.915021+00:00`
- Price records: `672`
- Market context records: `2047`
- Flow alert records: `7787`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `9.1674` n `205` status `ready` deltaP `32.1818` edge `0.6024` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4976` n `205` status `ready` deltaP `24.7053` edge `0.6579` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2363` n `205` status `ready` deltaP `19.7709` edge `0.4628` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0623` n `205` status `ready` deltaP `17.6017` edge `0.2473` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7915` n `205` status `ready` deltaP `17.5146` edge `0.6479` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6759` n `205` status `ready` deltaP `13.0765` edge `0.1511` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.6126` n `205` status `ready` deltaP `13.7312` edge `0.1112` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.3157` n `205` status `ready` deltaP `10.2322` edge `0.1528` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.8389` n `205` status `ready` deltaP `17.1829` edge `0.4452` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.7207` n `205` status `ready` deltaP `5.6849` edge `0.145` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.3375` n `205` status `ready` deltaP `7.6589` edge `0.0559` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1968` n `205` status `ready` deltaP `4.4947` edge `0.0584` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1563` n `205` status `ready` deltaP `3.6016` edge `0.022` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.492` n `205` status `ready` deltaP `11.2954` edge `0.023` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.7508` n `205` status `ready` deltaP `4.5567` edge `0.0258` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7871` n `205` status `ready` deltaP `-0.5433` edge `0.0008` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-0.8755` n `205` status `ready` deltaP `10.0808` edge `0.1221` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-1.1641` n `205` status `ready` deltaP `17.3964` edge `0.6456` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.4307` n `205` status `ready` deltaP `-4.5874` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9104` n `205` status `ready` deltaP `2.0067` edge `-0.0025` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

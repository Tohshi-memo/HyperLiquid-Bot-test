# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T23:22:16.945275+00:00`
- Price records: `672`
- Market context records: `1165`
- Flow alert records: `5255`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.8716` n `139` status `ready` deltaP `45.7334` edge `1.5476` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1714` n `139` status `ready` deltaP `22.1473` edge `0.9016` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.6965` n `139` status `ready` deltaP `21.6264` edge `0.5902` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.776` n `139` status `ready` deltaP `20.2375` edge `0.4022` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.482` n `139` status `ready` deltaP `-3.5772` edge `0.6474` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4347` n `155` status `ready` deltaP `12.1676` edge `0.1881` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0861` n `155` status `ready` deltaP `8.5661` edge `0.1017` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.7877` n `139` status `ready` deltaP `2.9414` edge `0.319` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.4643` n `155` status `ready` deltaP `7.4377` edge `0.0208` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2078` n `155` status `ready` deltaP `2.3227` edge `0.0396` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1818` n `155` status `ready` deltaP `8.9878` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1431` n `155` status `ready` deltaP `8.7097` edge `0.1524` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.014` n `155` status `ready` deltaP `6.8669` edge `0.029` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3629` n `155` status `ready` deltaP `2.6753` edge `0.0362` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.4651` n `155` status `ready` deltaP `5.6375` edge `-0.0153` maxDD `-2.2164`
- `market_context_high->unknown_4h` score `-0.6584` n `155` status `ready` deltaP `6.1182` edge `0.026` maxDD `-6.7322`
- `market_context_high->commodity_1h` score `-0.8365` n `155` status `ready` deltaP `-3.445` edge `-0.0035` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9861` n `155` status `ready` deltaP `-3.4176` edge `-0.004` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.2538` n `155` status `ready` deltaP `4.2673` edge `0.1073` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8926` n `155` status `ready` deltaP `5.0187` edge `-0.0807` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

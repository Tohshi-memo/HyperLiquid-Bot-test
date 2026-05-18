# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T20:37:19.953769+00:00`
- Price records: `672`
- Market context records: `1152`
- Flow alert records: `5219`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.0397` n `150` status `ready` deltaP `44.0347` edge `1.4896` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.7241` n `150` status `ready` deltaP `20.3958` edge `0.876` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.8995` n `150` status `ready` deltaP `19.875` edge `0.6188` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.2227` n `150` status `ready` deltaP `18.4861` edge `0.4511` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.7275` n `150` status `ready` deltaP `-1.8889` edge `0.6566` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5622` n `166` status `ready` deltaP `12.4871` edge `0.1966` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2208` n `166` status `ready` deltaP `9.6349` edge `0.1058` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5402` n `166` status `ready` deltaP `8.0712` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4758` n `166` status `ready` deltaP `3.8579` edge `0.0517` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.301` n `166` status `ready` deltaP `9.6459` edge `0.1664` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1705` n `166` status `ready` deltaP `7.9919` edge `0.0375` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0754` n `166` status `ready` deltaP `7.7033` edge `0.0005` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2092` n `166` status `ready` deltaP `7.1261` edge `-0.0039` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2179` n `166` status `ready` deltaP `3.4972` edge `0.0428` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.879` n `166` status `ready` deltaP `-1.5831` edge `-0.0025` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.8883` n `166` status `ready` deltaP `6.6614` edge `0.1382` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-1.1625` n `166` status `ready` deltaP `-2.1138` edge `-0.002` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.3775` n `166` status `ready` deltaP `7.2418` edge `-0.051` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-2.5214` n `150` status `ready` deltaP `4.507` edge `0.0328` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-2.9069` n `166` status `ready` deltaP `8.7019` edge `-0.1786` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

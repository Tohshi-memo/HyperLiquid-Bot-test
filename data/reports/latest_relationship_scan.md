# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T18:52:23.911164+00:00`
- Price records: `672`
- Market context records: `2996`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `17.9102` n `98` status `ready` deltaP `5.9843` edge `1.8443` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.2949` n `98` status `ready` deltaP `42.4674` edge `0.7525` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.6581` n `98` status `ready` deltaP `18.2221` edge `0.8965` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.5221` n `98` status `ready` deltaP `16.9572` edge `0.7975` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.2936` n `98` status `ready` deltaP `16.7411` edge `0.4276` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2816` n `101` status `ready` deltaP `16.9418` edge `0.1419` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.8355` n `101` status `ready` deltaP `19.0035` edge `0.1289` maxDD `-3.8774`
- `market_context_high->equity_4h` score `1.4488` n `101` status `ready` deltaP `14.4289` edge `0.1969` maxDD `-6.2547`
- `market_context_high->crypto_alt_4h` score `0.3417` n `101` status `ready` deltaP `23.1224` edge `0.3905` maxDD `-34.4002`
- `market_context_high->index_1h` score `0.0069` n `105` status `ready` deltaP `5.5375` edge `0.0242` maxDD `-2.4852`
- `market_context_high->commodity_1h` score `-0.0497` n `105` status `ready` deltaP `1.0337` edge `0.0197` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.3337` n `105` status `ready` deltaP `3.6998` edge `0.0345` maxDD `-5.1553`
- `market_context_high->fx_1h` score `-0.3588` n `105` status `ready` deltaP `-2.1771` edge `0.0007` maxDD `-0.2412`
- `market_context_high->fx_4h` score `-1.0879` n `101` status `ready` deltaP `-9.4059` edge `0.0011` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.092` n `105` status `ready` deltaP `6.3402` edge `0.0206` maxDD `-13.8964`
- `market_context_high->unknown_4h` score `-1.144` n `101` status `ready` deltaP `-0.3442` edge `0.0123` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.1842` n `105` status `ready` deltaP `-2.448` edge `-0.0106` maxDD `-6.3255`
- `market_context_high->crypto_major_1h` score `-1.5401` n `105` status `ready` deltaP `3.9193` edge `-0.0069` maxDD `-14.6674`
- `market_context_high->unknown_1h` score `-1.8736` n `105` status `ready` deltaP `1.2375` edge `-0.0913` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9442` n `98` status `ready` deltaP `-7.1747` edge `-0.027` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

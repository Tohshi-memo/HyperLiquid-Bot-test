# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T06:22:18.877652+00:00`
- Price records: `672`
- Market context records: `1294`
- Flow alert records: `5638`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8780`

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

- `market_context_high->crypto_major_24h` score `17.4013` n `128` status `ready` deltaP `41.5798` edge `1.2861` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.318` n `128` status `ready` deltaP `9.7222` edge `1.1284` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4538` n `128` status `ready` deltaP `27.5173` edge `0.806` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.8652` n `128` status `ready` deltaP `30.5556` edge `0.3937` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0224` n `128` status `ready` deltaP `25.3472` edge `0.5794` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4072` n `152` status `ready` deltaP `12.524` edge `0.1876` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3586` n `128` status `ready` deltaP `1.5625` edge `0.4591` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `0.925` n `128` status `ready` deltaP `-15.2778` edge `0.3271` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.5044` n `128` status `ready` deltaP `7.3785` edge `0.0393` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.2008` n `157` status `ready` deltaP `3.5174` edge `0.036` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.1123` n `157` status `ready` deltaP `6.2121` edge `0.0184` maxDD `-1.6329`
- `market_context_high->index_4h` score `0.0883` n `152` status `ready` deltaP `4.9984` edge `0.0869` maxDD `-3.7119`
- `market_context_high->metal_1h` score `0.0783` n `157` status `ready` deltaP `10.1396` edge `0.0079` maxDD `-2.8509`
- `market_context_high->metal_4h` score `0.0561` n `152` status `ready` deltaP `13.0456` edge `0.0608` maxDD `-6.4478`
- `market_context_high->unknown_4h` score `-0.0845` n `152` status `ready` deltaP `3.5221` edge `0.1966` maxDD `-11.1695`
- `market_context_high->fx_1h` score `-0.5242` n `157` status `ready` deltaP `0.8086` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5965` n `157` status `ready` deltaP `0.8467` edge `0.0317` maxDD `-3.6309`
- `market_context_high->crypto_major_4h` score `-0.7937` n `152` status `ready` deltaP `5.9451` edge `0.1295` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.826` n `157` status `ready` deltaP `-0.3185` edge `-0.0017` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.995` n `152` status `ready` deltaP `10.1011` edge `0.1817` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

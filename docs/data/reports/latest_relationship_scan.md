# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T11:52:15.806221+00:00`
- Price records: `672`
- Market context records: `1523`
- Flow alert records: `6298`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.8597` n `164` status `ready` deltaP `23.5984` edge `1.0977` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4352` n `164` status `ready` deltaP `28.8999` edge `0.9619` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5287` n `164` status `ready` deltaP `28.197` edge `0.8026` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7676` n `164` status `ready` deltaP `19.9356` edge `0.2897` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.493` n `164` status `ready` deltaP `13.1606` edge `0.3527` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9666` n `164` status `ready` deltaP `18.7881` edge `0.0602` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.5589` n `189` status `ready` deltaP `4.4183` edge `0.1021` maxDD `-3.7982`
- `market_context_high->fx_1h` score `-0.5743` n `199` status `ready` deltaP `-1.096` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6154` n `199` status `ready` deltaP `-0.5296` edge `0.027` maxDD `-4.1892`
- `market_context_high->index_1h` score `-0.7093` n `199` status `ready` deltaP `0.325` edge `0.0019` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.775` n `199` status `ready` deltaP `4.8484` edge `0.0019` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7874` n `199` status `ready` deltaP `-0.7966` edge `-0.0035` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.805` n `189` status `ready` deltaP `9.4569` edge `0.1657` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8486` n `189` status `ready` deltaP `4.9192` edge `0.1293` maxDD `-13.3376`
- `market_context_high->equity_1h` score `-0.8955` n `199` status `ready` deltaP `-1.7813` edge `0.0181` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0883` n `199` status `ready` deltaP `-1.7911` edge `0.0081` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2227` n `189` status `ready` deltaP `10.6942` edge `0.096` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4435` n `189` status `ready` deltaP `-5.1595` edge `0.023` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.7959` n `189` status `ready` deltaP `-6.8646` edge `-0.011` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.1965` n `164` status `ready` deltaP `-1.681` edge `0.0178` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

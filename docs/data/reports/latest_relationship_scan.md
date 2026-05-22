# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T07:22:21.939473+00:00`
- Price records: `672`
- Market context records: `1505`
- Flow alert records: `6242`
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

- `market_context_high->metal_24h` score `13.6026` n `164` status `ready` deltaP `23.5053` edge `1.0769` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1496` n `164` status `ready` deltaP `28.8999` edge `0.9381` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4604` n `164` status `ready` deltaP `27.3289` edge `0.8027` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7496` n `164` status `ready` deltaP `19.9356` edge `0.2882` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6898` n `164` status `ready` deltaP `13.1606` edge `0.3691` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0107` n `190` status `ready` deltaP `5.958` edge `0.1275` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9928` n `164` status `ready` deltaP `19.1311` edge `0.0601` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.254` n `191` status `ready` deltaP `2.7213` edge `0.0072` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2922` n `191` status `ready` deltaP `1.0` edge `0.029` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5139` n `191` status `ready` deltaP `0.0353` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.643` n `190` status `ready` deltaP `9.3325` edge `0.1873` maxDD `-19.5565`
- `market_context_high->metal_1h` score `-0.6744` n `191` status `ready` deltaP `6.3172` edge `0.005` maxDD `-6.3532`
- `market_context_high->crypto_alt_1h` score `-0.6762` n `191` status `ready` deltaP `1.0072` edge `0.0393` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.7197` n `190` status `ready` deltaP `5.3578` edge `0.1429` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.8794` n `191` status `ready` deltaP `-1.9822` edge `-0.0074` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.0563` n `191` status `ready` deltaP `-1.4602` edge `0.01` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.1947` n `190` status `ready` deltaP `10.9691` edge `0.0965` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.2006` n `190` status `ready` deltaP `-3.4724` edge `0.032` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.5616` n `190` status `ready` deltaP `-4.1159` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.3343` n `164` status `ready` deltaP `-1.3338` edge `0.004` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

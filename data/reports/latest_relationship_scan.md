# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T08:22:17.725133+00:00`
- Price records: `672`
- Market context records: `1509`
- Flow alert records: `6255`
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

- `market_context_high->metal_24h` score `13.9817` n `160` status `ready` deltaP `23.3681` edge `1.1094` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1471` n `160` status `ready` deltaP `28.8542` edge `0.9382` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6652` n `160` status `ready` deltaP `27.7431` edge `0.817` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6882` n `160` status `ready` deltaP `19.7222` edge `0.2845` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4639` n `160` status `ready` deltaP `12.9167` edge `0.3519` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0296` n `160` status `ready` deltaP `19.2014` edge `0.0627` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8787` n `186` status `ready` deltaP `5.6124` edge `0.1188` maxDD `-3.6396`
- `market_context_high->equity_1h` score `-0.3101` n `191` status `ready` deltaP `0.6262` edge `0.03` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.333` n `191` status `ready` deltaP `1.9736` edge `0.0056` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5139` n `191` status `ready` deltaP `0.0353` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6942` n `191` status `ready` deltaP `1.0072` edge `0.0378` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.764` n `191` status `ready` deltaP `5.1956` edge `0.001` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7821` n `191` status `ready` deltaP `-0.8606` edge `-0.0024` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.8054` n `186` status `ready` deltaP `8.7153` edge `0.1706` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8285` n `186` status `ready` deltaP `5.0961` edge `0.1307` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0158` n `191` status `ready` deltaP `-1.0863` edge `0.0127` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2168` n `186` status `ready` deltaP `10.7527` edge `0.0961` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.3101` n `186` status `ready` deltaP `-4.242` edge `0.028` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6304` n `186` status `ready` deltaP `-4.8863` edge `-0.0104` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.0454` n `160` status `ready` deltaP `-2.1875` edge `0.1171` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

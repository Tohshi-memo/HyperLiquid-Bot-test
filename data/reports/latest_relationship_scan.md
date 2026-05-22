# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T07:52:17.969846+00:00`
- Price records: `672`
- Market context records: `1507`
- Flow alert records: `6248`
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

- `market_context_high->metal_24h` score `13.7856` n `162` status `ready` deltaP `23.4375` edge `1.0926` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1346` n `162` status `ready` deltaP `28.8773` edge `0.937` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5433` n `162` status `ready` deltaP `27.4498` edge `0.8088` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7184` n `162` status `ready` deltaP `19.8302` edge `0.2863` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5734` n `162` status `ready` deltaP `13.0402` edge `0.3602` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9922` n `162` status `ready` deltaP `18.9429` edge `0.0613` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.955` n `188` status `ready` deltaP `5.7116` edge `0.1245` maxDD `-3.6396`
- `market_context_high->equity_1h` score `-0.3197` n `191` status `ready` deltaP `0.6262` edge `0.0292` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3222` n `191` status `ready` deltaP `1.9736` edge `0.0065` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5342` n `191` status `ready` deltaP `-0.3386` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6978` n `191` status `ready` deltaP `1.0072` edge `0.0375` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.7367` n `191` status `ready` deltaP `5.5695` edge `0.002` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.7439` n `188` status `ready` deltaP `8.9518` edge `0.1769` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.7824` n `188` status `ready` deltaP `5.2316` edge `0.1357` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.8522` n `191` status `ready` deltaP `-1.6083` edge `-0.0064` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.0314` n `191` status `ready` deltaP `-1.0863` edge `0.0107` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2138` n `188` status `ready` deltaP `10.8653` edge `0.0956` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.2526` n `188` status `ready` deltaP `-3.8531` edge `0.0302` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.5821` n `188` status `ready` deltaP `-4.3429` edge `-0.01` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.7068` n `162` status `ready` deltaP `-1.7554` edge `0.0591` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

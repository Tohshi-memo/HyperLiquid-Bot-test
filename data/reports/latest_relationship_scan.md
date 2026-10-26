# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T12:52:27.652268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8396`

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

- `market_context_high->unknown_4h` score `15.5471` n `142` status `ready` deltaP `-0.4015` edge `1.3318` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5858` n `113` status `ready` deltaP `28.4445` edge `0.1525` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.2162` n `142` status `ready` deltaP `10.3744` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0963` n `151` status `ready` deltaP `6.2914` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0208` n `113` status `ready` deltaP `19.6196` edge `0.0291` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.276` n `151` status `ready` deltaP `6.3598` edge `0.0014` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2792` n `151` status `ready` deltaP `2.2951` edge `0.0115` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4276` n `113` status `ready` deltaP `11.4768` edge `-0.0031` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5176` n `142` status `ready` deltaP `5.6488` edge `0.0421` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5775` n `151` status `ready` deltaP `-1.0568` edge `-0.0018` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0141` n `142` status `ready` deltaP `6.7653` edge `-0.0041` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2343` n `151` status `ready` deltaP `1.8053` edge `-0.0122` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.9303` n `142` status `ready` deltaP `-5.9752` edge `-0.0202` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2819` n `151` status `ready` deltaP `-1.4603` edge `-0.0542` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3735` n `151` status `ready` deltaP `-2.8255` edge `-0.037` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.4369` n `113` status `ready` deltaP `-2.0726` edge `-0.0693` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.0552` n `142` status `ready` deltaP `-3.0638` edge `-0.1237` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.2117` n `113` status `ready` deltaP `-2.9914` edge `-0.2189` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4763` n `113` status `ready` deltaP `-18.8191` edge `-0.1459` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.8681` n `142` status `ready` deltaP `-4.9446` edge `-0.2496` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

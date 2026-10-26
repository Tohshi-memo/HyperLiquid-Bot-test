# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T12:37:38.070881+00:00`
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

- `market_context_high->unknown_4h` score `16.0099` n `141` status `ready` deltaP `-0.5113` edge `1.3711` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5866` n `113` status `ready` deltaP `28.4445` edge `0.1526` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.193` n `141` status `ready` deltaP `10.0847` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0831` n `151` status `ready` deltaP `6.1417` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0208` n `113` status `ready` deltaP `19.6196` edge `0.0291` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2732` n `151` status `ready` deltaP `2.2951` edge `0.012` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.2869` n `151` status `ready` deltaP `6.2101` edge `0.001` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.4346` n `113` status `ready` deltaP `11.4768` edge `-0.004` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5202` n `141` status `ready` deltaP `5.5115` edge `0.0428` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5806` n `151` status `ready` deltaP `-1.0568` edge `-0.0022` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0077` n `141` status `ready` deltaP `6.9625` edge `-0.0046` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2491` n `151` status `ready` deltaP `1.8053` edge `-0.0141` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.9607` n `141` status `ready` deltaP `-6.3797` edge `-0.0214` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2936` n `151` status `ready` deltaP `-1.4603` edge `-0.0557` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3914` n `151` status `ready` deltaP `-2.8255` edge `-0.0393` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.4603` n `113` status `ready` deltaP `-2.0726` edge `-0.0723` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.121` n `141` status `ready` deltaP `-3.4434` edge `-0.1296` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.2476` n `113` status `ready` deltaP `-2.9914` edge `-0.2235` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.477` n `113` status `ready` deltaP `-18.8191` edge `-0.146` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.9661` n `141` status `ready` deltaP `-5.3591` edge `-0.2594` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

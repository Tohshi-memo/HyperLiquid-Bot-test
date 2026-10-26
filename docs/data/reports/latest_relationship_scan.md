# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T11:37:28.403793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `17.8586` n `137` status `ready` deltaP `-0.9669` edge `1.5282` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5912` n `113` status `ready` deltaP `28.4445` edge `0.1532` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.0909` n `137` status `ready` deltaP `8.8837` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0662` n `149` status `ready` deltaP `6.3758` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0404` n `113` status `ready` deltaP `19.9668` edge `0.0293` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2966` n `149` status `ready` deltaP `1.9722` edge `0.0122` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3296` n `149` status `ready` deltaP `5.5701` edge `-0.0002` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.4611` n `113` status `ready` deltaP `11.4768` edge `-0.0074` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5387` n `137` status `ready` deltaP `4.9203` edge `0.0452` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6315` n `149` status `ready` deltaP `-1.7502` edge `-0.0041` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.1161` n `137` status `ready` deltaP `5.4923` edge `-0.0087` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3405` n `149` status `ready` deltaP `1.1564` edge `-0.0215` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1001` n `137` status `ready` deltaP `-8.057` edge `-0.0281` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4056` n `149` status `ready` deltaP `-2.1893` edge `-0.0652` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.5034` n `149` status `ready` deltaP `-3.5989` edge `-0.0485` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.5726` n `113` status `ready` deltaP `-2.0726` edge `-0.0867` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.4821` n `137` status `ready` deltaP `-5.0172` edge `-0.1654` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.3942` n `113` status `ready` deltaP `-2.9914` edge `-0.2423` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4794` n `113` status `ready` deltaP `-18.8191` edge `-0.1463` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-8.4112` n `137` status `ready` deltaP `-7.0778` edge `-0.305` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

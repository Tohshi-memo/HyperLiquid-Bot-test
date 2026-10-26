# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T10:52:26.565032+00:00`
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

- `market_context_high->unknown_4h` score `18.7011` n `134` status `ready` deltaP `-1.3264` edge `1.6008` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5928` n `113` status `ready` deltaP `28.4445` edge `0.1534` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.0638` n `146` status `ready` deltaP `6.3141` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.051` n `113` status `ready` deltaP `20.1404` edge `0.0295` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0103` n `134` status `ready` deltaP `7.9359` edge `0.0078` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.2759` n `146` status `ready` deltaP `6.4822` edge `0.0006` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3263` n `146` status `ready` deltaP `1.6918` edge `0.0116` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5018` n `113` status `ready` deltaP `11.1296` edge `-0.0103` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.566` n `134` status `ready` deltaP `4.4298` edge `0.0462` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6271` n `146` status `ready` deltaP `-1.7554` edge `-0.0035` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.1983` n `134` status `ready` deltaP `4.332` edge `-0.0115` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3086` n `146` status `ready` deltaP `1.7554` edge `-0.0214` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1932` n `134` status `ready` deltaP `-9.3807` edge `-0.0312` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3552` n `146` status `ready` deltaP `-1.5647` edge `-0.0629` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4698` n `146` status `ready` deltaP `-3.0432` edge `-0.0479` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6561` n `113` status `ready` deltaP `-2.0726` edge `-0.0974` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.7159` n `134` status `ready` deltaP `-6.2591` edge `-0.1871` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4848` n `113` status `ready` deltaP `-18.8191` edge `-0.147` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.5523` n `113` status `ready` deltaP `-3.5122` edge `-0.2591` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.5928` n `134` status `ready` deltaP `-7.8403` edge `-0.3232` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

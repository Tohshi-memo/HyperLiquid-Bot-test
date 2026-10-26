# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T02:07:33.366533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5070`

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

- `market_context_high->unknown_4h` score `29.8011` n `113` status `ready` deltaP `-1.2061` edge `2.525` maxDD `-1.016`
- `market_context_high->fx_24h` score `-0.0069` n `95` status `ready` deltaP `19.3421` edge `0.0274` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.0807` n `95` status `ready` deltaP `19.5577` edge `0.1263` maxDD `-7.3625`
- `market_context_high->fx_1h` score `-0.0918` n `113` status `ready` deltaP `3.1106` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1144` n `113` status `ready` deltaP `6.3917` edge `0.0077` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3876` n `113` status `ready` deltaP `0.8651` edge `0.012` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6143` n `113` status `ready` deltaP `4.9335` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.637` n `113` status `ready` deltaP `0.0485` edge `0.0409` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6409` n `113` status `ready` deltaP `-1.7368` edge `-0.0054` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7187` n `95` status `ready` deltaP `11.9975` edge `-0.0439` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2514` n `113` status `ready` deltaP `3.9955` edge `-0.029` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-1.4309` n `95` status `ready` deltaP `2.4799` edge `0.014` maxDD `-8.3151`
- `market_context_high->metal_4h` score `-2.012` n `113` status `ready` deltaP `3.5466` edge `-0.0203` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0888` n `113` status `ready` deltaP `-0.9618` edge `-0.0636` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7876` n `113` status `ready` deltaP `-0.2398` edge `-0.0867` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-4.0643` n `95` status `ready` deltaP `-12.7887` edge `-0.0886` maxDD `-13.1096`
- `market_context_high->equity_24h` score `-7.323` n `95` status `ready` deltaP `-0.8517` edge `-0.4048` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-9.3315` n `95` status `ready` deltaP `-8.4375` edge `-0.348` maxDD `-54.0339`
- `market_context_high->crypto_major_4h` score `-10.034` n `113` status `ready` deltaP `-12.7428` edge `-0.2514` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

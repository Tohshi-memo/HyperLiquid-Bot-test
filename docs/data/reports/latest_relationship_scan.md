# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T19:52:28.314408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.7506` n `50` status `ready` deltaP `14.5581` edge `4.4655` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.3594` n `50` status `ready` deltaP `45.2201` edge `2.5226` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.1431` n `62` status `ready` deltaP `22.2463` edge `0.7945` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `6.7346` n `50` status `ready` deltaP `24.3813` edge `0.448` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.0367` n `50` status `ready` deltaP `30.1005` edge `0.3952` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3638` n `50` status `ready` deltaP `43.4073` edge `0.0785` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `4.0594` n `120` status `ready` deltaP `7.8914` edge `0.3589` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.5089` n `71` status `ready` deltaP `9.5556` edge `0.2644` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `3.3185` n `62` status `ready` deltaP `40.5144` edge `0.0286` maxDD `-0.1059`
- `market_context_high->metal_24h` score `3.181` n `120` status `ready` deltaP `28.7406` edge `0.1754` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.3842` n `50` status `ready` deltaP `26.9948` edge `0.0338` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3127` n `120` status `ready` deltaP `17.7033` edge `0.1154` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9215` n `120` status `ready` deltaP `9.3913` edge `0.0592` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5818` n `71` status `ready` deltaP `12.2101` edge `0.0058` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3829` n `71` status `ready` deltaP `11.6113` edge `0.0037` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0636` n `120` status `ready` deltaP `13.1504` edge `0.0122` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.4044` n `120` status `ready` deltaP `3.3134` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_4h` score `-0.4458` n `62` status `ready` deltaP `2.4636` edge `-0.0182` maxDD `-1.4304`
- `news_risk_high->index_1h` score `-0.4678` n `71` status `ready` deltaP `-1.031` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.6588` n `71` status `ready` deltaP `-0.1054` edge `-0.0262` maxDD `-2.605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

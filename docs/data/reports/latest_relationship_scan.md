# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T22:37:24.975139+00:00`
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

- `news_risk_high->unknown_24h` score `55.6856` n `50` status `ready` deltaP `16.4645` edge `4.5307` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4075` n `50` status `ready` deltaP `46.6066` edge `2.6007` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `8.8301` n `71` status `ready` deltaP `17.7387` edge `0.6486` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `8.5383` n `50` status `ready` deltaP `26.2877` edge `0.5856` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.4591` n `50` status `ready` deltaP `30.1005` edge `0.4304` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `4.9943` n `120` status `ready` deltaP `9.7978` edge `0.4241` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4274` n `50` status `ready` deltaP `43.4073` edge `0.0838` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.5113` n `71` status `ready` deltaP `9.1064` edge `0.2676` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2446` n `120` status `ready` deltaP `28.7406` edge `0.1807` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4178` n `50` status `ready` deltaP `26.9948` edge `0.0366` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2727` n `120` status `ready` deltaP `17.3984` edge `0.1141` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1176` n `71` status `ready` deltaP `31.3917` edge `0.0221` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9239` n `120` status `ready` deltaP `8.9421` edge `0.0624` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5818` n `71` status `ready` deltaP `12.2101` edge `0.0058` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3657` n `71` status `ready` deltaP `11.3119` edge `0.0035` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0871` n `120` status `ready` deltaP `13.3028` edge `0.0142` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.4044` n `120` status `ready` deltaP `3.3134` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4592` n `71` status `ready` deltaP `-0.8813` edge `-0.0096` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.6931` n `71` status `ready` deltaP `-0.7042` edge `-0.0266` maxDD `-2.605`
- `news_risk_high->index_4h` score `-0.729` n `71` status `ready` deltaP `-1.3505` edge `-0.0203` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T02:07:31.152683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9166`

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

- `news_risk_high->crypto_major_24h` score `24.8921` n `98` status `ready` deltaP `12.7906` edge `2.6749` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2251` n `98` status `ready` deltaP `15.0935` edge `2.0729` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.7506` n `101` status `ready` deltaP `20.7483` edge `0.3785` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8617` n `101` status `ready` deltaP `20.4434` edge `0.3113` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8469` n `101` status `ready` deltaP `16.8302` edge `0.1716` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.106` n `101` status `ready` deltaP `18.3272` edge `0.1056` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.1111` n `58` status `ready` deltaP `8.4039` edge `0.0619` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `1.0275` n `98` status `ready` deltaP `22.4277` edge `0.1128` maxDD `-3.4467`
- `market_context_high->index_1h` score `0.9448` n `58` status `ready` deltaP `13.2717` edge `0.0158` maxDD `-0.0435`
- `market_context_high->fx_4h` score `0.9172` n `46` status `ready` deltaP `14.2298` edge `0.0098` maxDD `-0.2586`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.5024` n `101` status `ready` deltaP `16.0317` edge `0.0404` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3319` n `58` status `ready` deltaP `8.6259` edge `0.0058` maxDD `-0.1854`
- `market_context_high->index_4h` score `0.1901` n `46` status `ready` deltaP `12.5928` edge `0.0041` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.1445` n `101` status `ready` deltaP `8.0309` edge `0.0221` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.122` n `98` status `ready` deltaP `14.8349` edge `0.0522` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.0363` n `101` status `ready` deltaP `4.0167` edge `0.0168` maxDD `-0.9112`
- `market_context_high->metal_4h` score `-0.0464` n `46` status `ready` deltaP `1.869` edge `0.0233` maxDD `-0.5038`
- `news_risk_high->metal_24h` score `-0.1501` n `98` status `ready` deltaP `12.2059` edge `-0.0162` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

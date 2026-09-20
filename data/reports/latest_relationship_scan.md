# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T22:22:31.007692+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.5297` n `98` status `ready` deltaP `12.7906` edge `2.6447` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2743` n `98` status `ready` deltaP `15.0935` edge `2.077` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.5668` n `101` status `ready` deltaP `20.5958` edge `0.3642` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7177` n `101` status `ready` deltaP `20.4434` edge `0.2993` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.727` n `101` status `ready` deltaP `16.3811` edge `0.1646` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1071` n `101` status `ready` deltaP `18.4769` edge `0.1047` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `1.8009` n `44` status `ready` deltaP `31.8182` edge `0.0415` maxDD `-0.486`
- `market_context_high->fx_1h` score `1.0177` n `51` status `ready` deltaP `14.4359` edge `0.0065` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9971` n `98` status `ready` deltaP `22.4277` edge `0.1089` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6353` n `101` status `ready` deltaP `14.7477` edge `0.0148` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.624` n `101` status `ready` deltaP `17.2512` edge `0.0424` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.4147` n `44` status `ready` deltaP `11.6408` edge `0.0038` maxDD `-0.2586`
- `news_risk_high->equity_24h` score `0.3801` n `98` status `ready` deltaP `16.0501` edge `0.0656` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2585` n `51` status `ready` deltaP `6.2639` edge `0.0121` maxDD `-0.2519`
- `market_context_high->commodity_1h` score `0.2552` n `51` status `ready` deltaP `7.9253` edge `0.0101` maxDD `-0.4171`
- `news_risk_high->fx_4h` score `0.2407` n `101` status `ready` deltaP `9.098` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.1477` n `101` status `ready` deltaP `4.7652` edge `0.0211` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.0636` n `98` status `ready` deltaP `14.6365` edge `-0.005` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2783` n `101` status `ready` deltaP `2.244` edge `0.0062` maxDD `-0.2147`
- `market_context_high->index_1h` score `-0.358` n `51` status `ready` deltaP `-2.178` edge `-0.0003` maxDD `-0.4865`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

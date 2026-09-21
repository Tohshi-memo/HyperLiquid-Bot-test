# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T01:52:31.103152+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.8777` n `98` status `ready` deltaP `12.7906` edge `2.6737` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2251` n `98` status `ready` deltaP `15.0935` edge `2.0729` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.7096` n `101` status `ready` deltaP `20.5958` edge `0.3761` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8437` n `101` status `ready` deltaP `20.4434` edge `0.3098` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8013` n `101` status `ready` deltaP `16.6805` edge `0.1688` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0616` n `101` status `ready` deltaP `18.1775` edge `0.1029` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.2499` n `57` status `ready` deltaP `9.3734` edge `0.067` maxDD `-0.36`
- `market_context_high->fx_4h` score `1.0505` n `45` status `ready` deltaP `15.7757` edge `0.0106` maxDD `-0.2586`
- `market_context_high->index_1h` score `1.044` n `57` status `ready` deltaP `14.4212` edge `0.0164` maxDD `-0.0435`
- `news_risk_high->commodity_24h` score `1.0099` n `98` status `ready` deltaP `22.2541` edge `0.1117` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.517` n `101` status `ready` deltaP `16.1842` edge `0.0406` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.4516` n `57` status `ready` deltaP `7.2959` edge `0.0198` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.4106` n `57` status `ready` deltaP `9.5651` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->equity_24h` score `0.1491` n `98` status `ready` deltaP `15.0085` edge `0.0533` maxDD `-4.941`
- `market_context_high->index_4h` score `0.1482` n `45` status `ready` deltaP `12.1172` edge `0.0019` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.1445` n `101` status `ready` deltaP `8.0309` edge `0.0221` maxDD `-0.421`
- `market_context_high->crypto_major_1h` score `0.0833` n `57` status `ready` deltaP `-0.7038` edge `0.0835` maxDD `-2.7494`
- `news_risk_high->equity_1h` score `0.0195` n `101` status `ready` deltaP `3.867` edge `0.0164` maxDD `-0.9112`
- `market_context_high->metal_4h` score `-0.1229` n `45` status `ready` deltaP `0.9587` edge `0.023` maxDD `-0.5038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

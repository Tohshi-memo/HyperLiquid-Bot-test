# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T23:29:55.588586+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.7109` n `98` status `ready` deltaP `12.7906` edge `2.6598` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3019` n `98` status `ready` deltaP `15.0935` edge `2.0793` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6268` n `101` status `ready` deltaP `20.5958` edge `0.3692` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7873` n `101` status `ready` deltaP `20.4434` edge `0.3051` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.745` n `101` status `ready` deltaP `16.5308` edge `0.1651` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0556` n `101` status `ready` deltaP `18.1775` edge `0.1024` maxDD `-2.8494`
- `market_context_high->fx_1h` score `1.3579` n `51` status `ready` deltaP `18.058` edge `0.0107` maxDD `-0.1012`
- `market_context_high->commodity_4h` score `1.1947` n `43` status `ready` deltaP `27.2015` edge `0.0187` maxDD `-1.4167`
- `news_risk_high->commodity_24h` score `0.9834` n `98` status `ready` deltaP `22.2541` edge `0.1083` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6106` n `101` status `ready` deltaP `17.0988` edge `0.0423` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.3946` n `43` status `ready` deltaP `10.848` edge `0.0065` maxDD `-0.2586`
- `news_risk_high->equity_24h` score `0.2789` n `98` status `ready` deltaP `15.3557` edge `0.0618` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2371` n `101` status `ready` deltaP `9.098` edge `0.0227` maxDD `-0.421`
- `market_context_high->index_1h` score `0.2191` n `51` status `ready` deltaP `5.0663` edge `0.011` maxDD `-0.1211`
- `market_context_high->metal_1h` score `0.1448` n `51` status `ready` deltaP `4.4529` edge `0.0147` maxDD `-0.2519`
- `news_risk_high->equity_1h` score `0.0806` n `101` status `ready` deltaP `4.3161` edge `0.0185` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.0072` n `98` status `ready` deltaP `13.9421` edge `-0.0076` maxDD `-2.4203`
- `market_context_high->equity_1h` score `-0.0285` n `51` status `ready` deltaP `1.7729` edge `0.0171` maxDD `-0.9397`
- `market_context_high->index_4h` score `-0.1375` n `43` status `ready` deltaP `8.7529` edge `-0.0123` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T01:37:31.783250+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.8573` n `98` status `ready` deltaP `12.7906` edge `2.672` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2275` n `98` status `ready` deltaP `15.0935` edge `2.0731` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.694` n `101` status `ready` deltaP `20.5958` edge `0.3748` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8365` n `101` status `ready` deltaP `20.4434` edge `0.3092` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7522` n `101` status `ready` deltaP `16.5308` edge `0.1657` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0112` n `101` status `ready` deltaP `18.0278` edge `0.0997` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.3522` n `56` status `ready` deltaP `10.3828` edge `0.0688` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `1.0029` n `98` status `ready` deltaP `22.2541` edge `0.1108` maxDD `-3.4467`
- `market_context_high->fx_4h` score `1.0029` n `44` status `ready` deltaP `15.2716` edge `0.01` maxDD `-0.2586`
- `market_context_high->index_1h` score `0.9963` n `56` status `ready` deltaP `13.8259` edge `0.0164` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.646` n `101` status `ready` deltaP `14.8974` edge `0.0147` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.534` n `101` status `ready` deltaP `16.3366` edge `0.041` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3914` n `56` status `ready` deltaP `6.6938` edge `0.0188` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3592` n `56` status `ready` deltaP `8.9072` edge `0.0062` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3386` n `56` status `ready` deltaP `0.1176` edge `0.0993` maxDD `-2.7494`
- `news_risk_high->equity_24h` score `0.1611` n `98` status `ready` deltaP `15.0085` edge `0.0543` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.1579` n `101` status `ready` deltaP `8.1834` edge `0.0222` maxDD `-0.421`
- `market_context_high->index_4h` score `0.1009` n `44` status `ready` deltaP `11.613` edge `-0.0008` maxDD `-1.0949`
- `news_risk_high->equity_1h` score `0.0003` n `101` status `ready` deltaP `3.7173` edge `0.0158` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `-0.118` n `98` status `ready` deltaP `12.5532` edge `-0.0144` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

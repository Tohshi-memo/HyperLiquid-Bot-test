# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T00:52:26.316361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9142`

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

- `news_risk_high->crypto_major_24h` score `24.8393` n `98` status `ready` deltaP `12.7906` edge `2.6705` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2731` n `98` status `ready` deltaP `15.0935` edge `2.0769` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6928` n `101` status `ready` deltaP `20.5958` edge `0.3747` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8497` n `101` status `ready` deltaP `20.4434` edge `0.3103` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.685` n `101` status `ready` deltaP `16.3811` edge `0.1611` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9644` n `101` status `ready` deltaP `17.8781` edge `0.0968` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.0666` n `53` status `ready` deltaP `8.4623` edge `0.0578` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `0.9896` n `98` status `ready` deltaP `22.2541` edge `0.1091` maxDD `-3.4467`
- `market_context_high->fx_4h` score `0.9246` n `42` status `ready` deltaP `14.322` edge `0.0098` maxDD `-0.2586`
- `market_context_high->index_1h` score `0.8355` n `53` status `ready` deltaP `11.9054` edge `0.0158` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.646` n `101` status `ready` deltaP `14.8974` edge `0.0147` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.5893` n `53` status `ready` deltaP `10.2587` edge `0.0074` maxDD `-0.1347`
- `news_risk_high->metal_4h` score `0.5534` n `101` status `ready` deltaP `16.489` edge `0.0416` maxDD `-2.0994`
- `market_context_high->commodity_4h` score `0.4031` n `42` status `ready` deltaP `20.1147` edge `-0.0095` maxDD `-2.4997`
- `news_risk_high->fx_4h` score `0.1969` n `101` status `ready` deltaP `8.6407` edge `0.0224` maxDD `-0.421`
- `market_context_high->crypto_major_1h` score `0.189` n `53` status `ready` deltaP `-0.6722` edge `0.0921` maxDD `-2.7494`
- `news_risk_high->equity_24h` score `0.1863` n `98` status `ready` deltaP `15.0085` edge `0.0564` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.1349` n `53` status `ready` deltaP `4.2679` edge `0.0136` maxDD `-0.1314`
- `news_risk_high->equity_1h` score `-0.0129` n `101` status `ready` deltaP `3.7173` edge `0.0147` maxDD `-0.9112`
- `market_context_high->index_4h` score `-0.0191` n `42` status `ready` deltaP `10.2061` edge `-0.0068` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

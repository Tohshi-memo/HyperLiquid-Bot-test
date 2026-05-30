# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T16:37:23.250688+00:00`
- Price records: `672`
- Market context records: `2368`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.8329` n `43` status `ready` deltaP `50.0363` edge `1.5447` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.7354` n `43` status `ready` deltaP `47.3272` edge `1.2064` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0631` n `43` status `ready` deltaP `29.7925` edge `1.0881` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7398` n `43` status `ready` deltaP `19.7674` edge `0.9046` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.2017` n `140` status `ready` deltaP `20.0` edge `0.9394` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.9972` n `43` status `ready` deltaP `27.8141` edge `0.5036` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9344` n `140` status `ready` deltaP `23.8939` edge `0.3764` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.7937` n `149` status `ready` deltaP `24.3166` edge `0.5017` maxDD `-10.1468`
- `news_risk_high->index_24h` score `5.2156` n `43` status `ready` deltaP `13.0976` edge `0.3892` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `5.0935` n `149` status `ready` deltaP `19.5235` edge `0.5622` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.0756` n `149` status `ready` deltaP `21.0796` edge `0.3434` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7638` n `43` status `ready` deltaP `32.0051` edge `0.3363` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.438` n `43` status `ready` deltaP `36.5351` edge `0.0614` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9467` n `43` status `ready` deltaP `24.9929` edge `0.014` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.7879` n `149` status `ready` deltaP `19.2564` edge `0.1032` maxDD `-2.2732`
- `market_context_high->crypto_major_1h` score `1.6909` n `156` status `ready` deltaP `14.3137` edge `0.1649` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.6697` n `140` status `ready` deltaP `12.5992` edge `0.1069` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `1.4623` n `156` status `ready` deltaP `11.0241` edge `0.1671` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.0496` n `140` status `ready` deltaP `19.9752` edge `0.107` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.9386` n `43` status `ready` deltaP `13.4005` edge `0.0612` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

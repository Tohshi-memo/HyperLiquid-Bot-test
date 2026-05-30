# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T12:37:17.749300+00:00`
- Price records: `672`
- Market context records: `2350`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `21.3229` n `43` status `ready` deltaP `50.0363` edge `1.5022` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.0514` n `43` status `ready` deltaP `44.8966` edge `1.1656` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.6479` n `43` status `ready` deltaP `29.7925` edge `1.0535` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.0726` n `43` status `ready` deltaP `19.7674` edge `0.849` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.0581` n `140` status `ready` deltaP `20.0` edge `1.0941` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.6701` n `43` status `ready` deltaP `27.6405` edge `0.4775` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.8873` n `140` status `ready` deltaP `24.4346` edge `0.4522` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.542` n `156` status `ready` deltaP `22.4047` edge `0.6637` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5272` n `156` status `ready` deltaP `25.2502` edge `0.5566` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.6753` n `156` status `ready` deltaP `22.7408` edge `0.3823` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.8278` n `43` status `ready` deltaP `12.7504` edge `0.3592` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0026` n `43` status `ready` deltaP `33.9868` edge `0.3537` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4066` n `43` status `ready` deltaP `36.1879` edge `0.0611` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.787` n `140` status `ready` deltaP `13.6806` edge `0.1928` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.1764` n `140` status `ready` deltaP `19.9752` edge `0.2009` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0645` n `156` status `ready` deltaP `20.3135` edge `0.1192` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0125` n `43` status `ready` deltaP `25.7551` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.6118` n `164` status `ready` deltaP `11.7679` edge `0.1746` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.6045` n `164` status `ready` deltaP `13.4585` edge `0.1634` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1277` n `156` status `ready` deltaP `10.8935` edge `0.1618` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T11:22:17.329100+00:00`
- Price records: `672`
- Market context records: `2452`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.3061` n `43` status `ready` deltaP `43.7863` edge `1.3758` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.1943` n `43` status `ready` deltaP `54.7925` edge `1.2782` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.6935` n `43` status `ready` deltaP `29.7925` edge `1.0573` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.3226` n `43` status `ready` deltaP `16.6424` edge `0.724` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `6.8432` n `43` status `ready` deltaP `22.7794` edge `0.441` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8686` n `109` status `ready` deltaP `21.926` edge `0.3757` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9579` n `43` status `ready` deltaP `8.9309` edge `0.3955` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.652` n `128` status `ready` deltaP `21.7607` edge `0.4236` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.3984` n `128` status `ready` deltaP `21.3796` edge `0.4919` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1831` n `43` status `ready` deltaP `28.6514` edge `0.2842` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1674` n `43` status `ready` deltaP `33.0629` edge `0.062` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.5126` n `109` status `ready` deltaP `12.0126` edge `0.6313` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`
- `market_context_high->unknown_4h` score `2.0455` n `128` status `ready` deltaP `11.1853` edge `0.1712` maxDD `-2.358`
- `news_risk_high->unknown_4h` score `1.6623` n `43` status `ready` deltaP `15.3822` edge `0.1083` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.4023` n `109` status `ready` deltaP `6.9253` edge `0.1113` maxDD `-0.5824`
- `news_risk_high->unknown_1h` score `1.1624` n `43` status `ready` deltaP `20.7457` edge `0.0055` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8824` n `136` status `ready` deltaP `9.3827` edge `0.1304` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.744` n `136` status `ready` deltaP `7.9253` edge `0.1279` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5195` n `43` status `ready` deltaP `8.8184` edge `0.0758` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

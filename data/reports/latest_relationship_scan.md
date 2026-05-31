# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T06:22:17.467694+00:00`
- Price records: `672`
- Market context records: `2430`
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

- `news_risk_high->crypto_alt_24h` score `19.3908` n `43` status `ready` deltaP `43.9599` edge `1.3817` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.7348` n `43` status `ready` deltaP `51.4938` edge `1.2619` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9515` n `43` status `ready` deltaP `29.7925` edge `1.0788` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.9194` n `43` status `ready` deltaP `17.3368` edge `0.7691` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.5073` n `43` status `ready` deltaP `25.0363` edge `0.4813` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7503` n `101` status `ready` deltaP `23.7469` edge `0.3537` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9874` n `43` status `ready` deltaP `9.1045` edge `0.3968` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6153` n `124` status `ready` deltaP `22.2757` edge `0.504` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.587` n `124` status `ready` deltaP `21.2333` edge `0.4217` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.3942` n `43` status `ready` deltaP `35.4934` edge `0.0647` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1715` n `43` status `ready` deltaP `28.8038` edge `0.2817` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7044` n `124` status `ready` deltaP `13.6851` edge `0.1951` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4879` n `101` status `ready` deltaP `13.203` edge `0.145` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.3263` n `101` status `ready` deltaP `9.9456` edge `0.6212` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7747` n `43` status `ready` deltaP `15.9919` edge `0.1136` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2001` n `124` status `ready` deltaP `11.073` edge `0.1456` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1157` n `43` status `ready` deltaP `20.596` edge `0.0026` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0317` n `124` status `ready` deltaP `8.8372` edge `0.1458` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5234` n `43` status `ready` deltaP `8.9681` edge `0.0753` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

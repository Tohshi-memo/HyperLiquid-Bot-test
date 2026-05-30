# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T19:37:18.935733+00:00`
- Price records: `672`
- Market context records: `2381`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.806` n `43` status `ready` deltaP `50.2099` edge `1.5413` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.0778` n `43` status `ready` deltaP `49.2369` edge `1.2222` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2635` n `43` status `ready` deltaP `29.7925` edge `1.1048` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8502` n `43` status `ready` deltaP `19.7674` edge `0.9138` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2793` n `43` status `ready` deltaP `28.1613` edge `0.5248` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.4646` n `129` status `ready` deltaP `17.4419` edge `0.8117` maxDD `-25.1408`
- `news_risk_high->index_24h` score `5.3694` n `43` status `ready` deltaP `13.4448` edge `0.3997` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3625` n `129` status `ready` deltaP `23.5102` edge `0.3313` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.293` n `145` status `ready` deltaP `23.7427` edge `0.4638` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.1095` n `145` status `ready` deltaP `18.6533` edge `0.486` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `3.7899` n `145` status `ready` deltaP `18.2686` edge `0.255` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.6702` n `43` status `ready` deltaP `32.0051` edge `0.3243` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.529` n `43` status `ready` deltaP `37.4031` edge `0.0632` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.0235` n `43` status `ready` deltaP `25.9075` edge `0.0143` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6939` n `152` status `ready` deltaP `14.1113` edge `0.1665` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.4265` n `129` status `ready` deltaP `11.1192` edge `0.0965` maxDD `-1.4737`
- `news_risk_high->unknown_4h` score `1.3332` n `43` status `ready` deltaP `14.1627` edge `0.089` maxDD `-2.7857`
- `market_context_high->index_4h` score `1.2627` n `145` status `ready` deltaP `15.7212` edge `0.083` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.2079` n `152` status `ready` deltaP `9.3287` edge `0.1572` maxDD `-6.1656`
- `news_risk_high->unknown_1h` score `0.9215` n `43` status `ready` deltaP `19.2487` edge `-0.0046` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

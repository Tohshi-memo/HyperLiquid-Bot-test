# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T01:22:20.242248+00:00`
- Price records: `672`
- Market context records: `2409`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.3985` n `43` status `ready` deltaP `46.9113` edge `1.446` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2309` n `43` status `ready` deltaP `49.4105` edge `1.2338` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2311` n `43` status `ready` deltaP `29.7925` edge `1.1021` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9816` n `43` status `ready` deltaP `18.8993` edge `0.8472` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2187` n `43` status `ready` deltaP `27.9877` edge `0.5209` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6011` n `109` status `ready` deltaP `22.5472` edge `0.3576` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3616` n `43` status `ready` deltaP `12.4031` edge `0.406` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8299` n `132` status `ready` deltaP `23.3093` edge `0.4281` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.2129` n `132` status `ready` deltaP `20.9211` edge `0.4795` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6103` n `43` status `ready` deltaP `37.924` edge `0.0665` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2732` n `43` status `ready` deltaP `30.1758` edge `0.2856` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.9863` n `109` status `ready` deltaP `13.3521` edge `0.6831` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4566` n `132` status `ready` deltaP `12.8973` edge `0.1797` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1658` n `43` status `ready` deltaP `27.4319` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7805` n `43` status `ready` deltaP `15.8395` edge `0.1151` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.6582` n `109` status `ready` deltaP `10.3975` edge `0.1166` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.399` n `132` status `ready` deltaP `12.9151` edge `0.1499` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1313` n `43` status `ready` deltaP `20.2966` edge `0.0059` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0084` n `132` status `ready` deltaP `8.8006` edge `0.1441` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.6198` n `132` status `ready` deltaP `12.6801` edge `0.0497` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

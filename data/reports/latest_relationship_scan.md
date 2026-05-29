# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T13:52:22.228833+00:00`
- Price records: `672`
- Market context records: `2250`
- Flow alert records: `8370`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `24.1939` n `43` status `ready` deltaP `54.7238` edge `1.7102` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.2921` n `43` status `ready` deltaP `44.3758` edge `1.1058` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.9108` n `43` status `ready` deltaP `35.348` edge `1.1217` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.6399` n `43` status `ready` deltaP `25.323` edge `1.0259` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `10.3163` n `115` status `ready` deltaP `31.5821` edge `0.6903` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `10.1077` n `133` status `ready` deltaP `29.9239` edge `0.829` maxDD `-10.5615`
- `news_risk_high->unknown_24h` score `9.8798` n `43` status `ready` deltaP `35.6266` edge `0.6084` maxDD `-1.4744`
- `market_context_high->crypto_major_4h` score `9.332` n `133` status `ready` deltaP `35.4403` edge `0.6626` maxDD `-6.6959`
- `market_context_high->crypto_major_24h` score `7.1443` n `115` status `ready` deltaP `19.0339` edge `1.1783` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.277` n `133` status `ready` deltaP `20.0875` edge `0.3668` maxDD `-1.8773`
- `market_context_high->index_4h` score `4.0503` n `133` status `ready` deltaP `31.0793` edge `0.1677` maxDD `-0.3228`
- `news_risk_high->index_24h` score `3.9534` n `43` status `ready` deltaP `13.4448` edge `0.2817` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8432` n `43` status `ready` deltaP `32.7673` edge `0.3414` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6663` n `43` status `ready` deltaP `37.2295` edge `0.0758` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.5637` n `115` status `ready` deltaP `15.2446` edge `0.2471` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.5497` n `115` status `ready` deltaP `22.891` edge `0.2959` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9766` n `43` status `ready` deltaP `2.0309` edge `0.3162` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.8535` n `133` status `ready` deltaP `20.3695` edge `0.2219` maxDD `-4.2589`
- `news_risk_high->fx_4h` score `2.0831` n `43` status `ready` deltaP `26.5173` edge `0.0152` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.8996` n `145` status `ready` deltaP `12.9672` edge `0.1886` maxDD `-6.0065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

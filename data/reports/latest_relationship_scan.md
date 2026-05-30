# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T19:22:18.618590+00:00`
- Price records: `672`
- Market context records: `2380`
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

- `news_risk_high->crypto_alt_24h` score `21.8252` n `43` status `ready` deltaP `50.2099` edge `1.5429` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.0471` n `43` status `ready` deltaP `49.0633` edge `1.2208` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2503` n `43` status `ready` deltaP `29.7925` edge `1.1037` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8514` n `43` status `ready` deltaP `19.7674` edge `0.9139` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2517` n `43` status `ready` deltaP `28.1613` edge `0.5225` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.6323` n `130` status `ready` deltaP `17.6923` edge `0.824` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.4271` n `146` status `ready` deltaP `23.8891` edge `0.474` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.4066` n `130` status `ready` deltaP `23.5817` edge `0.3345` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3598` n `43` status `ready` deltaP `13.4448` edge `0.3989` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.2676` n `146` status `ready` deltaP `18.8753` edge `0.4977` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.0082` n `146` status `ready` deltaP `18.3428` edge `0.2727` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.6905` n `43` status `ready` deltaP `32.0051` edge `0.3269` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.5127` n `43` status `ready` deltaP `37.2295` edge `0.063` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.0113` n `43` status `ready` deltaP `25.7551` edge `0.0143` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6967` n `153` status `ready` deltaP `14.1766` edge `0.1663` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.4528` n `130` status `ready` deltaP `11.2981` edge `0.0975` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.2893` n `146` status `ready` deltaP `15.7388` edge `0.0851` maxDD `-2.2732`
- `news_risk_high->unknown_4h` score `1.249` n `43` status `ready` deltaP `14.0102` edge `0.083` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `1.2117` n `153` status `ready` deltaP `9.437` edge `0.1568` maxDD `-6.1656`
- `news_risk_high->unknown_1h` score `0.9047` n `43` status `ready` deltaP `19.2487` edge `-0.006` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

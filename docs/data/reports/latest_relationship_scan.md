# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T04:07:27.798490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12599`

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

- `market_context_high->unknown_24h` score `16607.3946` n `59` status `ready` deltaP `12.756` edge `1383.8697` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `380.2874` n `82` status `ready` deltaP `-4.6517` edge `31.7638` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.9176` n `82` status `ready` deltaP `38.8042` edge `1.3815` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.9092` n `82` status `ready` deltaP `32.0587` edge `1.3275` maxDD `-2.2369`
- `market_context_high->equity_24h` score `10.7436` n `59` status `ready` deltaP `48.0903` edge `0.5747` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.0106` n `59` status `ready` deltaP `22.0133` edge `0.7702` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.4865` n `82` status `ready` deltaP `17.6025` edge `0.6012` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1928` n `82` status `ready` deltaP `43.1741` edge `0.2459` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8364` n `82` status `ready` deltaP `26.4821` edge `0.2719` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.239` n `59` status `ready` deltaP `42.1875` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `4.0714` n `59` status `ready` deltaP `43.7736` edge `0.0867` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.2526` n `59` status `ready` deltaP `7.2799` edge `0.1036` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.226` n `82` status `ready` deltaP `9.4512` edge `0.0288` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.0669` n `53` status `ready` deltaP `6.7562` edge `0.131` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.0669` n `53` status `ready` deltaP `6.7562` edge `0.131` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.0373` n `64` status `ready` deltaP `3.808` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0373` n `64` status `ready` deltaP `3.808` edge `0.0033` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.1011` n `122` status `ready` deltaP `3.0652` edge `-0.0018` maxDD `-0.5274`
- `risk_on_high->metal_1h` score `-0.1746` n `64` status `ready` deltaP `2.5449` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1746` n `64` status `ready` deltaP `2.5449` edge `0.0015` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

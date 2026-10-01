# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T12:22:30.209265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `324.6591` n `50` status `ready` deltaP `7.5808` edge `27.0093` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.8304` n `50` status `ready` deltaP `6.8598` edge `23.3568` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.481` n `118` status `ready` deltaP `31.4648` edge `1.4346` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.0213` n `50` status `ready` deltaP `30.0903` edge `0.6928` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.0171` n `50` status `ready` deltaP `18.9146` edge `0.529` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.2554` n `118` status `ready` deltaP `21.6661` edge `0.5284` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.462` n `123` status `ready` deltaP `29.7764` edge `0.2222` maxDD `-1.2436`
- `market_context_high->crypto_alt_4h` score `4.4061` n `50` status `ready` deltaP `14.9695` edge `0.3967` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.6216` n `50` status `ready` deltaP `16.7847` edge `0.5386` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.518` n `118` status `ready` deltaP `20.9717` edge `0.6266` maxDD `-15.8971`
- `market_context_high->fx_4h` score `2.9996` n `50` status `ready` deltaP `33.9085` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_alt_24h` score `2.8737` n `50` status `ready` deltaP `7.1597` edge `0.3627` maxDD `-11.6768`
- `market_context_high->crypto_major_1h` score `2.8643` n `50` status `ready` deltaP `14.4491` edge `0.1874` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.6172` n `50` status `ready` deltaP `12.4072` edge `0.2017` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4679` n `118` status `ready` deltaP `23.8906` edge `0.0942` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2618` n `118` status `ready` deltaP `26.6213` edge `0.2399` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `1.9161` n `123` status `ready` deltaP `10.0102` edge `0.2936` maxDD `-10.7193`
- `market_context_high->fx_1h` score `1.4316` n `50` status `ready` deltaP `20.1916` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.9272` n `131` status `ready` deltaP `8.7032` edge `0.0729` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7041` n `50` status `ready` deltaP `12.5347` edge `0.0638` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

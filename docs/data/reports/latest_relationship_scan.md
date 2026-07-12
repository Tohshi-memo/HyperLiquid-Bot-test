# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T20:07:28.216984+00:00`
- Price records: `672`
- Market context records: `6535`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.7092` n `32` status `ready` deltaP `37.0776` edge `0.91` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6048` n `32` status `ready` deltaP `54.4194` edge `0.1876` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3151` n `144` status `ready` deltaP `11.8934` edge `0.777` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.9976` n `32` status `ready` deltaP `21.7775` edge `0.5735` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6999` n `38` status `ready` deltaP `39.1688` edge `0.0518` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.0519` n `194` status `ready` deltaP `-6.4356` edge `0.304` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `1.9549` n `32` status `ready` deltaP `21.9833` edge `0.0369` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7915` n `38` status `ready` deltaP `22.463` edge `0.0176` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.5359` n `144` status `ready` deltaP `13.9972` edge `0.2215` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7165` n `182` status `ready` deltaP `14.7815` edge `0.0288` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5901` n `38` status `ready` deltaP `5.3498` edge `0.0937` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3882` n `182` status `ready` deltaP `10.4429` edge `0.1181` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0937` n `38` status `ready` deltaP `1.7334` edge `0.0514` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.1938` n `32` status `ready` deltaP `8.4164` edge `0.0062` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3515` n `182` status `ready` deltaP `9.798` edge `0.0595` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.358` n `182` status `ready` deltaP `13.4029` edge `0.0938` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4124` n `194` status `ready` deltaP `-0.0818` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.464` n `194` status `ready` deltaP `1.5788` edge `-0.0017` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5458` n `194` status `ready` deltaP `6.3183` edge `0.0192` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5494` n `194` status `ready` deltaP `6.218` edge `0.0147` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

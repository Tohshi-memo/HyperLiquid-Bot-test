# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T12:22:29.016027+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_1h` score `403.4098` n `51` status `ready` deltaP `7.9194` edge `33.5696` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `323.7801` n `43` status `ready` deltaP `8.2317` edge `26.9268` maxDD `0.0`
- `news_risk_high->unknown_24h` score `113.2096` n `135` status `ready` deltaP `1.9097` edge `9.4214` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2395` n `135` status `ready` deltaP `26.9907` edge `1.1943` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `6.9503` n `135` status `ready` deltaP `25.6019` edge `0.6434` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.4401` n `135` status `ready` deltaP `23.9931` edge `0.6921` maxDD `-15.8971`
- `market_context_high->crypto_major_4h` score `4.3925` n `43` status `ready` deltaP `13.8578` edge `0.344` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4218` n `135` status `ready` deltaP `31.794` edge `0.121` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.3331` n `43` status `ready` deltaP `37.2625` edge `0.0424` maxDD `-0.0449`
- `news_risk_high->metal_24h` score `2.9655` n `135` status `ready` deltaP `23.4491` edge `0.2182` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.5897` n `135` status `ready` deltaP `27.7992` edge `0.1906` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.3298` n `51` status `ready` deltaP `14.8409` edge `0.1562` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.0766` n `51` status `ready` deltaP `12.9095` edge `0.1533` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.4789` n `51` status `ready` deltaP `20.7086` edge `0.0116` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `0.9795` n `43` status `ready` deltaP `9.7809` edge `0.1897` maxDD `-7.6792`
- `news_risk_high->equity_1h` score `0.9187` n `135` status `ready` deltaP `9.7006` edge `0.0742` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.8716` n `135` status `ready` deltaP `8.2036` edge `0.109` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.6567` n `135` status `ready` deltaP `8.3683` edge `0.2649` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.4933` n `135` status `ready` deltaP `8.8179` edge `0.0111` maxDD `-0.302`
- `market_context_high->commodity_1h` score `-0.0103` n `51` status `ready` deltaP `9.1229` edge `-0.0075` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

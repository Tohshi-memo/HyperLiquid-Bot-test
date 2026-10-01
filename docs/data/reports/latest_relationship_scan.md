# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T22:07:30.694091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.0629` n `50` status `ready` deltaP `8.9281` edge `28.1173` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.7646` n `50` status `ready` deltaP `7.0122` edge `23.8503` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3862` n `94` status `ready` deltaP `36.2404` edge `1.4782` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.4383` n `50` status `ready` deltaP `34.2569` edge `0.7831` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2691` n `50` status `ready` deltaP `18.9146` edge `0.55` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.9339` n `50` status `ready` deltaP `12.3681` edge `0.583` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0608` n `50` status `ready` deltaP `16.4939` edge `0.4411` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.599` n `94` status `ready` deltaP `18.2143` edge `0.5772` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7654` n `50` status `ready` deltaP `19.0417` edge `0.542` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.1606` n `107` status `ready` deltaP `26.8478` edge `0.154` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.06` n `50` status `ready` deltaP `34.2134` edge `0.0404` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0359` n `50` status `ready` deltaP `14.7485` edge `0.1997` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9829` n `50` status `ready` deltaP `13.9042` edge `0.2222` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.5633` n `94` status `ready` deltaP `18.063` edge `0.4431` maxDD `-9.4579`
- `news_risk_high->index_24h` score `1.9677` n `94` status `ready` deltaP `21.3874` edge `0.0692` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `1.9519` n `94` status `ready` deltaP `22.2666` edge `0.2292` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4771` n `50` status `ready` deltaP `20.6407` edge `0.0119` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.3255` n `94` status `ready` deltaP `23.0312` edge `0.1288` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9089` n `50` status `ready` deltaP `14.7917` edge `0.075` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5948` n `107` status `ready` deltaP `8.2391` edge `0.0483` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

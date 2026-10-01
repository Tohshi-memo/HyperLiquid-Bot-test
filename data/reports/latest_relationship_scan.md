# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T10:52:30.795923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6886`

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

- `market_context_high->unknown_1h` score `324.3699` n `50` status `ready` deltaP `7.2814` edge `26.9872` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.1064` n `50` status `ready` deltaP `6.8598` edge `23.3798` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.4292` n `123` status `ready` deltaP `30.4921` edge `1.5201` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.5857` n `50` status `ready` deltaP `30.0903` edge `0.6565` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.8549` n `50` status `ready` deltaP `18.7622` edge `0.5165` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.982` n `123` status `ready` deltaP `22.7684` edge `0.5816` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.4954` n `123` status `ready` deltaP `29.6239` edge `0.226` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.2836` n `123` status `ready` deltaP `22.074` edge `0.7174` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.9525` n `50` status `ready` deltaP `14.0549` edge `0.365` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5225` n `50` status `ready` deltaP `16.7847` edge `0.5259` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.325` n `123` status `ready` deltaP `13.1606` edge `0.39` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.9582` n `50` status `ready` deltaP `33.4512` edge `0.037` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8847` n `50` status `ready` deltaP `14.5988` edge `0.1881` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.6255` n `50` status `ready` deltaP `12.7066` edge `0.2004` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.6125` n `123` status `ready` deltaP `24.6485` edge `0.1012` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.33` n `123` status `ready` deltaP `27.3035` edge `0.2441` maxDD `-2.192`
- `market_context_high->crypto_alt_24h` score `2.0139` n `50` status `ready` deltaP `6.1181` edge `0.298` maxDD `-11.6768`
- `market_context_high->fx_1h` score `1.4711` n `50` status `ready` deltaP `20.6407` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7311` n `134` status `ready` deltaP `7.3018` edge `0.0659` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.7208` n `50` status `ready` deltaP `16.8611` edge `0.0818` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

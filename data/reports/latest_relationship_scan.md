# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T06:37:34.595681+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6722`

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

- `market_context_high->unknown_1h` score `324.7432` n `50` status `ready` deltaP `7.1317` edge `27.0193` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0824` n `50` status `ready` deltaP `6.8598` edge `23.3778` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3384` n `126` status `ready` deltaP `29.1419` edge `1.4382` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `7.8875` n `35` status `ready` deltaP `27.9167` edge `0.6128` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.6511` n `50` status `ready` deltaP `18.0` edge `0.5046` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.8869` n `126` status `ready` deltaP `23.2143` edge `0.5707` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `4.1625` n `126` status `ready` deltaP `22.5199` edge `0.6989` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `4.0896` n `126` status `ready` deltaP `27.3568` edge `0.2073` maxDD `-1.2436`
- `market_context_high->crypto_alt_24h` score `3.5924` n `35` status `ready` deltaP `10.7292` edge `0.3988` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `3.5147` n `50` status `ready` deltaP `13.2927` edge `0.3336` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9339` n `50` status `ready` deltaP `14.7485` edge `0.1912` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9083` n `50` status `ready` deltaP `32.8415` edge `0.0369` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.6003` n `50` status `ready` deltaP `12.5569` edge `0.1993` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5924` n `126` status `ready` deltaP `24.7272` edge `0.099` maxDD `-0.4916`
- `news_risk_high->crypto_alt_4h` score `2.5922` n `126` status `ready` deltaP `11.5467` edge `0.3397` maxDD `-10.7193`
- `news_risk_high->metal_24h` score `2.0905` n `126` status `ready` deltaP `24.6776` edge `0.2309` maxDD `-2.192`
- `market_context_high->equity_24h` score `1.9996` n `35` status `ready` deltaP `5.754` edge `0.4042` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.4424` n `50` status `ready` deltaP `20.3413` edge `0.011` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.806` n `126` status `ready` deltaP `7.7132` edge `0.0694` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.6571` n `126` status `ready` deltaP `7.668` edge `0.0947` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

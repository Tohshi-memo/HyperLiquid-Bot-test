# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T05:37:34.763706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6754`

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

- `market_context_high->unknown_1h` score `324.6028` n `50` status `ready` deltaP `6.8323` edge `27.0096` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9492` n `50` status `ready` deltaP `6.8598` edge `23.3667` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2511` n `130` status `ready` deltaP `29.1907` edge `1.4306` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8787` n `50` status `ready` deltaP `18.6098` edge `0.5195` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4615` n `130` status `ready` deltaP `23.3013` edge `0.6985` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.2278` n `130` status `ready` deltaP `23.9957` edge `0.5939` maxDD `-9.4579`
- `market_context_high->crypto_major_24h` score `4.084` n `31` status `ready` deltaP `25.3361` edge `0.4963` maxDD `-9.3299`
- `market_context_high->crypto_alt_4h` score `3.7843` n `50` status `ready` deltaP `13.9024` edge `0.352` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `3.3098` n `130` status `ready` deltaP `25.4268` edge `0.1881` maxDD `-3.8771`
- `market_context_high->crypto_major_1h` score `2.9435` n `50` status `ready` deltaP `14.8982` edge `0.191` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8559` n `50` status `ready` deltaP `32.2317` edge `0.0366` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.6618` n `130` status `ready` deltaP `25.2644` edge `0.1012` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6123` n `50` status `ready` deltaP `12.7066` edge `0.1993` maxDD `-3.6387`
- `market_context_high->crypto_alt_24h` score `2.5076` n `31` status `ready` deltaP `8.1486` edge `0.3256` maxDD `-11.6768`
- `news_risk_high->metal_24h` score `1.9744` n `130` status `ready` deltaP `23.2692` edge `0.2254` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `1.8334` n `130` status `ready` deltaP `10.0562` edge `0.2864` maxDD `-10.7193`
- `market_context_high->fx_1h` score `1.4304` n `50` status `ready` deltaP `20.1916` edge `0.011` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7211` n `130` status `ready` deltaP `7.0267` edge `0.0669` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.6129` n `130` status `ready` deltaP `7.4758` edge `0.0923` maxDD `-4.2849`
- `market_context_high->equity_24h` score `0.6115` n `31` status `ready` deltaP `0.224` edge `0.2631` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T09:07:27.897982+00:00`
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

- `market_context_high->unknown_1h` score `324.346` n `50` status `ready` deltaP `7.1317` edge `26.9862` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.8856` n `50` status `ready` deltaP `6.8598` edge `23.3614` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.793` n `124` status `ready` deltaP `29.2899` edge `1.4751` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.916` n `45` status `ready` deltaP `32.0138` edge `0.6712` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.4791` n `50` status `ready` deltaP `17.6951` edge `0.4923` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.9136` n `124` status `ready` deltaP `22.9782` edge `0.5745` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.2705` n `124` status `ready` deltaP `28.6881` edge `0.2135` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.1426` n `124` status `ready` deltaP `21.7629` edge `0.7014` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `3.4961` n `45` status `ready` deltaP `13.125` edge `0.3748` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `3.3847` n `50` status `ready` deltaP `12.9878` edge `0.3248` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.0116` n `45` status `ready` deltaP `13.2291` edge `0.4841` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9582` n `50` status `ready` deltaP `33.4512` edge `0.037` maxDD `-0.0791`
- `news_risk_high->crypto_alt_4h` score `2.9139` n `124` status `ready` deltaP `12.3426` edge `0.3612` maxDD `-10.7193`
- `market_context_high->crypto_major_1h` score `2.8811` n `50` status `ready` deltaP `14.5988` edge `0.1878` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.6133` n `124` status `ready` deltaP `24.7928` edge `0.1003` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.5296` n `50` status `ready` deltaP `12.2575` edge `0.1954` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.244` n `124` status `ready` deltaP `26.3833` edge `0.2392` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.5689` n `128` status `ready` deltaP `6.1143` edge `0.0603` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5668` n `45` status `ready` deltaP `13.8542` edge `0.0821` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

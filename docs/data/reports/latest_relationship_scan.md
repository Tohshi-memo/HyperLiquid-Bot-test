# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T10:07:33.344262+00:00`
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

- `market_context_high->unknown_1h` score `324.2656` n `50` status `ready` deltaP `7.1317` edge `26.9795` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9888` n `50` status `ready` deltaP `6.8598` edge `23.37` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3141` n `124` status `ready` deltaP `29.9843` edge `1.5139` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.6666` n `49` status `ready` deltaP `31.4166` edge `0.6544` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.6815` n `50` status `ready` deltaP `18.3049` edge `0.5051` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.0624` n `124` status `ready` deltaP `22.9782` edge `0.5869` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.4093` n `124` status `ready` deltaP `29.2978` edge `0.221` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.2975` n `124` status `ready` deltaP `21.9366` edge `0.7201` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.6627` n `50` status `ready` deltaP `13.5976` edge `0.3439` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.3903` n `49` status `ready` deltaP `16.1316` edge `0.5133` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.1919` n `124` status `ready` deltaP `12.9524` edge `0.3803` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.9582` n `50` status `ready` deltaP `33.4512` edge `0.037` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8523` n `50` status `ready` deltaP `14.4491` edge `0.1864` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.6313` n `124` status `ready` deltaP `24.7928` edge `0.1018` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.5356` n `50` status `ready` deltaP `12.2575` edge `0.1959` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.3105` n `124` status `ready` deltaP `27.0778` edge `0.2431` maxDD `-2.192`
- `market_context_high->crypto_alt_24h` score `2.1087` n `49` status `ready` deltaP `7.1074` edge `0.2993` maxDD `-11.6768`
- `market_context_high->fx_1h` score `1.4579` n `50` status `ready` deltaP `20.491` edge `0.0113` maxDD `-0.113`
- `market_context_high->fx_24h` score `0.7193` n `49` status `ready` deltaP `16.6064` edge `0.0833` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.6624` n `132` status `ready` deltaP `6.7139` edge `0.0641` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

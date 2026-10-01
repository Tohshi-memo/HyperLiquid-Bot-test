# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T08:52:32.369796+00:00`
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

- `market_context_high->unknown_1h` score `324.3388` n `50` status `ready` deltaP `7.1317` edge `26.9856` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9036` n `50` status `ready` deltaP `6.8598` edge `23.3629` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6855` n `124` status `ready` deltaP `29.1163` edge `1.4673` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.8709` n `44` status `ready` deltaP `31.6603` edge `0.6698` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.4537` n `50` status `ready` deltaP `17.5427` edge `0.4912` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.8752` n `124` status `ready` deltaP `22.9782` edge `0.5713` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.2439` n `124` status `ready` deltaP `28.5356` edge `0.2123` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.12` n `124` status `ready` deltaP `21.7629` edge `0.6985` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `3.7913` n `44` status `ready` deltaP `14.8201` edge `0.3881` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `3.351` n `50` status `ready` deltaP `12.8354` edge `0.323` maxDD `-7.6792`
- `market_context_high->fx_4h` score `2.9594` n `50` status `ready` deltaP `33.4512` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9135` n `50` status `ready` deltaP `14.7485` edge `0.1895` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.9126` n `44` status `ready` deltaP `12.4211` edge `0.4768` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `2.8801` n `124` status `ready` deltaP `12.1902` edge `0.3594` maxDD `-10.7193`
- `news_risk_high->index_24h` score `2.6073` n `124` status `ready` deltaP `24.7928` edge `0.0998` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.562` n `50` status `ready` deltaP `12.4072` edge `0.1971` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.2264` n `124` status `ready` deltaP `26.2097` edge `0.2381` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.614` n `127` status `ready` deltaP `6.588` edge `0.0609` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.522` n `44` status `ready` deltaP `13.0682` edge `0.0816` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

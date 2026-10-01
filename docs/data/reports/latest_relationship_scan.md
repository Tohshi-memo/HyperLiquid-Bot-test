# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T21:07:48.411153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6814`

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

- `market_context_high->unknown_1h` score `337.7905` n `50` status `ready` deltaP `8.479` edge `28.0976` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.534` n `50` status `ready` deltaP `6.8598` edge `23.8321` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1667` n `98` status `ready` deltaP `35.8064` edge `1.4628` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.3251` n `50` status `ready` deltaP `33.5625` edge `0.7783` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2245` n `50` status `ready` deltaP `18.7622` edge `0.5473` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.7519` n `50` status `ready` deltaP `11.8472` edge `0.5713` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.01` n `50` status `ready` deltaP `16.189` edge `0.4389` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6066` n `98` status `ready` deltaP `18.9094` edge `0.5732` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8208` n `50` status `ready` deltaP `19.0417` edge `0.5491` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2579` n `111` status `ready` deltaP `27.2839` edge `0.1592` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1172` n `50` status `ready` deltaP `34.8232` edge `0.0411` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0287` n `50` status `ready` deltaP `14.5988` edge `0.2001` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9638` n `50` status `ready` deltaP `13.7545` edge `0.2216` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.6996` n `98` status `ready` deltaP `19.409` edge `0.4516` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.1329` n `98` status `ready` deltaP `22.3427` edge `0.0766` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.047` n `98` status `ready` deltaP `23.526` edge `0.233` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5142` n `50` status `ready` deltaP `21.0898` edge `0.012` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.4733` n `98` status `ready` deltaP `21.1203` edge `0.1126` maxDD `-5.4503`
- `market_context_high->index_24h` score `0.9073` n `50` status `ready` deltaP `14.7917` edge `0.0748` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.4899` n `50` status `ready` deltaP `14.4306` edge `0.0684` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

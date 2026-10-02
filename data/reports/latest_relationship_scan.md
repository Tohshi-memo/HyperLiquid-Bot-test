# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T21:07:32.406880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4884`

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

- `market_context_high->unknown_1h` score `364.3727` n `50` status `ready` deltaP `10.4251` edge `30.2998` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.7307` n `50` status `ready` deltaP `10.2134` edge `24.2428` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4776` n `73` status `ready` deltaP `41.7047` edge `1.116` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.1523` n `50` status `ready` deltaP `18.4444` edge `0.8934` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0474` n `50` status `ready` deltaP `31.8264` edge `0.6834` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.682` n `73` status `ready` deltaP `31.0169` edge `0.5652` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.7253` n `50` status `ready` deltaP `19.0671` edge `0.587` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1155` n `50` status `ready` deltaP `17.2561` edge `0.5235` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.9365` n `116` status `ready` deltaP `23.1182` edge `0.475` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3153` n `50` status `ready` deltaP `15.2515` edge `0.2409` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1211` n `50` status `ready` deltaP `14.4491` edge `0.2088` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5071` n `116` status `ready` deltaP `22.0984` edge `0.1312` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.5908` n `116` status `ready` deltaP `15.7223` edge `0.3301` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5456` n `73` status `ready` deltaP `5.9908` edge `0.4736` maxDD `-15.8971`
- `market_context_high->equity_24h` score `1.4699` n `50` status `ready` deltaP `7.2361` edge `0.3264` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3691` n `73` status `ready` deltaP `13.009` edge `0.2162` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.1678` n `116` status `ready` deltaP `6.1481` edge `0.1124` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9025` n `50` status `ready` deltaP `18.9444` edge `0.0912` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

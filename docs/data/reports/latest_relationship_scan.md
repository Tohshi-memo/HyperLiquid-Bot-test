# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T19:22:36.548068+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6822`

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

- `market_context_high->unknown_1h` score `340.3274` n `50` status `ready` deltaP `8.479` edge `28.309` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.6832` n `50` status `ready` deltaP `6.8598` edge `23.7612` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3106` n `105` status `ready` deltaP `35.5952` edge `1.4762` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.194` n `50` status `ready` deltaP `32.8681` edge `0.772` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3453` n `50` status `ready` deltaP `19.372` edge `0.5533` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.4145` n `50` status `ready` deltaP `11.5` edge `0.5455` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.1162` n `50` status `ready` deltaP `16.6463` edge `0.4447` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.88` n `105` status `ready` deltaP `20.3919` edge `0.5861` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.9051` n `50` status `ready` deltaP `19.0417` edge `0.5599` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3756` n `118` status `ready` deltaP `27.7646` edge `0.1658` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1684` n `50` status `ready` deltaP `35.4329` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0311` n `50` status `ready` deltaP `14.5988` edge `0.2003` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9494` n `50` status `ready` deltaP `13.6048` edge `0.2214` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.9263` n `105` status `ready` deltaP `21.5179` edge `0.4666` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.3834` n `105` status `ready` deltaP `23.8393` edge `0.0875` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2024` n `105` status `ready` deltaP `25.7193` edge `0.2383` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5645` n `50` status `ready` deltaP `21.6886` edge `0.0122` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9042` n `50` status `ready` deltaP `14.7917` edge `0.0744` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.504` n `50` status `ready` deltaP `14.4306` edge `0.0702` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.4853` n `118` status `ready` deltaP `7.2744` edge `0.0456` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

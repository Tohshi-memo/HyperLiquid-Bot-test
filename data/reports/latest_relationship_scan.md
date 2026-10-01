# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T23:37:36.563210+00:00`
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

- `market_context_high->unknown_1h` score `338.5704` n `50` status `ready` deltaP `9.5269` edge `28.1556` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.1077` n `50` status `ready` deltaP `7.9268` edge `23.8728` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.8064` n `88` status `ready` deltaP `37.137` edge `1.4239` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.7376` n `50` status `ready` deltaP `35.2986` edge `0.8011` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2945` n `50` status `ready` deltaP `19.0671` edge `0.5511` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.4853` n `50` status `ready` deltaP `13.4097` edge `0.622` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0392` n `50` status `ready` deltaP `16.4939` edge `0.4393` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.9002` n `88` status `ready` deltaP `16.935` edge `0.5275` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.6976` n `50` status `ready` deltaP `19.0417` edge `0.5333` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0623` n `50` status `ready` deltaP `14.8982` edge `0.2009` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0285` n `50` status `ready` deltaP `14.2036` edge `0.224` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9968` n `50` status `ready` deltaP `33.6037` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.9405` n `101` status `ready` deltaP `25.6263` edge `0.1438` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `2.3395` n `88` status `ready` deltaP `15.8144` edge `0.4294` maxDD `-9.4579`
- `news_risk_high->crypto_alt_4h` score `1.837` n `101` status `ready` deltaP `7.88` edge `0.241` maxDD `-6.9029`
- `news_risk_high->metal_24h` score `1.7617` n `88` status `ready` deltaP `19.5233` edge `0.2231` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.6912` n `88` status `ready` deltaP `19.7917` edge `0.0568` maxDD `-0.4916`
- `news_risk_high->commodity_24h` score `1.6443` n `88` status `ready` deltaP `26.3415` edge `0.1476` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9167` n `50` status `ready` deltaP `14.7917` edge `0.076` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

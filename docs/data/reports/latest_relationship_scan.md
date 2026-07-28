# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T09:22:32.990055+00:00`
- Price records: `672`
- Market context records: `8182`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8690.0895` n `43` status `ready` deltaP `36.9792` edge `723.9276` maxDD `0.0`
- `market_context_high->equity_24h` score `19.481` n `49` status `ready` deltaP `43.2221` edge `1.4263` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.2079` n `50` status `ready` deltaP `41.2561` edge `0.5874` maxDD `-0.2757`
- `market_context_high->metal_24h` score `8.4944` n `49` status `ready` deltaP `43.75` edge `0.4162` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.1938` n `47` status `ready` deltaP `30.2348` edge `0.5106` maxDD `-1.3479`
- `market_context_high->index_4h` score `4.2462` n `50` status `ready` deltaP `38.3598` edge `0.1024` maxDD `-0.0092`
- `market_context_high->crypto_alt_24h` score `3.7289` n `49` status `ready` deltaP `8.9605` edge `0.709` maxDD `-14.2542`
- `news_risk_high->equity_1h` score `3.4596` n `51` status `ready` deltaP `26.0362` edge `0.1456` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.2821` n `47` status `ready` deltaP `17.7932` edge `0.3637` maxDD `-2.2569`
- `market_context_high->equity_1h` score `2.9822` n `50` status `ready` deltaP `15.6048` edge `0.1648` maxDD `-0.6254`
- `market_context_high->metal_4h` score `2.8126` n `50` status `ready` deltaP `28.6463` edge `0.0709` maxDD `-0.5324`
- `news_risk_high->index_4h` score `2.7544` n `47` status `ready` deltaP `23.0832` edge `0.0947` maxDD `-0.191`
- `market_context_high->index_24h` score `2.0732` n `49` status `ready` deltaP `18.6437` edge `0.208` maxDD `-1.3197`
- `news_risk_high->crypto_major_1h` score `1.9637` n `51` status `ready` deltaP `12.8654` edge `0.1176` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.6652` n `51` status `ready` deltaP `12.7157` edge `0.0974` maxDD `-1.1388`
- `news_risk_high->metal_4h` score `1.6046` n `47` status `ready` deltaP `14.7314` edge `0.0823` maxDD `-0.7433`
- `news_risk_high->crypto_alt_4h` score `1.4136` n `47` status `ready` deltaP `16.4277` edge `0.2109` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.1629` n `50` status `ready` deltaP `20.5988` edge `0.0256` maxDD `-0.1069`
- `market_context_high->fx_24h` score `1.1246` n `49` status `ready` deltaP `22.5482` edge `0.0589` maxDD `-0.5369`
- `news_risk_high->index_1h` score `0.6882` n `51` status `ready` deltaP `9.4223` edge `0.0234` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

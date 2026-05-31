# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T22:07:19.638752+00:00`
- Price records: `672`
- Market context records: `2500`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.4703` n `124` status `ready` deltaP `19.8869` edge `0.3561` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.206` n `148` status `ready` deltaP `21.1643` edge `0.4773` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5897` n `148` status `ready` deltaP `17.2421` edge `0.3652` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1633` n `124` status `ready` deltaP `12.78` edge `0.5814` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5375` n `148` status `ready` deltaP `10.3947` edge `0.1638` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4664` n `155` status `ready` deltaP `6.5105` edge `0.1142` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.4527` n `124` status `ready` deltaP `3.0129` edge `0.7337` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.3706` n `155` status `ready` deltaP `6.8099` edge `0.1049` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.13` n `124` status `ready` deltaP `4.3514` edge `0.0799` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1341` n `124` status `ready` deltaP `18.4084` edge `0.0188` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1559` n `148` status `ready` deltaP `6.699` edge `0.0265` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3169` n `155` status `ready` deltaP `1.2671` edge `0.0044` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.502` n `155` status `ready` deltaP `2.9959` edge `0.0035` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5204` n `155` status `ready` deltaP `-0.055` edge `0.0064` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.5579` n `155` status `ready` deltaP `0.0338` edge `0.0042` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.6191` n `155` status `ready` deltaP `1.5559` edge `0.01` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6462` n `148` status `ready` deltaP `-0.8075` edge `0.0085` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8775` n `155` status `ready` deltaP `-0.1902` edge `0.012` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.0245` n `148` status `ready` deltaP `1.8252` edge `0.0412` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

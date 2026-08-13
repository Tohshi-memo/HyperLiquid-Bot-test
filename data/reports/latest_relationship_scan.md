# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T18:32:14.116330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `79.221` n `157` status `ready` deltaP `-25.0354` edge `7.0599` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6818` n `32` status `ready` deltaP `-42.0139` edge `4.6733` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6818` n `32` status `ready` deltaP `-42.0139` edge `4.6733` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.4822` n `36` status `ready` deltaP `10.0694` edge `0.761` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5447` n `36` status `ready` deltaP `35.5183` edge `0.3086` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.2851` n `32` status `ready` deltaP `30.2083` edge `0.1557` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.2851` n `32` status `ready` deltaP `30.2083` edge `0.1557` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6938` n `32` status `ready` deltaP `18.9787` edge `0.1162` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6938` n `32` status `ready` deltaP `18.9787` edge `0.1162` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5052` n `36` status `ready` deltaP `15.625` edge `0.1046` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.3354` n `157` status `ready` deltaP `20.0172` edge `0.1415` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.8311` n `32` status `ready` deltaP `20.6597` edge `0.0333` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8311` n `32` status `ready` deltaP `20.6597` edge `0.0333` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6495` n `36` status `ready` deltaP `19.4613` edge `0.0209` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5366` n `157` status `ready` deltaP `16.6499` edge `0.0809` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3533` n `36` status `ready` deltaP `6.9362` edge `0.0984` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.2886` n `32` status `ready` deltaP `13.0208` edge `0.194` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2886` n `32` status `ready` deltaP `13.0208` edge `0.194` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2874` n `32` status `ready` deltaP `13.8099` edge `0.0385` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2874` n `32` status `ready` deltaP `13.8099` edge `0.0385` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T21:52:16.155138+00:00`
- Price records: `672`
- Market context records: `2499`
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

- `market_context_high->unknown_24h` score `5.4619` n `124` status `ready` deltaP `19.8869` edge `0.3554` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.1679` n `147` status `ready` deltaP `21.1237` edge `0.4744` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5644` n `147` status `ready` deltaP `17.0307` edge `0.3645` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1656` n `124` status `ready` deltaP `12.78` edge `0.5817` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.4799` n `147` status `ready` deltaP `10.1097` edge `0.1609` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4381` n `154` status `ready` deltaP `6.3963` edge `0.1126` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.4301` n `124` status `ready` deltaP `3.0129` edge `0.7308` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.3591` n `154` status `ready` deltaP `6.6957` edge `0.1047` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.1264` n `124` status `ready` deltaP `4.3514` edge `0.0796` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1341` n `124` status `ready` deltaP `18.4084` edge `0.0188` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1648` n `147` status `ready` deltaP `6.6171` edge `0.0263` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3342` n `154` status `ready` deltaP `0.9488` edge `0.0043` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.5376` n `154` status `ready` deltaP `-0.1944` edge `0.0059` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5495` n `154` status `ready` deltaP `2.6985` edge `-0.0006` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.5891` n `154` status `ready` deltaP `1.7498` edge `0.0112` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6364` n `147` status `ready` deltaP `-0.6336` edge `0.0086` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.8151` n `154` status `ready` deltaP `0.348` edge `0.0057` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8549` n `154` status `ready` deltaP `0.0623` edge `0.0122` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.0181` n `147` status `ready` deltaP `1.9806` edge `0.0407` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

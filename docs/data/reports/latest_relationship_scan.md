# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T18:22:20.193031+00:00`
- Price records: `672`
- Market context records: `2482`
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

- `market_context_high->unknown_24h` score `5.2447` n `124` status `ready` deltaP `19.8869` edge `0.3373` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3162` n `136` status `ready` deltaP `21.8077` edge `0.4822` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.058` n `136` status `ready` deltaP `19.0907` edge `0.3919` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.8431` n `124` status `ready` deltaP `10.523` edge `0.5554` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5021` n `136` status `ready` deltaP `9.6934` edge `0.1626` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.6238` n `145` status `ready` deltaP `8.4442` edge `0.1151` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.5311` n `145` status `ready` deltaP `6.8243` edge `0.1175` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0304` n `124` status `ready` deltaP `4.3514` edge `0.0716` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1581` n `124` status `ready` deltaP `18.4084` edge `0.0168` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2212` n `136` status `ready` deltaP `5.4878` edge `0.0192` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2791` n `145` status `ready` deltaP `1.9647` edge `0.0046` maxDD `-0.278`
- `market_context_high->crypto_alt_24h` score `-0.3047` n `124` status `ready` deltaP `0.5824` edge `0.6528` maxDD `-43.6595`
- `market_context_high->unknown_1h` score `-0.4472` n `145` status `ready` deltaP `1.9647` edge `0.0216` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.5122` n `145` status `ready` deltaP `0.5214` edge `0.0068` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.5442` n `145` status `ready` deltaP `-0.0671` edge `0.0045` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5797` n `145` status `ready` deltaP `2.1464` edge `-0.0008` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6049` n `136` status `ready` deltaP `-0.0269` edge `0.0086` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8716` n `145` status `ready` deltaP `-0.3561` edge `0.0136` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9088` n `136` status `ready` deltaP `3.5868` edge `0.0391` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

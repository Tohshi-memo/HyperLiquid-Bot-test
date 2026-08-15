# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T13:07:26.617234+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.5431` n `128` status `ready` deltaP `-24.2892` edge `11.9151` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.682` n `32` status `ready` deltaP `-37.5704` edge `4.6437` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.682` n `32` status `ready` deltaP `-37.5704` edge `4.6437` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.7434` n `36` status `ready` deltaP `25.2744` edge `0.9314` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7221` n `36` status `ready` deltaP `40.3963` edge `0.3742` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4105` n `128` status `ready` deltaP `31.2784` edge `0.2481` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9866` n `32` status `ready` deltaP `33.6222` edge `0.1914` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9866` n `32` status `ready` deltaP `33.6222` edge `0.1914` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2448` n `32` status `ready` deltaP `28.2008` edge `0.4718` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2448` n `32` status `ready` deltaP `28.2008` edge `0.4718` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.5618` n `36` status `ready` deltaP `29.4627` edge `0.1004` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9415` n `32` status `ready` deltaP `21.2652` edge `0.1216` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9415` n `32` status `ready` deltaP `21.2652` edge `0.1216` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.9937` n `128` status `ready` deltaP `19.7027` edge `0.0819` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9388` n `36` status `ready` deltaP `22.3577` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.755` n `36` status `ready` deltaP `8.5829` edge `0.1209` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3342` n `32` status `ready` deltaP `14.259` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3342` n `32` status `ready` deltaP `14.259` edge `0.0394` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6976` n `128` status `ready` deltaP `9.5715` edge `0.024` maxDD `-0.3742`
- `risk_on_high->equity_24h` score `0.637` n `32` status `ready` deltaP `13.8161` edge `0.1675` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

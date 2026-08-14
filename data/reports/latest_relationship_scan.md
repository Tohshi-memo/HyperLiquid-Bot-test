# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T00:06:18.824150+00:00`
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

- `market_context_high->unknown_24h` score `91.1489` n `150` status `ready` deltaP `-27.5417` edge `8.0706` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7061` n `32` status `ready` deltaP `-41.6667` edge `4.6741` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7061` n `32` status `ready` deltaP `-41.6667` edge `4.6741` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5458` n `36` status `ready` deltaP `10.0694` edge `0.7663` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5539` n `36` status `ready` deltaP `35.2134` edge `0.3114` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7121` n `32` status `ready` deltaP `32.2917` edge `0.1774` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7121` n `32` status `ready` deltaP `32.2917` edge `0.1774` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9542` n `32` status `ready` deltaP `20.8079` edge `0.1257` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9542` n `32` status `ready` deltaP `20.8079` edge `0.1257` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.785` n `150` status `ready` deltaP `22.2917` edge `0.1638` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3091` n `36` status `ready` deltaP `14.5833` edge `0.0952` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.5926` n `150` status `ready` deltaP `17.3496` edge `0.0809` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5098` n `36` status `ready` deltaP `18.0894` edge `0.0184` maxDD `-0.0546`
- `risk_on_high->fx_24h` score `1.4572` n `32` status `ready` deltaP `16.8403` edge `0.0276` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.4572` n `32` status `ready` deltaP `16.8403` edge `0.0276` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.4325` n `36` status `ready` deltaP `6.7865` edge `0.106` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1387` n `32` status `ready` deltaP `11.4583` edge `0.1852` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1387` n `32` status `ready` deltaP `11.4583` edge `0.1852` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

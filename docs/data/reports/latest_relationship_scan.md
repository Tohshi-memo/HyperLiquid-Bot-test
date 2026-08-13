# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T21:52:25.815176+00:00`
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

- `market_context_high->unknown_24h` score `91.1681` n `150` status `ready` deltaP `-27.5417` edge `8.0722` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7186` n `32` status `ready` deltaP `-41.6667` edge `4.6757` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7186` n `32` status `ready` deltaP `-41.6667` edge `4.6757` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5434` n `36` status `ready` deltaP `10.0694` edge `0.7661` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5903` n `36` status `ready` deltaP `35.5183` edge `0.3124` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6641` n `32` status `ready` deltaP `32.2917` edge `0.1734` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6641` n `32` status `ready` deltaP `32.2917` edge `0.1734` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9676` n `32` status `ready` deltaP `20.9604` edge `0.1258` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9676` n `32` status `ready` deltaP `20.9604` edge `0.1258` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.737` n `150` status `ready` deltaP `22.2917` edge `0.1598` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.3559` n `36` status `ready` deltaP `14.5833` edge `0.0991` maxDD `0.0`
- `news_risk_high->index_4h` score `1.6203` n `36` status `ready` deltaP `19.1565` edge `0.0205` maxDD `-0.0546`
- `risk_on_high->fx_24h` score `1.6086` n `32` status `ready` deltaP `18.4028` edge `0.0298` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6086` n `32` status `ready` deltaP `18.4028` edge `0.0298` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.606` n `150` status `ready` deltaP `17.5021` edge `0.081` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4337` n `36` status `ready` deltaP `6.7865` edge `0.1061` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.333` n `32` status `ready` deltaP `14.1093` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2912` n `32` status `ready` deltaP `12.5` edge `0.1978` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2912` n `32` status `ready` deltaP `12.5` edge `0.1978` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

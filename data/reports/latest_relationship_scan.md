# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T22:37:27.867831+00:00`
- Price records: `672`
- Market context records: `3627`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `40.808` n `32` status `ready` deltaP `45.4861` edge `3.1017` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `40.808` n `32` status `ready` deltaP `45.4861` edge `3.1017` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `37.768` n `32` status `ready` deltaP `47.5694` edge `2.8302` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `37.768` n `32` status `ready` deltaP `47.5694` edge `2.8302` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `33.2774` n `32` status `ready` deltaP `44.6181` edge `2.4908` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `33.2774` n `32` status `ready` deltaP `44.6181` edge `2.4908` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.7192` n `32` status `ready` deltaP `47.5694` edge `1.4928` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.7192` n `32` status `ready` deltaP `47.5694` edge `1.4928` maxDD `0.0`
- `risk_on_high->metal_24h` score `14.2204` n `32` status `ready` deltaP `33.1597` edge `0.9901` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.2204` n `32` status `ready` deltaP `33.1597` edge `0.9901` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.3704` n `32` status `ready` deltaP `22.4085` edge `0.9937` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.3704` n `32` status `ready` deltaP `22.4085` edge `0.9937` maxDD `-5.9781`
- `market_context_high->equity_24h` score `12.0379` n `158` status `ready` deltaP `24.1517` edge `1.4834` maxDD `-40.9667`
- `market_context_high->index_24h` score `10.3692` n `158` status `ready` deltaP `32.3795` edge `0.8699` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `5.4855` n `158` status `ready` deltaP `11.2693` edge `1.1551` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.7677` n `158` status `ready` deltaP `27.0679` edge `0.8848` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.942` n `32` status `ready` deltaP `2.9726` edge `0.4931` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.942` n `32` status `ready` deltaP `2.9726` edge `0.4931` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.8073` n `32` status `ready` deltaP `11.814` edge `0.3946` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.8073` n `32` status `ready` deltaP `11.814` edge `0.3946` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

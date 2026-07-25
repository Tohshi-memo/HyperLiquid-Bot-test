# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T22:52:31.664693+00:00`
- Price records: `672`
- Market context records: `7925`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.5678` n `82` status `ready` deltaP `25.7749` edge `1.343` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3762` n `82` status `ready` deltaP `39.1681` edge `0.4369` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7333` n `91` status `ready` deltaP `24.8681` edge `0.4846` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.3824` n `82` status `ready` deltaP `27.185` edge `0.2539` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.8159` n `91` status `ready` deltaP `28.9865` edge `0.0774` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7407` n `91` status `ready` deltaP `24.4841` edge `0.1274` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7709` n `91` status `ready` deltaP `13.5795` edge `0.1388` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.3366` n `91` status `ready` deltaP `9.525` edge `0.1596` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.3075` n `82` status `ready` deltaP `10.9587` edge `0.1616` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2227` n `82` status `ready` deltaP `26.3635` edge `0.0349` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.0808` n `91` status `ready` deltaP `10.9606` edge `0.1888` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0468` n `91` status `ready` deltaP `15.9819` edge `0.0237` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6276` n `91` status `ready` deltaP `8.8406` edge `0.0312` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5681` n `91` status `ready` deltaP `10.5893` edge `0.0431` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2218` n `91` status `ready` deltaP `4.6934` edge `0.0404` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3648` n `91` status `ready` deltaP `0.754` edge `0.0013` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4059` n `91` status `ready` deltaP `0.9933` edge `-0.0018` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5188` n `91` status `ready` deltaP `2.5843` edge `0.016` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5943` n `91` status `ready` deltaP `3.006` edge `0.0052` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8767` n `91` status `ready` deltaP `8.0921` edge `-0.168` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

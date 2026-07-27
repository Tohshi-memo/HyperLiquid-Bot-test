# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T00:52:28.506615+00:00`
- Price records: `672`
- Market context records: `8041`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `18.139` n `80` status `ready` deltaP `29.987` edge `1.4027` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.1284` n `80` status `ready` deltaP `35.8752` edge `0.4382` maxDD `0.0`
- `market_context_high->equity_4h` score `7.1535` n `93` status `ready` deltaP `28.3995` edge `0.4854` maxDD `-4.2882`
- `market_context_high->commodity_24h` score `4.4673` n `80` status `ready` deltaP `30.4701` edge `0.2846` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.6454` n `93` status `ready` deltaP `27.5013` edge `0.0731` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.4602` n `93` status `ready` deltaP `22.2528` edge `0.1189` maxDD `-0.979`
- `market_context_high->index_24h` score `2.1117` n `80` status `ready` deltaP `11.8198` edge `0.1642` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.8053` n `93` status `ready` deltaP `15.0747` edge `0.1317` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1783` n `80` status `ready` deltaP `27.2704` edge `0.0453` maxDD `-1.083`
- `market_context_high->index_1h` score `0.8524` n `93` status `ready` deltaP `13.9721` edge `0.0209` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.8302` n `93` status `ready` deltaP `11.3724` edge `0.0312` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4404` n `93` status `ready` deltaP `9.9157` edge `0.0314` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.2997` n `93` status `ready` deltaP `7.6318` edge `0.1459` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.2559` n `93` status `ready` deltaP `4.1011` edge `0.1057` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0443` n `93` status `ready` deltaP `1.2861` edge `0.029` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.1316` n `93` status `ready` deltaP `5.832` edge `0.0044` maxDD `-0.6732`
- `market_context_high->commodity_1h` score `-0.4927` n `93` status `ready` deltaP `0.1433` edge `-0.0018` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.7436` n `93` status `ready` deltaP `-3.6958` edge `-0.0006` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-0.9835` n `93` status `ready` deltaP `3.1782` edge `0.0029` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.0878` n `93` status `ready` deltaP `6.1586` edge `-0.1727` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

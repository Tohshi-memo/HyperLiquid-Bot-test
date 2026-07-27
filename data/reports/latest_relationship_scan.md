# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T01:07:27.377045+00:00`
- Price records: `672`
- Market context records: `8042`
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

- `market_context_high->equity_24h` score `18.4127` n `79` status `ready` deltaP `30.858` edge `1.4197` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.1656` n `79` status `ready` deltaP `35.8752` edge `0.4413` maxDD `0.0`
- `market_context_high->equity_4h` score `7.2892` n `92` status `ready` deltaP `29.1821` edge `0.4908` maxDD `-4.233`
- `market_context_high->commodity_24h` score `4.6648` n `79` status `ready` deltaP `31.4986` edge `0.2942` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.6424` n `92` status `ready` deltaP `27.3728` edge `0.0737` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.416` n `92` status `ready` deltaP `22.0307` edge `0.1167` maxDD `-0.979`
- `market_context_high->index_24h` score `2.0892` n `79` status `ready` deltaP `11.3135` edge `0.1657` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.7266` n `92` status `ready` deltaP `14.8855` edge `0.1264` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.239` n `79` status `ready` deltaP `27.7933` edge `0.0472` maxDD `-0.891`
- `market_context_high->index_1h` score `0.8198` n `92` status `ready` deltaP `13.7594` edge `0.0196` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7981` n `92` status `ready` deltaP `11.1364` edge `0.0301` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4069` n `92` status `ready` deltaP `9.6329` edge `0.029` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.2576` n `92` status `ready` deltaP `7.2111` edge `0.1452` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.1954` n `92` status `ready` deltaP `3.6453` edge `0.1037` maxDD `-3.9374`
- `market_context_high->fx_4h` score `-0.0953` n `92` status `ready` deltaP `6.1705` edge `0.0046` maxDD `-0.6279`
- `market_context_high->crypto_alt_1h` score `-0.0965` n `92` status `ready` deltaP `0.8982` edge `0.0249` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.4676` n `92` status `ready` deltaP `0.5663` edge `-0.0014` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.7943` n `92` status `ready` deltaP `-4.3153` edge `-0.0007` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-0.9404` n `92` status `ready` deltaP `3.7977` edge `0.0043` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.104` n `92` status `ready` deltaP `5.8058` edge `-0.1717` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

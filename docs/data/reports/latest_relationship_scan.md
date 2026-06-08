# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T01:37:25.028539+00:00`
- Price records: `672`
- Market context records: `3236`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.4387` n `103` status `ready` deltaP `19.345` edge `2.7063` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.7948` n `103` status `ready` deltaP `49.904` edge `0.8597` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.7575` n `103` status `ready` deltaP `32.531` edge `0.8517` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.7479` n `103` status `ready` deltaP `20.09` edge `1.5728` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.85` n `103` status `ready` deltaP `23.4156` edge `2.2792` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.5821` n `31` status `ready` deltaP `10.5273` edge `0.3678` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5821` n `31` status `ready` deltaP `10.5273` edge `0.3678` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.9852` n `134` status `ready` deltaP `17.1323` edge `0.1405` maxDD `-3.4758`
- `risk_on_high->crypto_alt_1h` score `0.6755` n `31` status `ready` deltaP `3.7087` edge `0.2056` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6755` n `31` status `ready` deltaP `3.7087` edge `0.2056` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4834` n `31` status `ready` deltaP `8.2142` edge `0.0757` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4834` n `31` status `ready` deltaP `8.2142` edge `0.0757` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3235` n `31` status `ready` deltaP `2.3614` edge `0.1161` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3235` n `31` status `ready` deltaP `2.3614` edge `0.1161` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1468` n `31` status `ready` deltaP `-0.1159` edge `0.0443` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1468` n `31` status `ready` deltaP `-0.1159` edge `0.0443` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.4181` n `146` status `ready` deltaP `3.8738` edge `0.0209` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.5476` n `146` status `ready` deltaP `3.5518` edge `0.0124` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.679` n `134` status `ready` deltaP `10.1838` edge `0.1021` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7969` n `146` status `ready` deltaP `3.6338` edge `0.0999` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

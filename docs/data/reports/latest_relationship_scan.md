# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T05:37:14.877527+00:00`
- Price records: `672`
- Market context records: `1497`
- Flow alert records: `6221`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8811`

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

- `market_context_high->metal_24h` score `12.67` n `171` status `ready` deltaP `21.2628` edge `1.0183` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.374` n `171` status `ready` deltaP `28.9748` edge `0.9563` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.2817` n `171` status `ready` deltaP `27.33` edge `0.7878` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8556` n `171` status `ready` deltaP `20.2851` edge `0.2947` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1034` n `171` status `ready` deltaP `13.56` edge `0.4009` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2049` n `197` status `ready` deltaP `6.7809` edge `0.1382` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9935` n `171` status `ready` deltaP `19.7551` edge `0.056` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.2401` n `197` status `ready` deltaP `1.3518` edge `0.031` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2986` n `197` status `ready` deltaP `2.1331` edge `0.0074` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.4501` n `197` status `ready` deltaP `10.1468` edge `0.2268` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.5387` n `197` status `ready` deltaP `-0.4103` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5518` n `197` status `ready` deltaP `1.4377` edge `0.0468` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.7661` n `197` status `ready` deltaP `5.349` edge `-0.0003` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.7904` n `197` status `ready` deltaP `5.8832` edge `0.1658` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-0.9734` n `197` status `ready` deltaP `-3.4047` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.0052` n `197` status `ready` deltaP `-2.2007` edge `0.0398` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.1611` n `197` status `ready` deltaP `11.6743` edge `0.0946` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.1643` n `197` status `ready` deltaP `-0.5532` edge `-0.0012` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5577` n `197` status `ready` deltaP `-1.0677` edge `0.013` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.3727` n `197` status `ready` deltaP `-14.6666` edge `-0.0912` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T01:07:21.968184+00:00`
- Price records: `672`
- Market context records: `3234`
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

- `market_context_high->crypto_alt_24h` score `14.4966` n `103` status `ready` deltaP `19.6922` edge `2.7114` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.8574` n `103` status `ready` deltaP `50.2512` edge `0.8626` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.8153` n `103` status `ready` deltaP `32.8782` edge `0.8542` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.8112` n `103` status `ready` deltaP `20.4373` edge `1.5786` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.9913` n `103` status `ready` deltaP `23.7628` edge `2.295` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.5681` n `31` status `ready` deltaP `10.5273` edge `0.366` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5681` n `31` status `ready` deltaP `10.5273` edge `0.366` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0258` n `132` status `ready` deltaP `17.415` edge `0.142` maxDD `-3.4758`
- `risk_on_high->crypto_alt_1h` score `0.6497` n `31` status `ready` deltaP `3.559` edge `0.2033` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6497` n `31` status `ready` deltaP `3.559` edge `0.2033` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4428` n `31` status `ready` deltaP `7.9148` edge `0.0725` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4428` n `31` status `ready` deltaP `7.9148` edge `0.0725` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.2838` n `31` status `ready` deltaP `2.062` edge `0.113` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.2838` n `31` status `ready` deltaP `2.062` edge `0.113` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1468` n `31` status `ready` deltaP `-0.1159` edge `0.0443` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1468` n `31` status `ready` deltaP `-0.1159` edge `0.0443` maxDD `-1.3216`
- `market_context_high->index_1h` score `-0.4639` n `144` status `ready` deltaP `4.2748` edge `0.0183` maxDD `-4.5023`
- `market_context_high->commodity_1h` score `-0.4998` n `144` status `ready` deltaP `3.3766` edge `0.0174` maxDD `-2.5251`
- `market_context_high->unknown_4h` score `-0.677` n `132` status `ready` deltaP `9.9686` edge `0.1037` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.685` n `144` status `ready` deltaP `4.2997` edge `0.1098` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

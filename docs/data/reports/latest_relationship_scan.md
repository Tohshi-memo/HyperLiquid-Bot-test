# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T00:52:23.500953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.1608` n `103` status `ready` deltaP `4.5729` edge `0.5389` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.536` n `103` status `ready` deltaP `12.559` edge `0.1852` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4609` n `117` status `ready` deltaP `14.1951` edge `0.0944` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8529` n `103` status `ready` deltaP `22.0958` edge `0.0487` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.8064` n `129` status `ready` deltaP `9.8396` edge `0.0359` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4721` n `103` status `ready` deltaP `9.1002` edge `0.153` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4052` n `129` status `ready` deltaP `3.0126` edge `-0.0043` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5162` n `129` status `ready` deltaP `-3.0984` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.5831` n `117` status `ready` deltaP `-0.2319` edge `-0.0127` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5964` n `129` status `ready` deltaP `-3.0717` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.5971` n `117` status `ready` deltaP `4.3908` edge `-0.0037` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.8265` n `129` status `ready` deltaP `1.0177` edge `0.0072` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.091` n `117` status `ready` deltaP `-3.4331` edge `-0.0161` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1477` n `129` status `ready` deltaP `-12.0747` edge `-0.0343` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.2551` n `117` status `ready` deltaP `1.5752` edge `-0.0647` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0419` n `129` status `ready` deltaP `-10.0322` edge `-0.0654` maxDD `-6.3636`
- `market_context_high->crypto_major_24h` score `-3.7399` n `103` status `ready` deltaP `6.2197` edge `-0.1037` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4578` n `103` status `ready` deltaP `-12.4461` edge `-0.1442` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7261` n `117` status `ready` deltaP `-13.1776` edge `-0.1408` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.1775` n `129` status `ready` deltaP `-4.5363` edge `-0.6065` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T03:52:28.703801+00:00`
- Price records: `672`
- Market context records: `6881`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `0.7802` n `181` status `ready` deltaP `-4.2188` edge `0.5066` maxDD `-12.6092`
- `market_context_high->fx_1h` score `-0.2409` n `224` status `ready` deltaP `2.3872` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5698` n `224` status `ready` deltaP `2.0611` edge `0.0152` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6065` n `224` status `ready` deltaP `3.6971` edge `0.0152` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6128` n `224` status `ready` deltaP `-0.8982` edge `-0.0041` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8071` n `224` status `ready` deltaP `-1.4783` edge `-0.0025` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8931` n `224` status `ready` deltaP `-4.5926` edge `-0.0071` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.926` n `224` status `ready` deltaP `12.1734` edge `0.0065` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3407` n `224` status `ready` deltaP `-2.3411` edge `-0.0073` maxDD `-5.5853`
- `market_context_high->commodity_24h` score `-1.5302` n `181` status `ready` deltaP `2.5958` edge `0.042` maxDD `-5.2791`
- `market_context_high->unknown_1h` score `-1.5954` n `224` status `ready` deltaP `-2.9619` edge `-0.0231` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8385` n `224` status `ready` deltaP `1.1869` edge `-0.0256` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.982` n `224` status `ready` deltaP `3.9417` edge `-0.0224` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3794` n `224` status `ready` deltaP `0.49` edge `-0.01` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0781` n `224` status `ready` deltaP `-1.3066` edge `-0.0532` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1025` n `224` status `ready` deltaP `-0.0762` edge `-0.0389` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1881` n `224` status `ready` deltaP `-9.6472` edge `0.0352` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.379` n `181` status `ready` deltaP `-7.9033` edge `-0.0086` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3308` n `224` status `ready` deltaP `1.4917` edge `-0.1553` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.7796` n `181` status `ready` deltaP `-16.5478` edge `-0.1567` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

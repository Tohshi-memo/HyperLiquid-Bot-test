# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T02:52:18.537330+00:00`
- Price records: `672`
- Market context records: `1486`
- Flow alert records: `6187`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `12.1752` n `172` status `ready` deltaP `28.985` edge `1.023` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.3249` n `172` status `ready` deltaP `16.8281` edge `0.9816` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.1128` n `172` status `ready` deltaP `27.3538` edge `0.8569` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0826` n `172` status `ready` deltaP `20.3327` edge `0.3133` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8601` n `172` status `ready` deltaP `13.6144` edge `0.4636` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5434` n `208` status `ready` deltaP `7.3523` edge `0.1626` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.677` n `172` status `ready` deltaP `16.5779` edge `0.0508` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1003` n `208` status `ready` deltaP `11.9723` edge `0.2605` maxDD `-19.5565`
- `market_context_high->equity_1h` score `0.0185` n `208` status `ready` deltaP `3.2041` edge `0.0402` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1114` n `208` status `ready` deltaP `3.5583` edge `0.0135` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.546` n `208` status `ready` deltaP `-0.5355` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5697` n `208` status `ready` deltaP `1.1832` edge `0.047` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.6804` n `208` status `ready` deltaP `-0.3752` edge `0.0547` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-0.7143` n `208` status `ready` deltaP `6.6838` edge `0.1668` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7412` n `208` status `ready` deltaP `5.7232` edge `0.0004` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.0073` n `208` status `ready` deltaP `-4.0572` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.115` n `208` status `ready` deltaP `-0.2677` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.6117` n `208` status `ready` deltaP `8.9822` edge `0.075` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.636` n `208` status `ready` deltaP `-1.5517` edge `0.0097` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.1301` n `208` status `ready` deltaP `-12.7463` edge `-0.0729` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

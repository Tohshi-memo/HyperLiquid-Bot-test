# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T03:37:17.748144+00:00`
- Price records: `672`
- Market context records: `1489`
- Flow alert records: `6196`
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

- `market_context_high->crypto_alt_24h` score `11.9136` n `172` status `ready` deltaP `28.985` edge `1.0012` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.6567` n `172` status `ready` deltaP `18.0515` edge `0.9886` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `10.8776` n `172` status `ready` deltaP `27.3538` edge `0.8373` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0058` n `172` status `ready` deltaP `20.3327` edge `0.3069` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.6345` n `172` status `ready` deltaP `13.6144` edge `0.4448` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4713` n `205` status `ready` deltaP `7.5` edge `0.1556` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.7566` n `172` status `ready` deltaP `17.3934` edge `0.052` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0476` n `205` status `ready` deltaP `11.4939` edge `0.2593` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0251` n `205` status `ready` deltaP `2.7187` edge `0.0398` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1496` n `205` status `ready` deltaP `3.2014` edge `0.0127` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5497` n `205` status `ready` deltaP `-0.5769` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5679` n `205` status `ready` deltaP `1.191` edge `0.0471` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.611` n `205` status `ready` deltaP `7.2561` edge `0.1716` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7158` n `205` status `ready` deltaP `6.1078` edge `0.0011` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.7691` n `205` status `ready` deltaP `-0.8536` edge `0.0505` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9937` n `205` status `ready` deltaP `-3.811` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0686` n `205` status `ready` deltaP `0.1329` edge `0.0022` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.4584` n `205` status `ready` deltaP `9.8476` edge `0.082` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.637` n `205` status `ready` deltaP `-1.6248` edge `0.0101` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.1874` n `205` status `ready` deltaP `-13.2318` edge `-0.077` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

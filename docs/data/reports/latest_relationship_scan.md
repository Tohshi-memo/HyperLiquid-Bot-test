# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T16:52:16.611797+00:00`
- Price records: `672`
- Market context records: `1545`
- Flow alert records: `6360`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8803`

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

- `market_context_high->metal_24h` score `12.5109` n `180` status `ready` deltaP `23.2986` edge `0.9873` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2488` n `180` status `ready` deltaP `27.5` edge `0.9557` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6119` n `180` status `ready` deltaP `27.7777` edge `0.729` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0899` n `180` status `ready` deltaP `20.6944` edge `0.3115` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6566` n `180` status `ready` deltaP `13.6459` edge `0.3631` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7064` n `180` status `ready` deltaP `16.7361` edge `0.0522` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.2345` n `199` status `ready` deltaP `4.6337` edge `0.0981` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.279` n `199` status `ready` deltaP `12.4923` edge `0.2129` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.3635` n `199` status `ready` deltaP `8.5174` edge `0.1675` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4587` n `199` status `ready` deltaP `0.5183` edge `0.0401` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6242` n `199` status `ready` deltaP `-1.9942` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7336` n `199` status `ready` deltaP `-0.4972` edge `0.0014` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7633` n `199` status `ready` deltaP `4.8484` edge `0.0034` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7968` n `199` status `ready` deltaP `-0.4235` edge `-0.0004` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8596` n `199` status `ready` deltaP `-1.4819` edge `0.0191` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9839` n `199` status `ready` deltaP `-0.8929` edge `0.0155` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3357` n `199` status `ready` deltaP `-9.7875` edge `-0.0131` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3851` n `199` status `ready` deltaP `10.0587` edge `0.0867` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4282` n `199` status `ready` deltaP `-4.5923` edge `0.0205` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.2343` n `199` status `ready` deltaP `-15.3098` edge `-0.1063` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

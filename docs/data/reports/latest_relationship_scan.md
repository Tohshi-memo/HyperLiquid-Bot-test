# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T17:07:20.639895+00:00`
- Price records: `672`
- Market context records: `1546`
- Flow alert records: `6363`
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

- `market_context_high->metal_24h` score `12.3856` n `181` status `ready` deltaP `22.9473` edge `0.9792` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1517` n `181` status `ready` deltaP `27.3356` edge `0.9487` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.4658` n `181` status `ready` deltaP `27.256` edge `0.7203` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1222` n `181` status `ready` deltaP `20.7374` edge `0.3139` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.644` n `181` status `ready` deltaP `13.698` edge `0.3617` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.6982` n `181` status `ready` deltaP `16.6331` edge `0.0522` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.2503` n `199` status `ready` deltaP `4.7861` edge `0.0984` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.2508` n `199` status `ready` deltaP `12.6448` edge `0.2155` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.3376` n `199` status `ready` deltaP `8.6699` edge `0.1698` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.454` n `199` status `ready` deltaP `0.5183` edge `0.0407` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6242` n `199` status `ready` deltaP `-1.9942` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7203` n `199` status `ready` deltaP `-0.3475` edge `0.0021` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7633` n `199` status `ready` deltaP `4.8484` edge `0.0034` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7968` n `199` status `ready` deltaP `-0.4235` edge `-0.0004` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8584` n `199` status `ready` deltaP `-1.4819` edge `0.0192` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9792` n `199` status `ready` deltaP `-0.8929` edge `0.0161` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3365` n `199` status `ready` deltaP `-9.7875` edge `-0.0132` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3681` n `199` status `ready` deltaP `10.2111` edge `0.0871` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.433` n `199` status `ready` deltaP `-4.5923` edge `0.0201` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.2171` n `199` status `ready` deltaP `-15.1574` edge `-0.1051` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T07:22:17.875710+00:00`
- Price records: `672`
- Market context records: `1607`
- Flow alert records: `6539`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.3484` n `184` status `ready` deltaP `29.6724` edge `1.0271` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1329` n `184` status `ready` deltaP `26.0341` edge `1.0268` maxDD `-20.1429`
- `market_context_high->crypto_major_24h` score `8.8823` n `184` status `ready` deltaP `25.8303` edge `0.7902` maxDD `-15.4436`
- `market_context_high->equity_24h` score `4.87` n `184` status `ready` deltaP `20.3125` edge `0.5031` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.0865` n `184` status `ready` deltaP `21.792` edge `0.3039` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2414` n `196` status `ready` deltaP `10.6054` edge `0.1422` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.152` n `196` status `ready` deltaP `12.8609` edge `0.2657` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0539` n `196` status `ready` deltaP `8.9846` edge `0.2179` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1971` n `184` status `ready` deltaP `7.8125` edge `0.0364` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3692` n `196` status `ready` deltaP `0.4552` edge `0.052` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5654` n `196` status `ready` deltaP `0.5897` edge `0.0298` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6914` n `196` status `ready` deltaP `0.3239` edge `0.0034` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8867` n `196` status `ready` deltaP `-1.0754` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.9186` n `196` status `ready` deltaP `-1.0479` edge `0.0249` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9405` n `196` status `ready` deltaP `-0.1618` edge `0.0316` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.1402` n `196` status `ready` deltaP `-0.5377` edge `0.0007` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1654` n `196` status `ready` deltaP `4.7202` edge `0.005` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.4077` n `196` status `ready` deltaP `-10.9476` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4238` n `196` status `ready` deltaP `8.8259` edge `0.0917` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.2032` n `196` status `ready` deltaP `-14.2452` edge `-0.1094` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T08:52:18.010838+00:00`
- Price records: `672`
- Market context records: `1614`
- Flow alert records: `6556`
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

- `market_context_high->metal_24h` score `11.9363` n `187` status `ready` deltaP `27.645` edge `0.9743` maxDD `-8.4459`
- `market_context_high->index_24h` score `3.652` n `187` status `ready` deltaP `19.7907` edge `0.2852` maxDD `-5.3574`
- `market_context_high->crypto_major_24h` score `3.5958` n `187` status `ready` deltaP `23.8116` edge `0.6764` maxDD `-38.5062`
- `market_context_high->crypto_alt_24h` score `3.5559` n `187` status `ready` deltaP `23.937` edge `0.8715` maxDD `-55.114`
- `market_context_high->equity_24h` score `2.5901` n `187` status `ready` deltaP `18.3462` edge `0.4366` maxDD `-23.1119`
- `market_context_high->equity_4h` score `1.3295` n `193` status `ready` deltaP `11.076` edge `0.1464` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.3301` n `193` status `ready` deltaP `13.2124` edge `0.2862` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1863` n `193` status `ready` deltaP `9.2806` edge `0.2329` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2471` n `187` status `ready` deltaP `7.6519` edge `0.0333` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3015` n `193` status `ready` deltaP `0.4662` edge `0.0606` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4903` n `193` status `ready` deltaP `1.2139` edge `0.0319` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6881` n `193` status `ready` deltaP `0.3041` edge `0.0038` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8317` n `193` status `ready` deltaP `-0.432` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8892` n `193` status `ready` deltaP `0.1343` edge `0.0339` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8897` n `193` status `ready` deltaP `-1.2263` edge `0.0298` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0901` n `193` status `ready` deltaP `0.0287` edge `0.0011` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1659` n `193` status `ready` deltaP `4.6687` edge `0.0053` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.4144` n `193` status `ready` deltaP `8.7933` edge `0.0927` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4162` n `193` status `ready` deltaP `-11.1414` edge `-0.0144` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2017` n `193` status `ready` deltaP `-14.1563` edge `-0.1098` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T03:22:21.362072+00:00`
- Price records: `672`
- Market context records: `1384`
- Flow alert records: `5898`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2151` n `153` status `ready` deltaP `29.4526` edge `1.0181` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.8067` n `153` status `ready` deltaP `12.7656` edge `1.0655` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3995` n `153` status `ready` deltaP `28.7684` edge `0.9598` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1285` n `153` status `ready` deltaP `20.7108` edge `0.3146` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.596` n `153` status `ready` deltaP `13.8481` edge `0.3567` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6612` n `181` status `ready` deltaP `8.6739` edge `0.1636` maxDD `-3.6396`
- `market_context_high->index_1h` score `0.0131` n `193` status `ready` deltaP `4.7253` edge `0.0161` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.0084` n `153` status `ready` deltaP `9.1809` edge `0.043` maxDD `-1.3925`
- `market_context_high->metal_4h` score `-0.0225` n `181` status `ready` deltaP `11.0589` edge `0.0675` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.0308` n `193` status `ready` deltaP `3.2972` edge `0.0313` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3614` n `193` status `ready` deltaP `2.8265` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4965` n `181` status `ready` deltaP `0.7681` edge `0.0624` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5129` n `193` status `ready` deltaP `5.6933` edge `0.0011` maxDD `-4.0518`
- `market_context_high->crypto_alt_1h` score `-0.5198` n `193` status `ready` deltaP `1.836` edge `0.0315` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8201` n `193` status `ready` deltaP `-1.0882` edge `0.0004` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.2228` n `181` status `ready` deltaP `8.1239` edge `0.1759` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.294` n `193` status `ready` deltaP `-0.8121` edge `0.0041` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2951` n `181` status `ready` deltaP `4.5243` edge `0.1328` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.8457` n `181` status `ready` deltaP `-6.6972` edge `-0.0121` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.3063` n `181` status `ready` deltaP `4.1445` edge `-0.2244` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

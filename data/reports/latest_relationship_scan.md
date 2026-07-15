# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T00:07:24.051196+00:00`
- Price records: `672`
- Market context records: `6762`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `1.0558` n `176` status `ready` deltaP `0.5366` edge `0.507` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0505` n `176` status `ready` deltaP `7.3524` edge `0.0305` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.0586` n `176` status `ready` deltaP `7.9704` edge `0.1288` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.1855` n `176` status `ready` deltaP `5.049` edge `0.0273` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3719` n `176` status `ready` deltaP `0.034` edge `0.0006` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5775` n `176` status `ready` deltaP `0.296` edge `-0.0077` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5991` n `176` status `ready` deltaP `-0.8676` edge `0.0004` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7245` n `176` status `ready` deltaP `-5.4403` edge `-0.0041` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1232` n `176` status `ready` deltaP `3.5554` edge `-0.0146` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.1995` n `176` status `ready` deltaP `7.8437` edge `0.0003` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2397` n `176` status `ready` deltaP `6.2916` edge `-0.0129` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4046` n `176` status `ready` deltaP `-1.4689` edge `-0.0213` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7777` n `176` status `ready` deltaP `-7.0257` edge `-0.0112` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.5574` n `176` status `ready` deltaP `3.5061` edge `-0.0198` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.6783` n `176` status `ready` deltaP `2.5221` edge `-0.02` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6999` n `176` status `ready` deltaP `-6.9291` edge `-0.0139` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.5517` n `176` status `ready` deltaP `-15.2578` edge `0.0423` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2198` n `176` status `ready` deltaP `2.7023` edge `-0.1321` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2325` n `176` status `ready` deltaP `-7.1812` edge `-0.0012` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.5112` n `176` status `ready` deltaP `-13.81` edge `-0.1506` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

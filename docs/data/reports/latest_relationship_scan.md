# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T11:07:36.768322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.1068` n `81` status `ready` deltaP `1.9483` edge `0.8019` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.855` n `81` status `ready` deltaP `13.6574` edge `0.2878` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7139` n `81` status `ready` deltaP `33.6034` edge `0.0657` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.43` n `103` status `ready` deltaP `13.5241` edge `0.0963` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1736` n `81` status `ready` deltaP `7.0216` edge `0.2023` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9926` n `103` status `ready` deltaP `11.5371` edge `0.0401` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.4041` n `103` status `ready` deltaP `4.0478` edge `0.0222` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5772` n `103` status `ready` deltaP `-0.5091` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6732` n `103` status `ready` deltaP `-4.6087` edge `-0.006` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8773` n `103` status `ready` deltaP `1.0226` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7389` n `103` status `ready` deltaP `4.1129` edge `-0.0386` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8331` n `103` status `ready` deltaP `-9.9805` edge `-0.0233` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3571` n `103` status `ready` deltaP `-6.9865` edge `-0.0502` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6575` n `81` status `ready` deltaP `6.6937` edge `-0.1359` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.8037` n `81` status `ready` deltaP `-23.1674` edge `-0.1889` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.8951` n `103` status `ready` deltaP `-9.3595` edge `-0.097` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.5554` n `103` status `ready` deltaP `-11.9672` edge `-0.2107` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

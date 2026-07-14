# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T06:31:12.316591+00:00`
- Price records: `672`
- Market context records: `6683`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.3808` n `198` status `ready` deltaP `-5.1443` edge `0.3228` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.9977` n `198` status `ready` deltaP `11.6951` edge `0.192` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1348` n `198` status `ready` deltaP `8.3046` edge `0.0479` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0155` n `198` status `ready` deltaP `5.3862` edge `0.0418` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.0048` n `198` status `ready` deltaP `-3.0146` edge `0.3947` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2475` n `198` status `ready` deltaP `2.5645` edge `0.0014` maxDD `-0.6845`
- `market_context_high->unknown_4h` score `-0.3478` n `198` status `ready` deltaP `-14.0568` edge `0.3053` maxDD `-10.5788`
- `market_context_high->index_1h` score `-0.5138` n `198` status `ready` deltaP `0.3372` edge `0.0033` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.5797` n `198` status `ready` deltaP `0.2979` edge `-0.008` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6314` n `198` status `ready` deltaP `-4.2642` edge `0.0` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.869` n `198` status `ready` deltaP `10.7492` edge `0.0049` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9262` n `198` status `ready` deltaP `3.3479` edge `0.0032` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3686` n `198` status `ready` deltaP `6.8782` edge `-0.0001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4123` n `198` status `ready` deltaP `9.0432` edge `0.0901` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.5287` n `198` status `ready` deltaP `-2.2666` edge `-0.0314` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6911` n `198` status `ready` deltaP `6.4609` edge `0.0803` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1406` n `198` status `ready` deltaP `-1.4689` edge `0.0214` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1724` n `198` status `ready` deltaP `7.8899` edge `-0.0324` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.0173` n `198` status `ready` deltaP `-11.7266` edge `-0.0104` maxDD `-10.0291`
- `market_context_high->metal_24h` score `-6.9936` n `198` status `ready` deltaP `-6.3289` edge `-0.0059` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T18:23:57.990492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8604`

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

- `market_context_high->unknown_24h` score `1211.7003` n `148` status `ready` deltaP `-2.135` edge `101.082` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.8436` n `149` status `ready` deltaP `4.385` edge `1.8063` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.4908` n `148` status `ready` deltaP `24.4088` edge `0.0303` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1865` n `149` status `ready` deltaP `7.4187` edge `0.0019` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0816` n `149` status `ready` deltaP `8.4767` edge `0.0077` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1552` n `149` status `ready` deltaP `6.4669` edge `0.0038` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3328` n `149` status `ready` deltaP `6.83` edge `0.0401` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4088` n `148` status `ready` deltaP `13.7951` edge `0.0312` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4416` n `149` status `ready` deltaP `6.8966` edge `0.0391` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6213` n `149` status `ready` deltaP `-0.0412` edge `0.0069` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7344` n `149` status `ready` deltaP `-3.4743` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7427` n `149` status `ready` deltaP `9.0563` edge `-0.0015` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3984` n `149` status `ready` deltaP `1.0891` edge `0.0047` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.519` n `149` status `ready` deltaP `3.1949` edge `0.0203` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.7317` n `148` status `ready` deltaP `6.9585` edge `0.0224` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0784` n `149` status `ready` deltaP `-9.6364` edge `-0.0301` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2026` n `148` status `ready` deltaP `1.0229` edge `0.0683` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.3848` n `148` status `ready` deltaP `0.108` edge `0.0192` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.4026` n `149` status `ready` deltaP `3.6616` edge `-0.0287` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3833` n `149` status `ready` deltaP `-3.6299` edge `-0.1426` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

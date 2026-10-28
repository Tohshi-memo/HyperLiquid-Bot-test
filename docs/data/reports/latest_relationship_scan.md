# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T23:52:25.128631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8273`

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

- `market_context_high->unknown_24h` score `1253.0343` n `148` status `ready` deltaP `-2.135` edge `104.5265` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.456` n `149` status `ready` deltaP `4.385` edge `1.774` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.9393` n `148` status `ready` deltaP `20.5894` edge `0.0098` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2823` n `149` status `ready` deltaP `8.6163` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0115` n `149` status `ready` deltaP `8.1437` edge `0.0046` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1174` n `149` status `ready` deltaP `8.0276` edge `0.0061` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3694` n `149` status `ready` deltaP `6.5306` edge `0.0374` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3757` n `149` status `ready` deltaP `7.8112` edge `0.0385` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.5997` n `149` status `ready` deltaP `-0.0412` edge `0.0087` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7515` n `149` status `ready` deltaP `-3.7737` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.8324` n `148` status `ready` deltaP `10.1492` edge `0.0202` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8564` n `149` status `ready` deltaP `7.3795` edge `-0.0049` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4218` n `149` status `ready` deltaP `0.9394` edge `0.0027` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5845` n `149` status `ready` deltaP `2.7458` edge `0.0149` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0408` n `149` status `ready` deltaP `-9.3315` edge `-0.029` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3901` n `149` status `ready` deltaP `3.6616` edge `-0.0271` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5973` n `148` status `ready` deltaP `-0.2393` edge `0.0038` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.849` n `148` status `ready` deltaP `-2.7965` edge `0.0109` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.5792` n `148` status `ready` deltaP `3.139` edge `-0.1061` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4368` n `149` status `ready` deltaP `-4.0872` edge `-0.1464` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

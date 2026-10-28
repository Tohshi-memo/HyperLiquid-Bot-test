# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T22:22:25.194931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8464`

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

- `market_context_high->unknown_24h` score `1243.7991` n `148` status `ready` deltaP `-2.135` edge `103.7569` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.042` n `149` status `ready` deltaP `4.385` edge `1.7395` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.0886` n `148` status `ready` deltaP `21.631` edge `0.0153` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2081` n `149` status `ready` deltaP `7.7181` edge `0.0017` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0918` n `149` status `ready` deltaP `7.2291` edge `0.004` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1081` n `149` status `ready` deltaP `8.1773` edge `0.0063` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3265` n `149` status `ready` deltaP `7.8112` edge `0.0426` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3819` n `149` status `ready` deltaP `6.3809` edge `0.0368` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6464` n `149` status `ready` deltaP `-0.4903` edge `0.0078` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.7083` n `148` status `ready` deltaP `11.1909` edge `0.0236` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7414` n `149` status `ready` deltaP `-3.624` edge `-0.0026` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8785` n `149` status `ready` deltaP `7.0746` edge `-0.0057` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4062` n `149` status `ready` deltaP `0.9394` edge `0.0047` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.604` n `149` status `ready` deltaP `2.4464` edge `0.0144` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1356` n `149` status `ready` deltaP `-10.2462` edge `-0.0308` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4861` n `149` status `ready` deltaP `3.5092` edge `-0.0384` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5493` n `148` status `ready` deltaP `-0.2393` edge `0.0078` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.6279` n `148` status `ready` deltaP `-1.7549` edge `0.0323` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.0879` n `148` status `ready` deltaP `4.1807` edge `-0.0721` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5292` n `149` status `ready` deltaP `-4.5445` edge `-0.1552` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

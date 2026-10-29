# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T09:07:27.648917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8148`

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

- `market_context_high->unknown_24h` score `1270.7367` n `148` status `ready` deltaP `-2.135` edge `106.0017` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `27.1524` n `149` status `ready` deltaP `4.385` edge `2.2487` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5974` n `148` status `ready` deltaP `18.506` edge `-0.0048` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1578` n `149` status `ready` deltaP `7.1193` edge `0.0015` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1315` n `149` status `ready` deltaP `10.0978` edge `0.0436` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.149` n `149` status `ready` deltaP `6.6193` edge `0.0033` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1501` n `149` status `ready` deltaP `7.4288` edge `0.0059` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.459` n `149` status `ready` deltaP `5.333` edge `0.0339` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4655` n `149` status `ready` deltaP `1.4558` edge `0.0099` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8241` n `149` status `ready` deltaP `7.6844` edge `-0.0028` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8582` n `149` status `ready` deltaP `-5.5701` edge `-0.0046` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.3588` n `148` status `ready` deltaP `5.1145` edge `0.0099` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5581` n `149` status `ready` deltaP `-0.7073` edge `-0.0038` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6624` n `149` status `ready` deltaP `1.5482` edge `0.0129` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1596` n `149` status `ready` deltaP `-10.2462` edge `-0.0328` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3856` n `149` status `ready` deltaP `2.4421` edge `-0.0184` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.8034` n `148` status `ready` deltaP `-2.9701` edge `0.0179` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.8733` n `148` status `ready` deltaP `-0.2393` edge `-0.0192` maxDD `-10.1587`
- `market_context_high->equity_4h` score `-5.4863` n `149` status `ready` deltaP `-4.5445` edge `-0.1497` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.8271` n `148` status `ready` deltaP `2.271` edge `-0.2043` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

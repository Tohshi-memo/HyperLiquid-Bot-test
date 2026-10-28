# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T23:07:35.043185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8280`

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

- `market_context_high->unknown_24h` score `1246.3695` n `148` status `ready` deltaP `-2.135` edge `103.9711` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.1464` n `149` status `ready` deltaP `4.385` edge `1.7482` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.0145` n `148` status `ready` deltaP `21.1102` edge `0.0126` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2452` n `149` status `ready` deltaP `8.1672` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0517` n `149` status `ready` deltaP `7.6864` edge `0.0043` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.091` n `149` status `ready` deltaP `8.4767` edge `0.0065` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3531` n `149` status `ready` deltaP `6.6803` edge `0.0385` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3541` n `149` status `ready` deltaP `7.8112` edge `0.0403` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6344` n `149` status `ready` deltaP `-0.3406` edge `0.0078` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7328` n `149` status `ready` deltaP `-3.4743` edge `-0.0025` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.7704` n `148` status `ready` deltaP `10.6701` edge `0.0219` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8674` n `149` status `ready` deltaP `7.227` edge `-0.0053` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.389` n `149` status `ready` deltaP `1.2388` edge `0.0049` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5736` n `149` status `ready` deltaP `2.7458` edge `0.0163` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0882` n `149` status `ready` deltaP `-9.7889` edge `-0.0299` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4393` n `149` status `ready` deltaP `3.5092` edge `-0.0324` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5709` n `148` status `ready` deltaP `-0.2393` edge `0.006` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.7283` n `148` status `ready` deltaP `-2.2757` edge `0.0229` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.3276` n `148` status `ready` deltaP `3.6599` edge `-0.0886` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4775` n `149` status `ready` deltaP `-4.2396` edge `-0.1506` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

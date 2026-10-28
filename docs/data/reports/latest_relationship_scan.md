# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T19:07:32.019409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8626`

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

- `market_context_high->unknown_24h` score `1219.0023` n `148` status `ready` deltaP `-2.135` edge `101.6905` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.816` n `149` status `ready` deltaP `4.385` edge `1.804` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.4143` n `148` status `ready` deltaP `23.888` edge `0.0274` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1602` n `149` status `ready` deltaP `7.1193` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1003` n `149` status `ready` deltaP `8.1773` edge `0.0073` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1966` n `149` status `ready` deltaP `6.0096` edge `0.0034` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3788` n `149` status `ready` deltaP `6.3809` edge `0.0372` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4416` n `149` status `ready` deltaP `6.8966` edge `0.0391` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4684` n `148` status `ready` deltaP `13.2742` edge `0.0297` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6165` n `149` status `ready` deltaP `-0.0412` edge `0.0073` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7616` n `149` status `ready` deltaP `-3.9234` edge `-0.0032` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.764` n `149` status `ready` deltaP `8.7514` edge `-0.0022` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4514` n `149` status `ready` deltaP `0.64` edge `0.0009` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5689` n `149` status `ready` deltaP `2.7458` edge `0.0169` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.9953` n `148` status `ready` deltaP `6.4376` edge `0.0039` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.1234` n `149` status `ready` deltaP `-10.0937` edge `-0.0308` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2742` n `148` status `ready` deltaP `0.5021` edge `0.0626` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.4227` n `148` status `ready` deltaP `-0.0657` edge `0.0172` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.4362` n `149` status `ready` deltaP `3.5092` edge `-0.032` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4477` n `149` status `ready` deltaP `-4.0872` edge `-0.1478` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

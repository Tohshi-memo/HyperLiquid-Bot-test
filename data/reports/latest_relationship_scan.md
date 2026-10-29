# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T01:07:25.202015+00:00`
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

- `market_context_high->unknown_24h` score `1254.8979` n `148` status `ready` deltaP `-2.135` edge `104.6818` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1292` n `149` status `ready` deltaP `4.385` edge `1.8301` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.8038` n `148` status `ready` deltaP `19.7213` edge `0.0043` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3123` n `149` status `ready` deltaP `8.9157` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0335` n `149` status `ready` deltaP `8.601` edge `0.0053` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1073` n `149` status `ready` deltaP `8.1773` edge `0.0064` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3429` n `149` status `ready` deltaP `6.6803` edge `0.0398` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3875` n `149` status `ready` deltaP `7.9637` edge `0.0365` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6237` n `149` status `ready` deltaP `-0.1909` edge `0.0077` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7788` n `149` status `ready` deltaP `-4.2228` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8374` n `149` status `ready` deltaP `7.6844` edge `-0.0045` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.9307` n `148` status `ready` deltaP `9.2812` edge `0.0178` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.4607` n `149` status `ready` deltaP `0.4903` edge `0.0007` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5658` n `149` status `ready` deltaP `2.7458` edge `0.0173` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0396` n `149` status `ready` deltaP `-9.3315` edge `-0.0289` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3421` n `149` status `ready` deltaP `4.119` edge `-0.024` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.6573` n `148` status `ready` deltaP `-0.2393` edge `-0.0012` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-4.1156` n `148` status `ready` deltaP `-3.6646` edge `-0.0175` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-5.1203` n `148` status `ready` deltaP `2.271` edge `-0.1454` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4273` n `149` status `ready` deltaP `-3.9347` edge `-0.1462` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

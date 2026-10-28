# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T20:22:31.814585+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8400`

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

- `market_context_high->unknown_24h` score `1230.5823` n `148` status `ready` deltaP `-2.135` edge `102.6555` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.468` n `149` status `ready` deltaP `4.385` edge `1.775` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.2849` n `148` status `ready` deltaP `23.0199` edge `0.0224` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1602` n `149` status `ready` deltaP `7.1193` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1143` n `149` status `ready` deltaP `8.0276` edge `0.0065` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1966` n `149` status `ready` deltaP `6.0096` edge `0.0034` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.4102` n `149` status `ready` deltaP `7.049` edge `0.0407` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4154` n `149` status `ready` deltaP `6.0815` edge `0.0345` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.5655` n `148` status `ready` deltaP `12.4062` edge `0.0274` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5961` n `149` status `ready` deltaP `0.1085` edge `0.008` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7873` n `149` status `ready` deltaP `-4.3725` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8153` n `149` status `ready` deltaP `7.9892` edge `-0.0037` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4584` n `149` status `ready` deltaP `0.64` edge `0.0` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6484` n `149` status `ready` deltaP `2.147` edge `0.0107` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1659` n `149` status `ready` deltaP `-10.5511` edge `-0.0313` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.4004` n `148` status `ready` deltaP `-0.366` edge `0.0522` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-3.4452` n `148` status `ready` deltaP `5.5696` edge `-0.0278` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.4659` n `149` status `ready` deltaP `3.5092` edge `-0.0358` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.4857` n `148` status `ready` deltaP `-0.2393` edge `0.0131` maxDD `-10.1587`
- `market_context_high->equity_4h` score `-5.5231` n `149` status `ready` deltaP `-4.6969` edge `-0.1534` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

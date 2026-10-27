# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T21:52:28.691292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8673`

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

- `market_context_high->unknown_4h` score `51.4055` n `147` status `ready` deltaP `5.0285` edge `4.2655` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9555` n `135` status `ready` deltaP `27.1875` edge `0.0505` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3936` n `148` status `ready` deltaP `9.8276` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1085` n `147` status `ready` deltaP `8.9835` edge `0.009` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.1058` n `147` status `ready` deltaP `8.9493` edge `0.0534` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1286` n `148` status `ready` deltaP `7.7237` edge `0.0067` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3845` n `148` status `ready` deltaP `7.3515` edge `0.03` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4587` n `135` status `ready` deltaP `11.3889` edge `0.0225` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6022` n `148` status `ready` deltaP `-0.0728` edge `0.0087` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6498` n `148` status `ready` deltaP `-1.7276` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7802` n `147` status `ready` deltaP `8.7834` edge `-0.0045` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.2954` n `135` status `ready` deltaP `13.1481` edge `0.0822` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4274` n `148` status `ready` deltaP `1.942` edge `-0.0047` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.4814` n `135` status `ready` deltaP `8.0671` edge `0.1192` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6883` n `148` status `ready` deltaP `2.6096` edge `0.0025` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9679` n `147` status `ready` deltaP `-7.7755` edge `-0.0333` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7601` n `147` status `ready` deltaP `3.73` edge `-0.075` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.765` n `135` status `ready` deltaP `0.544` edge `-0.0006` maxDD `-29.1905`
- `market_context_high->unknown_1h` score `-4.5738` n `148` status `ready` deltaP `0.2509` edge `-0.3339` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.6424` n `147` status `ready` deltaP `-2.6859` edge `-0.1821` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

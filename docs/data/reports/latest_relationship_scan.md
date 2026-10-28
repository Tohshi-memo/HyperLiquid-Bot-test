# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T08:37:32.599484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8795`

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

- `market_context_high->unknown_24h` score `1320.5974` n `135` status `ready` deltaP `-3.7616` edge `110.1676` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `42.2112` n `148` status `ready` deltaP `5.2406` edge `3.4979` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8319` n `135` status `ready` deltaP `27.1875` edge `0.0402` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.293` n `148` status `ready` deltaP `8.63` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1237` n `148` status `ready` deltaP `9.3688` edge `0.0077` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0966` n `148` status `ready` deltaP `8.1728` edge `0.0078` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.34` n `148` status `ready` deltaP `7.3515` edge `0.0357` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4335` n `135` status `ready` deltaP `12.0833` edge `0.0211` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5264` n `148` status `ready` deltaP `5.8668` edge `0.0389` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6707` n `148` status `ready` deltaP `10.0198` edge `0.0013` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6969` n `148` status `ready` deltaP `-0.8213` edge `0.0058` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7424` n `148` status `ready` deltaP `-3.524` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.5441` n `148` status `ready` deltaP `-0.1538` edge `-0.0057` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5893` n `148` status `ready` deltaP `2.909` edge `0.0132` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.7466` n `135` status `ready` deltaP `8.0671` edge `0.0971` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.0584` n `135` status `ready` deltaP `7.7662` edge `0.0545` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0888` n `148` status `ready` deltaP `-9.5419` edge `-0.0316` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.194` n `135` status `ready` deltaP `0.544` edge `0.0726` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5076` n `148` status `ready` deltaP `3.5761` edge `-0.0416` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.709` n `148` status `ready` deltaP `-4.8368` edge `-0.1763` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T02:07:31.036801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8775`

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

- `market_context_high->unknown_24h` score `903.8638` n `135` status `ready` deltaP `-3.7616` edge `75.4398` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.521` n `148` status `ready` deltaP `5.0882` edge `3.9414` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9315` n `135` status `ready` deltaP `27.1875` edge `0.0485` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2894` n `148` status `ready` deltaP `8.63` edge `0.0024` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.087` n `148` status `ready` deltaP `8.7591` edge `0.0087` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1473` n `148` status `ready` deltaP `7.4243` edge `0.0063` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.2407` n `148` status `ready` deltaP `7.8485` edge `0.0495` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.372` n `135` status `ready` deltaP `12.9514` edge `0.0232` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4546` n `148` status `ready` deltaP `6.603` edge `0.026` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5579` n `148` status `ready` deltaP `0.3763` edge `0.0094` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7401` n `148` status `ready` deltaP `-3.2246` edge `-0.0051` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8355` n `148` status `ready` deltaP `7.8856` edge `-0.0056` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.1478` n `135` status `ready` deltaP `8.0671` edge `0.147` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5777` n `148` status `ready` deltaP `0.445` edge `-0.014` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6652` n `135` status `ready` deltaP `10.3704` edge `0.0699` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.781` n `148` status `ready` deltaP `1.7114` edge `-0.0034` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0528` n `148` status `ready` deltaP `-8.6273` edge `-0.0347` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.5099` n `135` status `ready` deltaP `0.544` edge `0.0321` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7169` n `148` status `ready` deltaP `3.2713` edge `-0.0664` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7768` n `148` status `ready` deltaP `-3.9222` edge `-0.1911` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

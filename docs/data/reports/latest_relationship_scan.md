# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T22:07:26.416083+00:00`
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

- `market_context_high->unknown_4h` score `49.3882` n `148` status `ready` deltaP `5.0882` edge `4.097` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9543` n `135` status `ready` deltaP `27.1875` edge `0.0504` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3816` n `148` status `ready` deltaP `9.6779` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0772` n `148` status `ready` deltaP `8.6066` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0757` n `148` status `ready` deltaP `9.2205` edge `0.0541` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1286` n `148` status `ready` deltaP `7.7237` edge `0.0067` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3969` n `148` status `ready` deltaP `7.2018` edge `0.0294` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4587` n `135` status `ready` deltaP `11.3889` edge `0.0225` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5878` n `148` status `ready` deltaP `0.0769` edge `0.0089` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6498` n `148` status `ready` deltaP `-1.7276` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7683` n `148` status `ready` deltaP `8.9527` edge `-0.0041` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.3177` n `135` status `ready` deltaP `12.9745` edge `0.0815` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4359` n `148` status `ready` deltaP `1.7923` edge `-0.0048` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.4562` n `135` status `ready` deltaP `8.0671` edge `0.1213` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.7` n `148` status `ready` deltaP `2.4599` edge `0.002` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9495` n `148` status `ready` deltaP `-7.5602` edge `-0.0332` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7484` n `148` status `ready` deltaP `3.881` edge `-0.0745` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.7603` n `135` status `ready` deltaP `0.544` edge `0.0` maxDD `-29.1905`
- `market_context_high->unknown_1h` score `-4.5774` n `148` status `ready` deltaP `0.2509` edge `-0.3342` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.6606` n `148` status `ready` deltaP `-3.0076` edge `-0.1823` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

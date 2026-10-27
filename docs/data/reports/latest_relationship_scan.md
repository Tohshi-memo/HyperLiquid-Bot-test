# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T20:23:10.508422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8684`

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

- `market_context_high->unknown_4h` score `65.4169` n `141` status `ready` deltaP `4.9569` edge `5.4336` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9651` n `135` status `ready` deltaP `27.1875` edge `0.0513` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3804` n `148` status `ready` deltaP `9.6779` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.2848` n `141` status `ready` deltaP `11.0523` edge `0.0099` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1216` n `148` status `ready` deltaP `7.8734` edge `0.0066` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3012` n `141` status `ready` deltaP `7.2414` edge `0.0485` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.365` n `148` status `ready` deltaP `7.5012` edge `0.0315` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4798` n `135` status `ready` deltaP `11.0417` edge `0.0221` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6022` n `148` status `ready` deltaP `-0.0728` edge `0.0087` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6763` n `148` status `ready` deltaP `-2.1767` edge `-0.0039` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8529` n `141` status `ready` deltaP `7.6717` edge `-0.0064` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1701` n `135` status `ready` deltaP `14.1898` edge `0.0857` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4632` n `148` status `ready` deltaP `1.4929` edge `-0.0063` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6206` n `135` status `ready` deltaP `8.0671` edge `0.1076` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6867` n `148` status `ready` deltaP `2.4599` edge `0.0037` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9981` n `141` status `ready` deltaP `-8.063` edge `-0.0339` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7626` n `141` status `ready` deltaP `3.8477` edge `-0.0761` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.7704` n `135` status `ready` deltaP `0.544` edge `-0.0013` maxDD `-29.1905`
- `market_context_high->unknown_1h` score `-4.6998` n `148` status `ready` deltaP `0.2509` edge `-0.3444` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.5066` n `141` status `ready` deltaP `-0.6595` edge `-0.1782` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

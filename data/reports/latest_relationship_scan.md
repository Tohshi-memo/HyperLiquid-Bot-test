# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T06:22:26.288112+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7786`

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

- `market_context_high->unknown_4h` score `50.0656` n `97` status `ready` deltaP `0.3096` edge `4.2036` maxDD `-1.016`
- `market_context_high->unknown_1h` score `16.6723` n `109` status `ready` deltaP `3.9375` edge `1.412` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `11.6469` n `35` status `ready` deltaP `31.7361` edge `0.8198` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `3.3893` n `35` status `ready` deltaP `20.2926` edge `0.2531` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.5895` n `35` status `ready` deltaP `12.1627` edge `0.0854` maxDD `-3.6055`
- `market_context_high->fx_24h` score `-0.0219` n `35` status `ready` deltaP `9.7917` edge `0.0061` maxDD `-0.9352`
- `market_context_high->fx_1h` score `-0.1256` n `109` status `ready` deltaP `2.3856` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1768` n `97` status `ready` deltaP `4.3625` edge `0.0081` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4545` n `109` status `ready` deltaP `-2.2359` edge `0.0067` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5751` n `109` status `ready` deltaP `-0.5164` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6095` n `109` status `ready` deltaP `4.9497` edge `-0.0046` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9566` n `97` status `ready` deltaP `-4.9723` edge `0.0334` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.2863` n `109` status `ready` deltaP `2.8004` edge `-0.0255` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9094` n `97` status `ready` deltaP `5.1892` edge `-0.0227` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0071` n `97` status `ready` deltaP `-4.603` edge `-0.0392` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.3336` n `35` status `ready` deltaP `-2.6637` edge `-0.0374` maxDD `-6.1446`
- `market_context_high->equity_1h` score `-2.3531` n `109` status `ready` deltaP `1.898` edge `-0.087` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.7876` n `109` status `ready` deltaP `-0.3667` edge `-0.0508` maxDD `-11.3243`
- `market_context_high->crypto_major_4h` score `-5.7168` n `97` status `ready` deltaP `-8.2694` edge `-0.1781` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.6079` n `35` status `ready` deltaP `-32.7778` edge `-0.202` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

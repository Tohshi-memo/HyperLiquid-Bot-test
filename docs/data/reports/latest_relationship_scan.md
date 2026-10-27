# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T20:07:29.835286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8708`

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

- `market_context_high->unknown_4h` score `67.8993` n `140` status `ready` deltaP `4.8911` edge `5.6409` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9675` n `135` status `ready` deltaP `27.1875` edge `0.0515` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3804` n `148` status `ready` deltaP `9.6779` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.318` n `140` status `ready` deltaP `11.4677` edge `0.0099` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1122` n `148` status `ready` deltaP `8.0231` edge `0.0068` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3336` n `140` status `ready` deltaP `6.9425` edge `0.0478` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3533` n `148` status `ready` deltaP `7.6509` edge `0.032` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4806` n `135` status `ready` deltaP `11.0417` edge `0.022` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5998` n `148` status `ready` deltaP `-0.0728` edge `0.0089` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6763` n `148` status `ready` deltaP `-2.1767` edge `-0.0039` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8657` n `140` status `ready` deltaP `7.4695` edge `-0.0067` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1478` n `135` status `ready` deltaP `14.3634` edge `0.0864` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.464` n `148` status `ready` deltaP `1.4929` edge `-0.0064` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.635` n `135` status `ready` deltaP `8.0671` edge `0.1064` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6859` n `148` status `ready` deltaP `2.4599` edge `0.0038` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.969` n `140` status `ready` deltaP `-7.7439` edge `-0.0336` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7673` n `135` status `ready` deltaP `0.544` edge `-0.0009` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7754` n `140` status `ready` deltaP `3.6759` edge `-0.0766` maxDD `-27.2215`
- `market_context_high->unknown_1h` score `-4.6687` n `148` status `ready` deltaP `0.4006` edge `-0.3428` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.4819` n `140` status `ready` deltaP `-0.3049` edge `-0.1774` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

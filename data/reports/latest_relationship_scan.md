# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T08:52:23.857610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9426`

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

- `market_context_high->unknown_4h` score `87.2823` n `135` status `ready` deltaP `5.0045` edge `7.2554` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `22.5143` n `135` status `ready` deltaP `1.8175` edge `1.913` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.7405` n `123` status `ready` deltaP `25.8951` edge `0.0412` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4847` n `135` status `ready` deltaP `10.906` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1192` n `135` status `ready` deltaP `11.6933` edge `0.012` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3321` n `135` status `ready` deltaP `1.8286` edge `0.0102` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5043` n `135` status `ready` deltaP `5.2872` edge `0.0284` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5383` n `135` status `ready` deltaP `0.0865` edge `-0.0013` maxDD `-1.4631`
- `market_context_high->metal_24h` score `-0.5597` n `123` status `ready` deltaP `16.0658` edge `0.0988` maxDD `-6.204`
- `market_context_high->fx_24h` score `-0.6112` n `123` status `ready` deltaP `8.7712` edge `0.0204` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.6324` n `135` status `ready` deltaP `4.7075` edge `0.0378` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6438` n `135` status `ready` deltaP `10.1479` edge `0.0039` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.324` n `135` status `ready` deltaP `2.6391` edge `0.0039` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.942` n `123` status `ready` deltaP `4.9428` edge `0.0145` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9888` n `135` status `ready` deltaP `-1.4904` edge `-0.0087` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.4826` n `135` status `ready` deltaP `-3.269` edge `-0.0229` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.6577` n `135` status `ready` deltaP `3.6597` edge `-0.0614` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6162` n `123` status `ready` deltaP `-0.6003` edge `-0.1021` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7123` n `135` status `ready` deltaP `3.9194` edge `-0.1069` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

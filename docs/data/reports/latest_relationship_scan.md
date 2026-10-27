# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T08:37:28.845614+00:00`
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

- `market_context_high->unknown_4h` score `87.2631` n `135` status `ready` deltaP `5.0045` edge `7.2538` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `26.0951` n `135` status `ready` deltaP `1.8175` edge `2.2114` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.7085` n `122` status `ready` deltaP `25.7352` edge `0.0396` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4727` n `135` status `ready` deltaP `10.7563` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1106` n `135` status `ready` deltaP `11.5436` edge `0.0119` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3177` n `135` status `ready` deltaP `1.9783` edge `0.0104` maxDD `-1.0053`
- `market_context_high->metal_24h` score `-0.3347` n `122` status `ready` deltaP `16.2656` edge `0.1012` maxDD `-6.204`
- `market_context_high->crypto_major_1h` score `-0.5043` n `135` status `ready` deltaP `5.2872` edge `0.0284` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5297` n `135` status `ready` deltaP `0.2362` edge `-0.0012` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5965` n `122` status `ready` deltaP `9.0377` edge `0.0205` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.6082` n `135` status `ready` deltaP `4.86` edge `0.0388` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6469` n `135` status `ready` deltaP `10.1479` edge `0.0035` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.31` n `135` status `ready` deltaP `2.7888` edge `0.0047` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.977` n `122` status `ready` deltaP `4.6296` edge `0.0121` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9873` n `135` status `ready` deltaP `-1.4904` edge `-0.0085` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.4838` n `135` status `ready` deltaP `-3.269` edge `-0.023` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.668` n `135` status `ready` deltaP `3.5072` edge `-0.0617` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6135` n `122` status `ready` deltaP `-0.3538` edge `-0.1034` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7139` n `135` status `ready` deltaP `3.9194` edge `-0.1071` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

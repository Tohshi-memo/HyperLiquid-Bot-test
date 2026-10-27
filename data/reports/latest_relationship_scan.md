# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T08:07:35.078162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9462`

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

- `market_context_high->unknown_4h` score `87.2753` n `135` status `ready` deltaP `5.157` edge `7.2538` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `26.0747` n `135` status `ready` deltaP `1.6678` edge `2.2107` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.6704` n `120` status `ready` deltaP `25.7539` edge `0.0363` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4727` n `135` status `ready` deltaP `10.7563` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4493` n `135` status `ready` deltaP `13.0488` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1013` n `135` status `ready` deltaP `11.3939` edge `0.0117` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.2771` n `120` status `ready` deltaP `16.684` edge `0.1058` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.3177` n `135` status `ready` deltaP `1.9783` edge `0.0104` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4903` n `135` status `ready` deltaP `5.4369` edge `0.0292` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5134` n `135` status `ready` deltaP `0.5356` edge `-0.0011` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5638` n `120` status `ready` deltaP `9.5927` edge `0.021` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5646` n `135` status `ready` deltaP `5.1648` edge `0.0404` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6539` n `135` status `ready` deltaP `10.1479` edge `0.0026` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.2796` n `135` status `ready` deltaP `3.0882` edge `0.0066` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9701` n `135` status `ready` deltaP `-1.3407` edge `-0.0073` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.0649` n `120` status `ready` deltaP `4.3342` edge `0.0028` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.4704` n `135` status `ready` deltaP `-3.1166` edge `-0.0229` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.6577` n `135` status `ready` deltaP `3.6597` edge `-0.0614` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6928` n `120` status `ready` deltaP `-0.4997` edge `-0.1126` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.717` n `135` status `ready` deltaP `3.9194` edge `-0.1075` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

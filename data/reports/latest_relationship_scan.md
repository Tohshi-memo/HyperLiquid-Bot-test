# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T14:37:28.955357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8487`

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

- `market_context_high->unknown_24h` score `1513.6774` n `135` status `ready` deltaP `-3.7616` edge `126.2576` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1616` n `149` status `ready` deltaP `4.385` edge `1.8328` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5094` n `135` status `ready` deltaP `25.4514` edge `0.0249` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2009` n `149` status `ready` deltaP `7.5684` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0381` n `149` status `ready` deltaP `8.4486` edge `0.0067` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0801` n `149` status `ready` deltaP `8.4767` edge `0.0079` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2705` n `149` status `ready` deltaP `7.7282` edge `0.0421` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.375` n `149` status `ready` deltaP `7.3539` edge `0.0416` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5408` n `135` status `ready` deltaP `10.6945` edge `0.0166` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7027` n `149` status `ready` deltaP `-0.9394` edge `0.0061` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7118` n `149` status `ready` deltaP `-3.0252` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7229` n `149` status `ready` deltaP `9.3612` edge `-0.001` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3789` n `149` status `ready` deltaP `1.3885` edge `0.0052` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5221` n `149` status `ready` deltaP `3.1949` edge `0.0199` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.5967` n `135` status `ready` deltaP `3.9468` edge `0.0351` maxDD `-8.2244`
- `market_context_high->index_4h` score `-2.9726` n `149` status `ready` deltaP `-8.5693` edge `-0.0284` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-3.002` n `135` status `ready` deltaP `6.5046` edge `0.0029` maxDD `-15.7143`
- `market_context_high->crypto_major_24h` score `-3.3048` n `135` status `ready` deltaP `0.544` edge `0.0584` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4555` n `149` status `ready` deltaP `3.8141` edge `-0.0365` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.358` n `149` status `ready` deltaP `-3.1725` edge `-0.1424` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

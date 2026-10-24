# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T22:22:30.217936+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `20.3205` n `99` status `ready` deltaP `-0.194` edge `1.7282` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.8633` n `65` status `ready` deltaP `24.6421` edge `0.0819` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `1.0499` n `99` status `ready` deltaP `13.4285` edge `0.0542` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.2549` n `107` status `ready` deltaP `8.6113` edge `0.0139` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2074` n `107` status `ready` deltaP `0.957` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.4615` n `99` status `ready` deltaP `-0.6206` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.2492` n `107` status `ready` deltaP `-2.7408` edge `-0.0064` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.54` n `65` status `ready` deltaP `-8.6698` edge `-0.0042` maxDD `-1.9736`
- `market_context_high->crypto_major_1h` score `-3.2743` n `107` status `ready` deltaP `-4.8044` edge `-0.0609` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.6005` n `99` status `ready` deltaP `-12.229` edge `-0.0312` maxDD `-5.985`
- `market_context_high->metal_24h` score `-3.9962` n `65` status `ready` deltaP `-13.2131` edge `0.0183` maxDD `-7.7251`
- `market_context_high->equity_1h` score `-4.1267` n `107` status `ready` deltaP `-1.9195` edge `-0.0982` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.3062` n `107` status `ready` deltaP `-6.5561` edge `-0.0833` maxDD `-15.214`
- `market_context_high->crypto_major_24h` score `-4.7046` n `65` status `ready` deltaP `-8.1624` edge `-0.1796` maxDD `-23.1975`
- `market_context_high->index_4h` score `-5.1399` n `99` status `ready` deltaP `-26.3304` edge `-0.0525` maxDD `-5.3565`
- `market_context_high->index_24h` score `-8.2496` n `65` status `ready` deltaP `-38.0155` edge `-0.1693` maxDD `-7.5114`
- `market_context_high->crypto_alt_24h` score `-13.1238` n `65` status `ready` deltaP `-5.187` edge `-0.5754` maxDD `-75.1382`
- `market_context_high->crypto_major_4h` score `-15.7475` n `99` status `ready` deltaP `-29.0558` edge `-0.3944` maxDD `-47.6015`
- `market_context_high->equity_4h` score `-17.4194` n `99` status `ready` deltaP `-25.5682` edge `-0.4858` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

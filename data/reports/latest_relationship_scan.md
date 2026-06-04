# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T21:37:20.718588+00:00`
- Price records: `672`
- Market context records: `2905`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `11.5079` n `142` status `ready` deltaP `11.0354` edge `1.2771` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.13` n `142` status `ready` deltaP `12.901` edge `0.6252` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.355` n `142` status `ready` deltaP `11.2822` edge `0.4175` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2006` n `142` status `ready` deltaP `10.2382` edge `0.2132` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7676` n `142` status `ready` deltaP `15.5516` edge `0.353` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4673` n `142` status `ready` deltaP `13.1484` edge `0.0564` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.1181` n `142` status `ready` deltaP `5.9258` edge `0.1083` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1061` n `142` status `ready` deltaP `4.6612` edge `0.0831` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0586` n `142` status `ready` deltaP `3.8986` edge `0.0159` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.293` n `142` status `ready` deltaP `4.3308` edge `0.0198` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.5177` n `142` status `ready` deltaP `14.7951` edge `0.2923` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-0.5262` n `142` status `ready` deltaP `-0.3542` edge `0.0418` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5416` n `142` status `ready` deltaP `5.695` edge `0.0686` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6132` n `142` status `ready` deltaP `-0.7316` edge `0.0016` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6567` n `142` status `ready` deltaP `5.8721` edge `0.0636` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6723` n `142` status `ready` deltaP `-0.3163` edge `0.0005` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0701` n `142` status `ready` deltaP `-2.6859` edge `0.0066` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1946` n `142` status `ready` deltaP `2.9049` edge `0.0195` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2948` n `142` status `ready` deltaP `-1.7116` edge `-0.0093` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

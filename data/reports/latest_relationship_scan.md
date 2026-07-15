# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T11:00:56.677132+00:00`
- Price records: `672`
- Market context records: `6810`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8273` n `176` status `ready` deltaP `-1.5467` edge `0.4916` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.394` n `176` status `ready` deltaP `10.7481` edge `0.148` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3574` n `192` status `ready` deltaP `5.9257` edge `0.0167` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4591` n `192` status `ready` deltaP `-1.4783` edge `-0.0005` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4713` n `192` status `ready` deltaP `3.1718` edge `0.016` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6523` n `192` status `ready` deltaP `-1.2038` edge `-0.0073` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7258` n `192` status `ready` deltaP `-2.7601` edge `-0.0018` maxDD `-0.8285`
- `market_context_high->metal_1h` score `-0.8968` n `192` status `ready` deltaP `-6.6804` edge `-0.0065` maxDD `-1.7817`
- `market_context_high->fx_4h` score `-1.3556` n `185` status `ready` deltaP `5.2175` edge `-0.0022` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3782` n `185` status `ready` deltaP `-2.4456` edge `-0.0114` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.4051` n `192` status `ready` deltaP `1.4658` edge `-0.0198` maxDD `-4.2318`
- `market_context_high->index_4h` score `-1.657` n `185` status `ready` deltaP `1.8375` edge `-0.0287` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.7897` n `192` status `ready` deltaP `-6.8301` edge `-0.0135` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8453` n `185` status `ready` deltaP `-6.0094` edge `-0.0264` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2964` n `185` status `ready` deltaP `-0.81` edge `-0.0845` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.5013` n `185` status `ready` deltaP `-14.1175` edge `0.0389` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5019` n `185` status `ready` deltaP `-1.517` edge `-0.0805` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.484` n `176` status `ready` deltaP `-9.7853` edge `-0.0048` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0353` n `185` status `ready` deltaP `-0.81` edge `-0.1863` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6027` n `176` status `ready` deltaP `-21.4489` edge `-0.2396` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

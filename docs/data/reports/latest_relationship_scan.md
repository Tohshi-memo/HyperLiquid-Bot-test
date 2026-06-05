# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T18:07:24.121502+00:00`
- Price records: `672`
- Market context records: `2992`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `17.1858` n `98` status `ready` deltaP `5.4634` edge `1.7874` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.197` n `98` status `ready` deltaP `42.2938` edge `0.7455` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.4881` n `98` status `ready` deltaP `17.7013` edge `0.8858` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.9717` n `98` status `ready` deltaP `16.4364` edge `0.7551` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.9891` n `98` status `ready` deltaP `16.2203` edge `0.4057` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0149` n `100` status `ready` deltaP `14.6646` edge `0.2163` maxDD `-2.6927`
- `market_context_high->commodity_4h` score `2.3244` n `100` status `ready` deltaP `17.2073` edge `0.1437` maxDD `-2.8438`
- `market_context_high->index_4h` score `2.2992` n `100` status `ready` deltaP `19.2195` edge `0.1423` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `0.8901` n `100` status `ready` deltaP `23.7561` edge `0.4139` maxDD `-30.9862`
- `market_context_high->index_1h` score `0.1113` n `104` status `ready` deltaP `5.7692` edge `0.0257` maxDD `-2.0579`
- `market_context_high->commodity_1h` score `-0.0837` n `104` status `ready` deltaP `0.5758` edge `0.0184` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.1554` n `104` status `ready` deltaP `4.0995` edge `0.0385` maxDD `-4.1938`
- `market_context_high->fx_1h` score `-0.3553` n `104` status `ready` deltaP `-2.1591` edge `0.0008` maxDD `-0.2237`
- `market_context_high->crypto_alt_1h` score `-0.9063` n `104` status `ready` deltaP `6.7308` edge `0.0257` maxDD `-12.6074`
- `market_context_high->unknown_4h` score `-1.043` n `100` status `ready` deltaP `0.0183` edge `0.0183` maxDD `-3.7602`
- `market_context_high->fx_4h` score `-1.0614` n `100` status `ready` deltaP `-9.0` edge `0.0018` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.0916` n `104` status `ready` deltaP `-2.1764` edge `-0.008` maxDD `-5.728`
- `market_context_high->crypto_major_1h` score `-1.375` n `104` status `ready` deltaP `4.2549` edge `-0.0032` maxDD `-13.4487`
- `market_context_high->unknown_1h` score `-1.7738` n `104` status `ready` deltaP `1.6007` edge `-0.0854` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9629` n `98` status `ready` deltaP `-7.3483` edge `-0.0274` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T10:37:24.104017+00:00`
- Price records: `672`
- Market context records: `2961`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.2459` n `121` status `ready` deltaP `12.2604` edge `1.7471` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.8649` n `121` status `ready` deltaP `17.0268` edge `0.6717` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.8841` n `121` status `ready` deltaP `17.7413` edge `0.7391` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `7.075` n `121` status `ready` deltaP `27.4779` edge `0.5179` maxDD `-3.5866`
- `market_context_high->equity_4h` score `3.3858` n `122` status `ready` deltaP `16.8732` edge `0.2086` maxDD `-0.7819`
- `market_context_high->index_24h` score `3.2579` n `121` status `ready` deltaP `13.4355` edge `0.28` maxDD `-2.5127`
- `market_context_high->crypto_alt_4h` score `2.8639` n `122` status `ready` deltaP `23.6531` edge `0.5371` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7549` n `122` status `ready` deltaP `13.9344` edge `0.0838` maxDD `-2.0601`
- `market_context_high->unknown_4h` score `0.5986` n `122` status `ready` deltaP `5.8526` edge `0.1162` maxDD `-3.7602`
- `market_context_high->equity_1h` score `0.5013` n `122` status `ready` deltaP `3.7769` edge `0.055` maxDD `-1.4059`
- `market_context_high->index_1h` score `0.0182` n `122` status `ready` deltaP `4.9107` edge `0.019` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.2191` n `122` status `ready` deltaP `1.2541` edge `0.0041` maxDD `-0.1244`
- `market_context_high->crypto_major_1h` score `-0.3753` n `122` status `ready` deltaP `5.9733` edge `0.074` maxDD `-9.622`
- `market_context_high->crypto_alt_1h` score `-0.431` n `122` status `ready` deltaP `6.258` edge `0.0942` maxDD `-10.747`
- `market_context_high->crypto_major_4h` score `-0.4695` n `122` status `ready` deltaP `12.5775` edge `0.3685` maxDD `-33.6701`
- `market_context_high->commodity_1h` score `-0.5372` n `122` status `ready` deltaP `-1.0553` edge `0.0007` maxDD `-3.3365`
- `market_context_high->unknown_1h` score `-0.7312` n `122` status `ready` deltaP `1.8529` edge `-0.0002` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-0.7925` n `122` status `ready` deltaP `5.7402` edge `0.0391` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.8133` n `122` status `ready` deltaP `-1.924` edge `-0.0027` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.9158` n `122` status `ready` deltaP `-1.162` edge `0.0093` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

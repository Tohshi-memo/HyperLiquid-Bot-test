# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T01:07:27.385097+00:00`
- Price records: `672`
- Market context records: `3023`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `21.7766` n `99` status `ready` deltaP `9.9431` edge `2.1401` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5909` n `99` status `ready` deltaP `42.3769` edge `0.7908` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `12.5822` n `99` status `ready` deltaP `21.7172` edge `0.9502` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.0849` n `99` status `ready` deltaP `20.5966` edge `1.0462` maxDD `-18.3486`
- `market_context_high->index_24h` score `6.9424` n `99` status `ready` deltaP `20.1863` edge `0.5695` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5939` n `114` status `ready` deltaP `18.8062` edge `0.1555` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6446` n `114` status `ready` deltaP `14.6476` edge `0.1759` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.4413` n `114` status `ready` deltaP `24.401` edge `0.4487` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.2495` n `114` status `ready` deltaP `17.1989` edge `0.1071` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.1213` n `126` status `ready` deltaP `3.2198` edge `0.0309` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3015` n `126` status `ready` deltaP `4.2986` edge `0.0423` maxDD `-5.7692`
- `market_context_high->index_1h` score `-0.494` n `126` status `ready` deltaP `5.0613` edge `0.0265` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.4995` n `126` status `ready` deltaP `6.948` edge `0.1026` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.5043` n `126` status `ready` deltaP `-4.2677` edge `0.0004` maxDD `-0.2615`
- `market_context_high->unknown_1h` score `-0.7` n `126` status `ready` deltaP `4.7928` edge `-0.0172` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-0.8632` n `114` status `ready` deltaP `-0.1497` edge `0.0344` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-0.952` n `126` status `ready` deltaP `4.8807` edge `0.0717` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1715` n `126` status `ready` deltaP `-2.1576` edge `-0.004` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.5096` n `114` status `ready` deltaP `-6.9026` edge `-0.0008` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.6901` n `99` status `ready` deltaP `-4.4034` edge `-0.0243` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T09:22:25.905177+00:00`
- Price records: `672`
- Market context records: `2956`
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

- `market_context_high->crypto_alt_24h` score `17.2969` n `126` status `ready` deltaP `13.3929` edge `1.7438` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.466` n `126` status `ready` deltaP `17.4107` edge `0.6359` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.0699` n `126` status `ready` deltaP `18.2044` edge `0.7515` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `5.9109` n `126` status `ready` deltaP `24.2311` edge `0.4796` maxDD `-4.8854`
- `market_context_high->index_24h` score `3.1778` n `126` status `ready` deltaP `13.8889` edge `0.2703` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.8384` n `127` status `ready` deltaP `15.149` edge `0.1935` maxDD `-2.3036`
- `market_context_high->crypto_alt_4h` score `2.0193` n `127` status `ready` deltaP `21.3762` edge `0.4819` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.8906` n `127` status `ready` deltaP `6.7433` edge `0.1346` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6678` n `127` status `ready` deltaP `13.4494` edge `0.0801` maxDD `-2.3986`
- `market_context_high->index_1h` score `0.0888` n `127` status `ready` deltaP `5.8336` edge `0.0219` maxDD `-1.2855`
- `market_context_high->equity_1h` score `0.0214` n `127` status `ready` deltaP `2.2019` edge `0.052` maxDD `-1.8586`
- `market_context_high->fx_1h` score `-0.2528` n `127` status `ready` deltaP `0.8487` edge `0.004` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.4` n `127` status `ready` deltaP `5.2678` edge `0.0896` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.517` n `127` status `ready` deltaP `-0.7261` edge `0.0011` maxDD `-3.3365`
- `market_context_high->crypto_major_1h` score `-0.654` n `127` status `ready` deltaP `4.3248` edge `0.0701` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.702` n `127` status `ready` deltaP `-0.3996` edge `0.0014` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.712` n `127` status `ready` deltaP `1.5972` edge `0.0031` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-0.7182` n `127` status `ready` deltaP `6.4624` edge `0.0438` maxDD `-8.9839`
- `market_context_high->fx_4h` score `-0.7549` n `127` status `ready` deltaP `0.7742` edge `0.0098` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-0.7848` n `127` status `ready` deltaP `11.0896` edge `0.338` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

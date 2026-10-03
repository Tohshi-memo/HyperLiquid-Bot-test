# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T09:22:23.831516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.3294` n `50` status `ready` deltaP `10.855` edge `30.46` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2288` n `50` status `ready` deltaP `12.0244` edge `24.4389` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.7207` n `50` status `ready` deltaP `26.3397` edge `1.0548` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.3216` n `70` status `ready` deltaP `30.0768` edge `0.7081` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.1328` n `50` status `ready` deltaP `33.9931` edge `0.7594` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.0912` n `73` status `ready` deltaP `38.8128` edge `0.6025` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.7495` n `73` status `ready` deltaP `29.9848` edge `0.5803` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3996` n `50` status `ready` deltaP `17.7717` edge `0.5685` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2269` n `50` status `ready` deltaP `17.793` edge `0.5292` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2536` n `70` status `ready` deltaP `32.976` edge `0.1505` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9803` n `73` status `ready` deltaP `29.5282` edge `0.1961` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.313` n `50` status `ready` deltaP `15.1779` edge `0.2412` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.2703` n `73` status `ready` deltaP `16.7496` edge `0.1964` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9881` n `50` status `ready` deltaP `13.6263` edge `0.2032` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9616` n `50` status `ready` deltaP `33.2085` edge `0.0389` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.5928` n `73` status `ready` deltaP `28.6149` edge `0.0515` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.3351` n `73` status `ready` deltaP `20.3958` edge `0.1002` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `2.023` n `73` status `ready` deltaP `8.082` edge `0.1666` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.5239` n `73` status `ready` deltaP `14.6815` edge `0.0653` maxDD `-0.8948`
- `market_context_high->fx_1h` score `1.4299` n `50` status `ready` deltaP `20.1106` edge `0.0115` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

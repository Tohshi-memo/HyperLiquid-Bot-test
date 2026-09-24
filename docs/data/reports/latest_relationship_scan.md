# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T14:37:30.380307+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10084`

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

- `market_context_high->unknown_1h` score `88.7683` n `47` status `ready` deltaP `10.116` edge `7.337` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.5264` n `47` status `ready` deltaP `29.9017` edge `3.3838` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.4836` n `47` status `ready` deltaP `24.782` edge `2.2464` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.9908` n `47` status `ready` deltaP `27.6448` edge `1.8505` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8317` n `47` status `ready` deltaP `34.9364` edge `0.4327` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `6.2045` n `98` status `ready` deltaP `2.6112` edge `1.6823` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `4.3652` n `98` status `ready` deltaP `0.3791` edge `1.2584` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5363` n `47` status `ready` deltaP `30.5445` edge `0.1149` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0688` n `47` status `ready` deltaP `34.941` edge `0.0382` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.979` n `119` status `ready` deltaP `13.9775` edge `0.2041` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6407` n `47` status `ready` deltaP `17.7542` edge `0.1435` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.4437` n `119` status `ready` deltaP `16.223` edge `0.139` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.8394` n `109` status `ready` deltaP `26.2768` edge `0.0417` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2753` n `98` status `ready` deltaP `30.063` edge `0.1262` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `1.1827` n `98` status `ready` deltaP `25.4642` edge `0.1267` maxDD `-7.2536`
- `news_risk_high->commodity_24h` score `1.0973` n `98` status `ready` deltaP `16.3088` edge `0.1006` maxDD `-2.431`
- `market_context_high->index_1h` score `0.9511` n `47` status `ready` deltaP `14.4604` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8816` n `47` status `ready` deltaP `10.7179` edge `0.0423` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.5727` n `109` status `ready` deltaP `13.6468` edge `0.1956` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.5094` n `119` status `ready` deltaP `15.7777` edge `0.0178` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T13:07:23.626048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `10012.4741` n `126` status `ready` deltaP `1.0146` edge `834.3859` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6090.7745` n `126` status `ready` deltaP `-0.6194` edge `507.5992` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1914` n `126` status `ready` deltaP `4.1013` edge `0.0146` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3162` n `126` status `ready` deltaP `2.5591` edge `0.0036` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.615` n `126` status `ready` deltaP `10.2714` edge `0.0333` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4154` n `126` status `ready` deltaP `-9.1056` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8659` n `126` status `ready` deltaP `5.5389` edge `0.0135` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8693` n `126` status `ready` deltaP `-5.9645` edge `0.0017` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2691` n `126` status `ready` deltaP `-8.072` edge `-0.0221` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5553` n `126` status `ready` deltaP `-5.166` edge `-0.0152` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.7318` n `126` status `ready` deltaP `1.8106` edge `-0.0079` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.4161` n `126` status `ready` deltaP `-4.7928` edge `-0.025` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.9643` n `126` status `ready` deltaP `-2.6326` edge `0.074` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4254` n `122` status `ready` deltaP `-13.2741` edge `-0.0066` maxDD `-6.5617`
- `market_context_high->commodity_4h` score `-6.9186` n `126` status `ready` deltaP `-19.1202` edge `-0.0798` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.2563` n `122` status `ready` deltaP `9.3608` edge `0.1144` maxDD `-51.1864`
- `market_context_high->crypto_alt_4h` score `-8.4304` n `126` status `ready` deltaP `-3.6997` edge `0.0034` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-10.2239` n `122` status `ready` deltaP `19.0375` edge `0.4801` maxDD `-142.0886`
- `market_context_high->crypto_alt_24h` score `-13.523` n `122` status `ready` deltaP `7.8808` edge `0.1976` maxDD `-147.3747`
- `market_context_high->index_24h` score `-14.5123` n `122` status `ready` deltaP `-27.0264` edge `-0.1209` maxDD `-38.6623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

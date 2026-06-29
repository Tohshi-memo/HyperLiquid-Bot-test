# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T22:07:32.678112+00:00`
- Price records: `672`
- Market context records: `5186`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `21.5689` n `83` status `ready` deltaP `33.0279` edge `1.5962` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.7118` n `83` status `ready` deltaP `26.3972` edge `1.2495` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.1203` n `83` status `ready` deltaP `27.2339` edge `1.0005` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.5737` n `154` status `ready` deltaP `19.724` edge `0.4352` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4037` n `154` status `ready` deltaP `12.8683` edge `0.4411` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3808` n `154` status `ready` deltaP `13.8621` edge `0.5019` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5484` n `155` status `ready` deltaP `9.1375` edge `0.2156` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2557` n `154` status `ready` deltaP `9.1365` edge `0.2076` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.4821` n `155` status `ready` deltaP `4.0545` edge `0.1093` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4709` n `155` status `ready` deltaP `6.1039` edge `0.1231` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.2717` n `155` status `ready` deltaP `7.7651` edge `0.0674` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1754` n `83` status `ready` deltaP `11.3621` edge `0.0284` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0238` n `155` status `ready` deltaP `5.7833` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0615` n `155` status `ready` deltaP `5.0096` edge `0.0179` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2736` n `155` status `ready` deltaP `1.5096` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4061` n `154` status `ready` deltaP `6.3748` edge `0.0354` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4981` n `154` status `ready` deltaP `4.8959` edge `0.0069` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.0278` n `83` status `ready` deltaP `6.9947` edge `-0.0149` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2318` n `154` status `ready` deltaP `0.7839` edge `0.0372` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T06:37:24.085981+00:00`
- Price records: `672`
- Market context records: `3047`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.1388` n `99` status `ready` deltaP `13.2418` edge `2.3983` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.5335` n `99` status `ready` deltaP `24.6686` edge `1.0098` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.2979` n `99` status `ready` deltaP `43.9394` edge `0.8393` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.5478` n `99` status `ready` deltaP `24.4161` edge `1.3365` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.1233` n `99` status `ready` deltaP `23.6585` edge `0.7281` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6625` n `129` status `ready` deltaP `17.8637` edge `0.1675` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.12` n `133` status `ready` deltaP `1.434` edge `0.0227` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4754` n `129` status `ready` deltaP `1.6981` edge `0.0544` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.4809` n `133` status `ready` deltaP `3.9789` edge `0.0181` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.535` n `133` status `ready` deltaP `-4.7409` edge `0.0` maxDD `-0.2921`
- `market_context_high->crypto_alt_1h` score `-0.5865` n `133` status `ready` deltaP `6.2345` edge `0.0962` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.6866` n `133` status `ready` deltaP `3.2405` edge `0.0317` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.9301` n `133` status `ready` deltaP `4.5675` edge `0.0766` maxDD `-15.1032`
- `market_context_high->index_4h` score `-0.9621` n `129` status `ready` deltaP `12.5602` edge `0.0622` maxDD `-16.8761`
- `market_context_high->unknown_1h` score `-0.9685` n `133` status `ready` deltaP `4.4516` edge `-0.0373` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1212` n `129` status `ready` deltaP `-8.4834` edge `-0.0037` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1786` n `133` status `ready` deltaP `-1.7537` edge `-0.0026` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.2718` n `99` status `ready` deltaP `-0.5839` edge `-0.0149` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9298` n `129` status `ready` deltaP `9.8423` edge `0.0515` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.2195` n `129` status `ready` deltaP `17.8696` edge `0.2726` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

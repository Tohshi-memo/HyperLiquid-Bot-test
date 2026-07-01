# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T09:22:27.840128+00:00`
- Price records: `672`
- Market context records: `5338`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9522`

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

- `market_context_high->unknown_24h` score `18.8659` n `153` status `ready` deltaP `22.4775` edge `1.4313` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9404` n `153` status `ready` deltaP `24.52` edge `0.8299` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.8681` n `153` status `ready` deltaP `17.7083` edge `0.8505` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0451` n `194` status `ready` deltaP `13.3361` edge `0.3941` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9657` n `194` status `ready` deltaP `11.8839` edge `0.332` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1376` n `194` status `ready` deltaP `11.1594` edge `0.2676` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7455` n `153` status `ready` deltaP `24.2953` edge `0.0971` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.559` n `194` status `ready` deltaP `8.6117` edge `0.0857` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2618` n `153` status `ready` deltaP `10.7026` edge `0.04` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.0866` n `194` status `ready` deltaP `2.2455` edge `0.0884` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.067` n `194` status `ready` deltaP `6.5174` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0263` n `194` status `ready` deltaP `4.3413` edge `0.0978` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3213` n `194` status `ready` deltaP `1.1637` edge `0.0` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.3475` n `194` status `ready` deltaP `2.0958` edge `0.009` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.3572` n `194` status `ready` deltaP `6.5266` edge `0.0266` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6122` n `194` status `ready` deltaP `3.0503` edge `0.0041` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2869` n `194` status `ready` deltaP `7.7555` edge `-0.0407` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.3784` n `194` status `ready` deltaP `-2.727` edge `-0.0049` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3943` n `194` status `ready` deltaP `-5.7` edge `-0.0165` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.342` n `153` status `ready` deltaP `12.8268` edge `0.327` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

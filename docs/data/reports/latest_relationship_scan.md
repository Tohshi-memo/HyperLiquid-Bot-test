# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T09:07:36.689667+00:00`
- Price records: `672`
- Market context records: `5337`
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

- `market_context_high->unknown_24h` score `18.9026` n `153` status `ready` deltaP `22.6511` edge `1.4332` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9536` n `153` status `ready` deltaP `24.52` edge `0.831` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.894` n `153` status `ready` deltaP `17.882` edge `0.8515` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0559` n `194` status `ready` deltaP `13.3361` edge `0.395` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9837` n `194` status `ready` deltaP `11.8839` edge `0.3335` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1436` n `194` status `ready` deltaP `11.1594` edge `0.2681` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7294` n `153` status `ready` deltaP `24.1217` edge `0.0962` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.571` n `194` status `ready` deltaP `8.7614` edge `0.0857` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2793` n `153` status `ready` deltaP `10.8762` edge `0.0403` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1142` n `194` status `ready` deltaP `2.3952` edge `0.0897` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0658` n `194` status `ready` deltaP `6.5174` edge `0.0124` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0515` n `194` status `ready` deltaP `4.491` edge `0.0989` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3127` n `194` status `ready` deltaP `1.3134` edge `0.0001` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.3451` n `194` status `ready` deltaP `2.0958` edge `0.0093` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.358` n `194` status `ready` deltaP `6.5266` edge `0.0265` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6027` n `194` status `ready` deltaP `3.2027` edge `0.0043` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2687` n `194` status `ready` deltaP `7.908` edge `-0.0402` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.3952` n `194` status `ready` deltaP `-2.8767` edge `-0.0053` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3707` n `194` status `ready` deltaP `-5.5475` edge `-0.0145` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.3233` n `153` status `ready` deltaP `12.8268` edge `0.3294` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

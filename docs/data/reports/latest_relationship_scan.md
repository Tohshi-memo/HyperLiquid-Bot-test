# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T07:22:30.265197+00:00`
- Price records: `672`
- Market context records: `5329`
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

- `market_context_high->unknown_24h` score `18.9849` n `153` status `ready` deltaP `22.8247` edge `1.4389` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9512` n `153` status `ready` deltaP `24.52` edge `0.8308` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9583` n `153` status `ready` deltaP `18.0556` edge `0.8557` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8727` n `194` status `ready` deltaP `12.7263` edge `0.3838` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8317` n `194` status `ready` deltaP `11.2742` edge `0.3249` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.0892` n `194` status `ready` deltaP `10.8546` edge `0.2656` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.6434` n `153` status `ready` deltaP `23.4273` edge `0.0898` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5985` n `194` status `ready` deltaP `9.0608` edge `0.086` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3921` n `153` status `ready` deltaP `12.0915` edge `0.0416` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1178` n `194` status `ready` deltaP `2.3952` edge `0.09` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.1029` n `194` status `ready` deltaP `6.9665` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0551` n `194` status `ready` deltaP `4.6407` edge `0.0982` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2782` n `194` status `ready` deltaP `3.1437` edge `0.0109` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3368` n `194` status `ready` deltaP `0.8643` edge `0.0` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4062` n `194` status `ready` deltaP `5.7644` edge `0.0254` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5837` n `194` status `ready` deltaP `3.5076` edge `0.0047` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2189` n `194` status `ready` deltaP `8.3653` edge `-0.0391` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4072` n `194` status `ready` deltaP `-2.8767` edge `-0.0063` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2988` n `194` status `ready` deltaP `-5.3951` edge `-0.0063` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2921` n `153` status `ready` deltaP `12.8268` edge `0.3334` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

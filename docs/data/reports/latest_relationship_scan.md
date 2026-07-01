# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T06:22:27.229003+00:00`
- Price records: `672`
- Market context records: `5325`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_24h` score `19.0233` n `153` status `ready` deltaP `22.8247` edge `1.4421` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.938` n `153` status `ready` deltaP `24.52` edge `0.8297` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.0136` n `153` status `ready` deltaP `18.4028` edge `0.858` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8823` n `194` status `ready` deltaP `12.7263` edge `0.3846` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8677` n `194` status `ready` deltaP `11.2742` edge `0.3279` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.116` n `194` status `ready` deltaP `11.1594` edge `0.2658` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.5761` n `153` status `ready` deltaP `22.7328` edge `0.0858` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.565` n `194` status `ready` deltaP `8.7614` edge `0.0852` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.4621` n `153` status `ready` deltaP `12.7859` edge `0.0428` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.0842` n `194` status `ready` deltaP `2.3952` edge `0.0872` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0765` n `194` status `ready` deltaP `6.6671` edge `0.0123` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0263` n `194` status `ready` deltaP `4.6407` edge `0.0958` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.268` n `194` status `ready` deltaP `3.2934` edge `0.0112` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3111` n `194` status `ready` deltaP `1.3134` edge `0.0003` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4236` n `194` status `ready` deltaP `5.4595` edge `0.0252` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5742` n `194` status `ready` deltaP `3.6601` edge `0.0049` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1329` n `194` status `ready` deltaP `8.9751` edge `-0.036` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.394` n `194` status `ready` deltaP `-2.727` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2817` n `194` status `ready` deltaP `-5.3951` edge `-0.0041` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2921` n `153` status `ready` deltaP `12.8268` edge `0.3334` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

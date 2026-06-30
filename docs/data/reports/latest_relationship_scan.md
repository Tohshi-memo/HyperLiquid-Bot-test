# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T19:22:30.719159+00:00`
- Price records: `672`
- Market context records: `5278`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `25.5908` n `153` status `ready` deltaP `28.5539` edge `1.9512` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.562` n `153` status `ready` deltaP `25.7353` edge `0.8736` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3204` n `172` status `ready` deltaP `16.3819` edge `0.4149` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8344` n `172` status `ready` deltaP `15.1624` edge `0.4477` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.7238` n `153` status `ready` deltaP `19.9653` edge `0.7401` maxDD `-40.0306`
- `market_context_high->equity_4h` score `0.9019` n `172` status `ready` deltaP `9.5434` edge `0.1754` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.788` n `172` status `ready` deltaP `14.4427` edge `0.0716` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5733` n `153` status `ready` deltaP `13.3068` edge `0.0486` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4875` n `180` status `ready` deltaP `4.9168` edge `0.104` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2652` n `180` status `ready` deltaP `5.7518` edge `0.1083` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2365` n `153` status `ready` deltaP `20.8231` edge `0.055` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0637` n `180` status `ready` deltaP `6.7698` edge `0.0567` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0318` n `180` status `ready` deltaP `6.2575` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2976` n `180` status `ready` deltaP `3.4631` edge `0.0113` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.303` n `172` status `ready` deltaP `6.959` edge `0.0265` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3752` n `180` status `ready` deltaP `0.1264` edge `0.0` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7136` n `172` status `ready` deltaP `1.4145` edge `0.002` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3885` n `180` status `ready` deltaP `-2.6281` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6347` n `172` status `ready` deltaP `-2.5843` edge `0.008` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.3748` n `180` status `ready` deltaP `6.5769` edge `-0.1776` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T06:37:30.051499+00:00`
- Price records: `672`
- Market context records: `5326`
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

- `market_context_high->unknown_24h` score `19.0173` n `153` status `ready` deltaP `22.8247` edge `1.4416` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.938` n `153` status `ready` deltaP `24.52` edge `0.8297` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9877` n `153` status `ready` deltaP `18.2292` edge `0.857` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8811` n `194` status `ready` deltaP `12.7263` edge `0.3845` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8569` n `194` status `ready` deltaP `11.2742` edge `0.327` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1014` n `194` status `ready` deltaP `11.007` edge `0.2656` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.5929` n `153` status `ready` deltaP `22.9065` edge `0.0868` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5638` n `194` status `ready` deltaP `8.7614` edge `0.0851` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.4446` n `153` status `ready` deltaP `12.6123` edge `0.0425` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.0914` n `194` status `ready` deltaP `2.3952` edge `0.0878` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0765` n `194` status `ready` deltaP `6.6671` edge `0.0123` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0335` n `194` status `ready` deltaP `4.6407` edge `0.0964` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2688` n `194` status `ready` deltaP `3.2934` edge `0.0111` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3197` n `194` status `ready` deltaP `1.1637` edge `0.0002` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4236` n `194` status `ready` deltaP `5.4595` edge `0.0252` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5829` n `194` status `ready` deltaP `3.5076` edge `0.0048` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1535` n `194` status `ready` deltaP `8.8226` edge `-0.0367` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.3928` n `194` status `ready` deltaP `-2.727` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2848` n `194` status `ready` deltaP `-5.3951` edge `-0.0045` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2921` n `153` status `ready` deltaP `12.8268` edge `0.3334` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

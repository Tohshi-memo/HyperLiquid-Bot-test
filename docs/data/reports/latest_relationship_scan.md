# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T09:37:25.706420+00:00`
- Price records: `672`
- Market context records: `5339`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9524`

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

- `market_context_high->unknown_24h` score `18.4075` n `154` status `ready` deltaP `22.3124` edge `1.3942` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.7807` n `154` status `ready` deltaP `24.0913` edge `0.8228` maxDD `-26.8012`
- `market_context_high->equity_24h` score `4.833` n `154` status `ready` deltaP `17.7804` edge `0.8471` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0403` n `194` status `ready` deltaP `13.3361` edge `0.3937` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9477` n `194` status `ready` deltaP `11.8839` edge `0.3305` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1256` n `194` status `ready` deltaP `11.1594` edge `0.2666` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.757` n `154` status `ready` deltaP `24.4566` edge `0.0975` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5578` n `194` status `ready` deltaP `8.6117` edge `0.0856` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2549` n `154` status `ready` deltaP `10.6309` edge `0.0399` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0789` n `194` status `ready` deltaP `6.6671` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0566` n `194` status `ready` deltaP `2.0958` edge `0.0869` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.0001` n `194` status `ready` deltaP `4.1916` edge `0.0966` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3298` n `194` status `ready` deltaP `1.014` edge `-0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3493` n `194` status `ready` deltaP `6.679` edge `0.0266` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3592` n `194` status `ready` deltaP `1.9461` edge `0.0085` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6217` n `194` status `ready` deltaP `2.8979` edge `0.0039` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2675` n `194` status `ready` deltaP `7.908` edge `-0.0401` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.3652` n `194` status `ready` deltaP `-2.5773` edge `-0.0048` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4162` n `194` status `ready` deltaP `-5.8524` edge `-0.0183` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.4187` n `154` status `ready` deltaP `12.5` edge `0.324` maxDD `-53.6498`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

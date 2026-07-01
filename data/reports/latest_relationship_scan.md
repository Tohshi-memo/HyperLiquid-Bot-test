# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T07:37:31.241385+00:00`
- Price records: `672`
- Market context records: `5330`
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

- `market_context_high->unknown_24h` score `18.9765` n `153` status `ready` deltaP `22.8247` edge `1.4382` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9596` n `153` status `ready` deltaP `24.52` edge `0.8315` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9583` n `153` status `ready` deltaP `18.0556` edge `0.8557` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8859` n `194` status `ready` deltaP `12.7263` edge `0.3849` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8353` n `194` status `ready` deltaP `11.2742` edge `0.3252` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1098` n `194` status `ready` deltaP `11.007` edge `0.2663` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.661` n `153` status `ready` deltaP `23.6009` edge `0.0909` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.6141` n `194` status `ready` deltaP `9.2105` edge `0.0863` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3758` n `153` status `ready` deltaP `11.9179` edge `0.0414` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1333` n `194` status `ready` deltaP `2.5449` edge `0.0903` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.1161` n `194` status `ready` deltaP `7.1162` edge `0.0126` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0563` n `194` status `ready` deltaP `4.6407` edge `0.0983` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2875` n `194` status `ready` deltaP `2.994` edge `0.0107` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3368` n `194` status `ready` deltaP `0.8643` edge `0.0` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3967` n `194` status `ready` deltaP `5.9168` edge `0.0256` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5837` n `194` status `ready` deltaP `3.5076` edge `0.0047` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2359` n `194` status `ready` deltaP `8.2129` edge `-0.0395` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4215` n `194` status `ready` deltaP `-3.0264` edge `-0.0065` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3043` n `194` status `ready` deltaP `-5.3951` edge `-0.007` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2929` n `153` status `ready` deltaP `12.8268` edge `0.3333` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

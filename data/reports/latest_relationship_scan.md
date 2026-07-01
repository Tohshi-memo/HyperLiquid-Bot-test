# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T02:37:26.364579+00:00`
- Price records: `672`
- Market context records: `5310`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `19.8043` n `153` status `ready` deltaP `23.6928` edge `1.5014` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4468` n `153` status `ready` deltaP `25.7353` edge `0.864` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.2134` n `153` status `ready` deltaP `19.4445` edge `0.8677` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.2989` n `194` status `ready` deltaP `12.4937` edge `0.3557` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.2229` n `194` status `ready` deltaP `13.4885` edge `0.4079` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9232` n `194` status `ready` deltaP `10.5497` edge `0.2538` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5506` n `194` status `ready` deltaP `8.9111` edge `0.083` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5349` n `153` status `ready` deltaP `13.3068` edge `0.0454` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.3532` n `153` status `ready` deltaP `20.9967` edge `0.0688` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.1909` n `194` status `ready` deltaP `2.994` edge `0.0921` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.055` n `194` status `ready` deltaP `4.9401` edge `0.0962` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0406` n `194` status `ready` deltaP `6.3677` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3257` n `194` status `ready` deltaP `2.5449` edge `0.0088` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.403` n `194` status `ready` deltaP `-0.3333` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.545` n `194` status `ready` deltaP `3.9351` edge `0.0198` maxDD `-2.9391`
- `market_context_high->unknown_4h` score `-0.5894` n `194` status `ready` deltaP `10.8043` edge `-0.0029` maxDD `-6.126`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4371` n `194` status `ready` deltaP `-3.1761` edge `-0.0068` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.414` n `194` status `ready` deltaP `-6.9195` edge `-0.0109` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.0256` n `153` status `ready` deltaP `13.3476` edge `0.3641` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

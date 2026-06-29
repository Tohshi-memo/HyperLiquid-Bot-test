# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T20:07:29.027997+00:00`
- Price records: `672`
- Market context records: `5177`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `25.069` n `75` status `ready` deltaP `32.5139` edge `1.8913` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.6697` n `75` status `ready` deltaP `23.4167` edge `1.0992` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.1963` n `75` status `ready` deltaP `24.6389` edge `0.9408` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.0535` n `149` status `ready` deltaP `20.3511` edge `0.471` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0073` n `149` status `ready` deltaP `15.3738` edge `0.4747` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.6947` n `149` status `ready` deltaP `14.3365` edge `0.5249` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6863` n `155` status `ready` deltaP `9.886` edge `0.2221` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.3986` n `149` status `ready` deltaP `9.0921` edge `0.2198` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5541` n `155` status `ready` deltaP `4.3539` edge `0.1133` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5417` n `155` status `ready` deltaP `6.553` edge `0.126` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3687` n `155` status `ready` deltaP `8.6633` edge `0.0695` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.037` n `155` status `ready` deltaP `5.933` edge `0.0139` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0436` n `155` status `ready` deltaP `5.309` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.0863` n `75` status `ready` deltaP `9.6667` edge `0.0179` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2324` n `155` status `ready` deltaP `2.2581` edge `0.0004` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.403` n `149` status `ready` deltaP `6.0689` edge `0.0377` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5701` n `149` status `ready` deltaP `3.5409` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6211` n `155` status `ready` deltaP `0.2762` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `-0.967` n `75` status `ready` deltaP `10.3333` edge `0.0654` maxDD `-11.9943`
- `market_context_high->metal_24h` score `-1.0687` n `75` status `ready` deltaP `-5.1528` edge `0.1526` maxDD `-11.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

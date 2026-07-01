# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T03:37:29.874944+00:00`
- Price records: `672`
- Market context records: `5314`
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

- `market_context_high->unknown_24h` score `19.15` n `153` status `ready` deltaP `22.9984` edge `1.4515` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.3472` n `153` status `ready` deltaP `25.7353` edge `0.8557` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.146` n `153` status `ready` deltaP `19.0972` edge `0.8644` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.2193` n `194` status `ready` deltaP `12.1888` edge `0.3511` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.1651` n `194` status `ready` deltaP `13.3361` edge `0.4041` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0536` n `194` status `ready` deltaP `11.1594` edge `0.2606` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5265` n `153` status `ready` deltaP `13.3068` edge `0.0447` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.4906` n `194` status `ready` deltaP `8.462` edge `0.081` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.3891` n `153` status `ready` deltaP `20.9967` edge `0.0734` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.083` n `194` status `ready` deltaP `2.3952` edge `0.0871` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0262` n `194` status `ready` deltaP `6.218` edge `0.0111` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0061` n `194` status `ready` deltaP `4.6407` edge `0.0931` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.335` n `194` status `ready` deltaP `2.3952` edge `0.0086` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3874` n `194` status `ready` deltaP `-0.0339` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4938` n `194` status `ready` deltaP `4.5448` edge `0.0223` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.6657` n `194` status `ready` deltaP `10.1946` edge `-0.0052` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4347` n `194` status `ready` deltaP `-3.1761` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3511` n `194` status `ready` deltaP `-6.3097` edge `-0.0069` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.0841` n `153` status `ready` deltaP `13.3476` edge `0.3566` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

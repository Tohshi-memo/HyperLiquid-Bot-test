# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T10:07:29.131052+00:00`
- Price records: `672`
- Market context records: `5341`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `17.5207` n `156` status `ready` deltaP `21.9818` edge `1.3225` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.3818` n `156` status `ready` deltaP `23.2505` edge `0.8069` maxDD `-27.7401`
- `market_context_high->equity_24h` score `4.7616` n `156` status `ready` deltaP `17.922` edge `0.8402` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0163` n `194` status `ready` deltaP `13.3361` edge `0.3917` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9093` n `194` status `ready` deltaP `11.8839` edge `0.3273` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.0812` n `194` status `ready` deltaP `11.1594` edge `0.2629` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7781` n `156` status `ready` deltaP `24.7729` edge `0.0981` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5291` n `194` status `ready` deltaP `8.3123` edge `0.0852` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2419` n `156` status `ready` deltaP `10.4835` edge `0.0398` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0921` n `194` status `ready` deltaP `6.8168` edge `0.0126` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.023` n `194` status `ready` deltaP `1.9461` edge `0.0851` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.0276` n `194` status `ready` deltaP `4.0419` edge `0.0953` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.347` n `194` status `ready` deltaP `0.7146` edge `-0.0003` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3493` n `194` status `ready` deltaP `6.679` edge `0.0266` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3833` n `194` status `ready` deltaP `1.6467` edge `0.0074` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6399` n `194` status `ready` deltaP `2.593` edge `0.0036` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2675` n `194` status `ready` deltaP `7.908` edge `-0.0401` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.394` n `194` status `ready` deltaP `-2.8767` edge `-0.0052` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4555` n `194` status `ready` deltaP `-6.1573` edge `-0.0213` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.6048` n `156` status `ready` deltaP `11.859` edge `0.3167` maxDD `-53.9664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

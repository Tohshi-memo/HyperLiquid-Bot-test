# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T04:51:03.645093+00:00`
- Price records: `672`
- Market context records: `5319`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `19.0125` n `153` status `ready` deltaP `22.8247` edge `1.4412` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.0973` n `153` status `ready` deltaP `25.0409` edge `0.8395` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.1184` n `153` status `ready` deltaP `19.0972` edge `0.8621` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.1039` n `194` status `ready` deltaP `12.0364` edge `0.3425` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.0775` n `194` status `ready` deltaP `13.3361` edge `0.3968` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.201` n `194` status `ready` deltaP `11.9216` edge `0.2678` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5242` n `194` status `ready` deltaP `8.462` edge `0.0838` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5181` n `153` status `ready` deltaP `13.3068` edge `0.044` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.472` n `153` status `ready` deltaP `21.6912` edge `0.0794` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.0482` n `194` status `ready` deltaP `2.2455` edge `0.0852` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0358` n `194` status `ready` deltaP `6.218` edge `0.0119` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0133` n `194` status `ready` deltaP `4.491` edge `0.0935` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3117` n `194` status `ready` deltaP `2.6946` edge `0.0096` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.354` n `194` status `ready` deltaP `0.5649` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4331` n `194` status `ready` deltaP `5.307` edge `0.025` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6201` n `194` status `ready` deltaP `2.8979` edge `0.0041` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.8379` n `194` status `ready` deltaP `9.7372` edge `-0.0165` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4227` n `194` status `ready` deltaP `-3.0264` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2841` n `194` status `ready` deltaP `-5.5475` edge `-0.0034` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2152` n `153` status `ready` deltaP `13.0004` edge `0.3421` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T10:22:26.640199+00:00`
- Price records: `672`
- Market context records: `5342`
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

- `market_context_high->unknown_24h` score `17.0216` n `157` status `ready` deltaP `21.3531` edge `1.2851` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.1599` n `157` status `ready` deltaP `22.8381` edge `0.7985` maxDD `-28.3274`
- `market_context_high->equity_24h` score `4.7263` n `157` status `ready` deltaP `17.9914` edge `0.8368` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9959` n `194` status `ready` deltaP `13.3361` edge `0.39` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8743` n `194` status `ready` deltaP `11.7315` edge `0.3254` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.0354` n `194` status `ready` deltaP `11.007` edge `0.2601` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7885` n `157` status `ready` deltaP `24.9281` edge `0.0984` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5111` n `194` status `ready` deltaP `8.1626` edge `0.0847` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2358` n `157` status `ready` deltaP `10.4078` edge `0.0398` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0789` n `194` status `ready` deltaP `6.6671` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0146` n `194` status `ready` deltaP `1.9461` edge `0.0844` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.0324` n `194` status `ready` deltaP `4.0419` edge `0.0949` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3547` n `194` status `ready` deltaP `0.5649` edge `-0.0003` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3588` n `194` status `ready` deltaP `6.5266` edge `0.0264` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.395` n `194` status `ready` deltaP `1.497` edge `0.0069` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6486` n `194` status `ready` deltaP `2.4406` edge `0.0035` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2627` n `194` status `ready` deltaP `7.908` edge `-0.0397` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4083` n `194` status `ready` deltaP `-3.0264` edge `-0.0054` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4728` n `194` status `ready` deltaP `-6.3097` edge `-0.0225` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.6933` n `157` status `ready` deltaP `11.5446` edge `0.3134` maxDD `-54.1096`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

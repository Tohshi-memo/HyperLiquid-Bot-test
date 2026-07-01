# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T08:07:32.097757+00:00`
- Price records: `672`
- Market context records: `5332`
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

- `market_context_high->unknown_24h` score `18.9609` n `153` status `ready` deltaP `22.8247` edge `1.4369` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9704` n `153` status `ready` deltaP `24.52` edge `0.8324` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9499` n `153` status `ready` deltaP `18.0556` edge `0.855` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9571` n `194` status `ready` deltaP `13.0312` edge `0.3888` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9005` n `194` status `ready` deltaP `11.579` edge `0.3286` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1364` n `194` status `ready` deltaP `11.1594` edge `0.2675` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.6939` n `153` status `ready` deltaP `23.9481` edge `0.0928` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.6153` n `194` status `ready` deltaP `9.2105` edge `0.0864` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3432` n `153` status `ready` deltaP `11.5706` edge `0.041` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1477` n `194` status `ready` deltaP `2.6946` edge `0.0905` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.1161` n `194` status `ready` deltaP `7.1162` edge `0.0126` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0575` n `194` status `ready` deltaP `4.6407` edge `0.0984` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3078` n `194` status `ready` deltaP `2.6946` edge `0.0101` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3368` n `194` status `ready` deltaP `0.8643` edge `0.0` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3777` n `194` status `ready` deltaP `6.2217` edge `0.026` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5845` n `194` status `ready` deltaP `3.5076` edge `0.0046` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2723` n `194` status `ready` deltaP `7.908` edge `-0.0405` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4227` n `194` status `ready` deltaP `-3.0264` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3183` n `194` status `ready` deltaP `-5.3951` edge `-0.0088` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2921` n `153` status `ready` deltaP `12.8268` edge `0.3334` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

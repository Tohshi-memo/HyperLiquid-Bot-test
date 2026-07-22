# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T15:22:35.749354+00:00`
- Price records: `672`
- Market context records: `7577`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2685` n `164` status `ready` deltaP `10.0321` edge `0.0315` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0031` n `164` status `ready` deltaP `5.7515` edge `0.0101` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.109` n `155` status `ready` deltaP `12.7144` edge `0.0645` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2068` n `164` status `ready` deltaP `5.3834` edge `0.0041` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4332` n `164` status `ready` deltaP `11.895` edge `0.0378` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.495` n `164` status `ready` deltaP `1.3331` edge `-0.0002` maxDD `-0.6615`
- `market_context_high->crypto_alt_1h` score `-0.6991` n `164` status `ready` deltaP `-0.1607` edge `0.0032` maxDD `-5.0068`
- `market_context_high->metal_1h` score `-0.7513` n `164` status `ready` deltaP `-0.0548` edge `0.0108` maxDD `-1.2069`
- `market_context_high->crypto_major_1h` score `-0.8265` n `164` status `ready` deltaP `4.7283` edge `0.0017` maxDD `-7.4678`
- `market_context_high->unknown_24h` score `-0.8735` n `156` status `ready` deltaP `7.3852` edge `0.0911` maxDD `-9.5186`
- `market_context_high->equity_1h` score `-0.916` n `164` status `ready` deltaP `4.2225` edge `0.0365` maxDD `-9.8998`
- `market_context_high->fx_24h` score `-1.0115` n `155` status `ready` deltaP `6.8147` edge `0.0143` maxDD `-3.8554`
- `market_context_high->unknown_1h` score `-1.4252` n `164` status `ready` deltaP `0.7485` edge `-0.0614` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.4551` n `164` status `ready` deltaP `1.2195` edge `0.0535` maxDD `-4.8549`
- `market_context_high->crypto_alt_4h` score `-1.469` n `164` status `ready` deltaP `0.6098` edge `0.0399` maxDD `-11.9168`
- `market_context_high->equity_4h` score `-1.5093` n `164` status `ready` deltaP `3.5131` edge `0.2198` maxDD `-21.9375`
- `market_context_high->unknown_4h` score `-1.9546` n `164` status `ready` deltaP `10.061` edge `-0.082` maxDD `-6.1862`
- `market_context_high->fx_4h` score `-2.116` n `164` status `ready` deltaP `-1.1952` edge `0.0001` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.1934` n `164` status `ready` deltaP `5.1829` edge `0.0409` maxDD `-20.8664`
- `market_context_high->metal_24h` score `-3.659` n `156` status `ready` deltaP `-5.5422` edge `0.0728` maxDD `-15.7292`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

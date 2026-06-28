# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T22:22:25.575584+00:00`
- Price records: `672`
- Market context records: `5083`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.0166` n `74` status `ready` deltaP `27.0364` edge `0.8554` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `10.5565` n `105` status `ready` deltaP `1.4828` edge `0.9336` maxDD `-2.769`
- `market_context_high->unknown_4h` score `9.2493` n `93` status `ready` deltaP `21.4496` edge `0.73` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2657` n `93` status `ready` deltaP `17.8616` edge `0.525` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.415` n `93` status `ready` deltaP `16.3208` edge `0.5191` maxDD `-9.7988`
- `market_context_high->equity_4h` score `2.3183` n `93` status `ready` deltaP `12.3656` edge `0.2239` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.2148` n `105` status `ready` deltaP `11.1021` edge `0.0804` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.8594` n `105` status `ready` deltaP `6.3815` edge `0.1101` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.7604` n `105` status `ready` deltaP `11.688` edge `0.0351` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.5961` n `93` status `ready` deltaP `9.2512` edge `0.0959` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.5909` n `105` status `ready` deltaP `7.6205` edge `0.1276` maxDD `-5.2121`
- `market_context_high->index_1h` score `0.4628` n `105` status `ready` deltaP `7.6461` edge `0.0174` maxDD `-0.3843`
- `market_context_high->index_4h` score `0.3428` n `93` status `ready` deltaP `8.8021` edge `0.046` maxDD `-1.0893`
- `market_context_high->commodity_4h` score `-0.4532` n `93` status `ready` deltaP `8.9217` edge `0.0106` maxDD `-3.6276`
- `market_context_high->fx_24h` score `-0.664` n `74` status `ready` deltaP `-0.6194` edge `-0.0048` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.6871` n `105` status `ready` deltaP `0.8169` edge `0.0042` maxDD `-1.3525`
- `market_context_high->fx_4h` score `-1.2958` n `93` status `ready` deltaP `-8.2169` edge `-0.0084` maxDD `-1.5692`
- `market_context_high->commodity_24h` score `-1.4783` n `74` status `ready` deltaP `11.036` edge `0.0471` maxDD `-15.8156`
- `market_context_high->fx_1h` score `-1.8756` n `105` status `ready` deltaP `-13.0197` edge `-0.0055` maxDD `-0.7866`
- `market_context_high->metal_24h` score `-4.4662` n `74` status `ready` deltaP `-4.4106` edge `0.0023` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

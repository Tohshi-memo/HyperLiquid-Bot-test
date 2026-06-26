# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T23:22:30.004320+00:00`
- Price records: `672`
- Market context records: `4875`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `15.3006` n `110` status `ready` deltaP `10.1715` edge `1.249` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6274` n `110` status `ready` deltaP `23.1624` edge `0.701` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4532` n `110` status `ready` deltaP `21.2084` edge `0.5316` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1566` n `110` status `ready` deltaP `18.3398` edge `0.5132` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1838` n `91` status `ready` deltaP `25.2957` edge `0.2976` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.217` n `110` status `ready` deltaP `8.9773` edge `0.1078` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8742` n `110` status `ready` deltaP `12.439` edge `0.1673` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5747` n `110` status `ready` deltaP `11.8403` edge `0.041` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4711` n `110` status `ready` deltaP `6.4698` edge `0.1211` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4612` n `110` status `ready` deltaP `8.4703` edge `0.1049` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.216` n `110` status `ready` deltaP `4.2352` edge `0.0592` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1682` n `110` status `ready` deltaP `0.8437` edge `0.0308` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2098` n `110` status `ready` deltaP `3.5819` edge `0.0152` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4767` n `110` status `ready` deltaP `0.46` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6268` n `110` status `ready` deltaP `1.6768` edge `0.0055` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9326` n `110` status `ready` deltaP `5.6624` edge `0.0032` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3358` n `110` status `ready` deltaP `-6.8672` edge `-0.0042` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8229` n `91` status `ready` deltaP `-6.1623` edge `-0.0098` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.6305` n `91` status `ready` deltaP `-6.4504` edge `-0.1421` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0939` n `91` status `ready` deltaP `12.7632` edge `0.0013` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

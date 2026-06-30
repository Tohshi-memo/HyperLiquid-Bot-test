# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T19:07:26.997983+00:00`
- Price records: `672`
- Market context records: `5276`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `25.7787` n `153` status `ready` deltaP `28.7275` edge `1.9657` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5908` n `153` status `ready` deltaP `25.7353` edge `0.876` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3093` n `171` status `ready` deltaP `16.1541` edge `0.4155` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8006` n `171` status `ready` deltaP `14.9346` edge `0.4464` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.7142` n `153` status `ready` deltaP `19.9653` edge `0.7393` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `0.8794` n `171` status `ready` deltaP `14.7153` edge `0.0774` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8672` n `171` status `ready` deltaP `9.3496` edge `0.1738` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5745` n `153` status `ready` deltaP `13.3068` edge `0.0487` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5085` n `179` status `ready` deltaP `5.0589` edge `0.1048` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2808` n `179` status `ready` deltaP `5.8876` edge `0.1087` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2502` n `153` status `ready` deltaP `20.9967` edge `0.0556` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0403` n `179` status `ready` deltaP `6.5526` edge `0.0562` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0139` n `179` status `ready` deltaP `6.034` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2709` n `179` status `ready` deltaP `3.7517` edge `0.0116` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3345` n `179` status `ready` deltaP `0.2685` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4894` n `171` status `ready` deltaP `6.7278` edge `0.0261` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6925` n `171` status `ready` deltaP `1.7749` edge `0.0023` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4193` n `179` status `ready` deltaP `-2.9229` edge `-0.007` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6431` n `171` status `ready` deltaP `-2.7617` edge `0.0081` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.2093` n `179` status `ready` deltaP `6.7717` edge `-0.1651` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

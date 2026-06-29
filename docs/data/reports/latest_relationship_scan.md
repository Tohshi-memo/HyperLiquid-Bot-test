# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T10:22:30.303091+00:00`
- Price records: `672`
- Market context records: `5135`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `29.095` n `63` status `ready` deltaP `29.3155` edge `2.2634` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `7.574` n `131` status `ready` deltaP `9.2574` edge `0.6336` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3405` n `120` status `ready` deltaP `20.2845` edge `0.5787` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.04` n `120` status `ready` deltaP `14.8069` edge `0.4812` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5848` n `120` status `ready` deltaP `12.6118` edge `0.4439` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.5865` n `63` status `ready` deltaP `20.2381` edge `0.1543` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.8229` n `120` status `ready` deltaP `8.496` edge `0.1758` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.8006` n `131` status `ready` deltaP `5.6806` edge `0.125` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7307` n `131` status `ready` deltaP `8.061` edge `0.1317` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6412` n `131` status `ready` deltaP `7.2222` edge `0.0646` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.0468` n `63` status `ready` deltaP `0.9424` edge `0.1986` maxDD `-11.4122`
- `market_context_high->index_1h` score `-0.0479` n `131` status `ready` deltaP `4.7973` edge `0.0144` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0769` n `131` status `ready` deltaP `4.5584` edge `0.0148` maxDD `-1.7376`
- `market_context_high->crypto_alt_24h` score `-0.441` n `63` status `ready` deltaP `15.625` edge `0.5406` maxDD `-50.438`
- `market_context_high->index_4h` score `-0.4588` n `120` status `ready` deltaP `5.6402` edge `0.0359` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5016` n `131` status `ready` deltaP `1.729` edge `0.0011` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5713` n `120` status `ready` deltaP `2.3984` edge `0.0518` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6607` n `131` status `ready` deltaP `-2.8512` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.9963` n `120` status `ready` deltaP `-3.1098` edge `0.0003` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.0928` n `63` status `ready` deltaP `0.8185` edge `-0.005` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

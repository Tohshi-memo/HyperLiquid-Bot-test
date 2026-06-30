# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T13:07:26.509528+00:00`
- Price records: `672`
- Market context records: `5250`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7568`

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

- `market_context_high->unknown_24h` score `25.0279` n `139` status `ready` deltaP `30.4556` edge `1.9016` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.6922` n `139` status `ready` deltaP `31.2924` edge `1.1319` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.4919` n `155` status `ready` deltaP `15.0659` edge `0.4338` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1866` n `155` status `ready` deltaP `15.2892` edge `0.4762` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `4.0076` n `139` status `ready` deltaP `18.4165` edge `0.6324` maxDD `-25.3634`
- `market_context_high->equity_24h` score `2.5267` n `139` status `ready` deltaP `18.8462` edge `0.6478` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.1974` n `155` status `ready` deltaP `17.1351` edge `0.1711` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `0.7619` n `161` status `ready` deltaP `8.3916` edge `0.0717` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5406` n `139` status `ready` deltaP `12.9421` edge `0.0483` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.5174` n `155` status `ready` deltaP `8.0074` edge `0.1536` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.4555` n `161` status `ready` deltaP `4.5468` edge `0.1038` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3923` n `161` status `ready` deltaP `6.3209` edge `0.1151` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.0434` n `139` status `ready` deltaP `19.8841` edge `0.0365` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0534` n `161` status `ready` deltaP `6.3116` edge `0.05` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1125` n `161` status `ready` deltaP `4.7188` edge `0.0133` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1579` n `161` status `ready` deltaP `4.2762` edge `0.0087` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.357` n `161` status `ready` deltaP `0.0558` edge `-0.0009` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.7979` n `155` status `ready` deltaP `-0.0148` edge `0.0012` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8217` n `155` status `ready` deltaP `3.9241` edge `0.0171` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.1486` n `161` status `ready` deltaP `-1.5082` edge `-0.0048` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

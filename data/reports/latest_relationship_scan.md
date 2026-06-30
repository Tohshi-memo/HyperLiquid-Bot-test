# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T21:22:33.736142+00:00`
- Price records: `672`
- Market context records: `5287`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `24.0469` n `153` status `ready` deltaP `27.165` edge `1.8318` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.514` n `153` status `ready` deltaP `25.7353` edge `0.8696` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3236` n `177` status `ready` deltaP `16.962` edge `0.4113` maxDD `-9.46`
- `market_context_high->equity_24h` score `4.091` n `153` status `ready` deltaP `19.9653` edge `0.7707` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `4.0414` n `177` status `ready` deltaP `16.4152` edge `0.4566` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.0414` n `177` status `ready` deltaP `10.3271` edge `0.1818` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.6831` n `177` status `ready` deltaP `14.4973` edge `0.0625` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5601` n `153` status `ready` deltaP `13.3068` edge `0.0475` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3833` n `187` status `ready` deltaP `4.5446` edge `0.0978` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2545` n `153` status `ready` deltaP `20.8231` edge `0.0573` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2164` n `187` status `ready` deltaP `5.7422` edge `0.1043` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.1717` n `187` status `ready` deltaP `8.0758` edge `0.057` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0617` n `187` status `ready` deltaP `5.2091` edge `0.0105` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2555` n `177` status `ready` deltaP `7.7081` edge `0.0276` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.2902` n `187` status `ready` deltaP `2.1278` edge `0.0078` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3619` n `187` status `ready` deltaP `0.3963` edge `-0.0001` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7073` n `177` status `ready` deltaP `1.5657` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4031` n `187` status `ready` deltaP `-2.8555` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7142` n `177` status `ready` deltaP `-3.6637` edge `0.005` maxDD `-9.3609`
- `market_context_high->crypto_alt_24h` score `-2.9015` n `153` status `ready` deltaP `13.3476` edge `0.38` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

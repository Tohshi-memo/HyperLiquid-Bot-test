# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T19:52:30.751872+00:00`
- Price records: `672`
- Market context records: `2795`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.9818` n `142` status `ready` deltaP `5.0322` edge `0.2614` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.8718` n `142` status `ready` deltaP `2.5284` edge `0.5308` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.91` n `142` status `ready` deltaP `6.4904` edge `0.1379` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5797` n `142` status `ready` deltaP `11.0377` edge `0.2841` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3215` n `142` status `ready` deltaP `13.3009` edge `0.0367` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0082` n `142` status `ready` deltaP `4.4805` edge `0.0439` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.089` n `142` status `ready` deltaP `4.198` edge `0.01` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6146` n `142` status `ready` deltaP `0.7316` edge `0.0009` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6826` n `142` status `ready` deltaP `-0.7316` edge `-0.0073` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6991` n `142` status `ready` deltaP `4.9465` edge `0.0534` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.8765` n `142` status `ready` deltaP `4.2254` edge `0.0464` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9495` n `142` status `ready` deltaP `-2.45` edge `0.0205` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1581` n `142` status `ready` deltaP `-3.9054` edge `0.0074` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.1874` n `142` status `ready` deltaP `2.2673` edge `0.0239` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.4317` n `142` status `ready` deltaP `14.1854` edge `0.2202` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5492` n `142` status `ready` deltaP `-2.9269` edge `-0.0224` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6577` n `142` status `ready` deltaP `-0.6012` edge `-0.0165` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.0585` n `142` status `ready` deltaP `-0.0086` edge `-0.0088` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4441` n `142` status `ready` deltaP `5.7347` edge `0.139` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

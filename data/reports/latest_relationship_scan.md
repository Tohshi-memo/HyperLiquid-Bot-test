# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T12:37:24.063253+00:00`
- Price records: `672`
- Market context records: `2867`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `market_context_high->crypto_alt_24h` score `6.0396` n `142` status `ready` deltaP `5.3062` edge `0.8596` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.9267` n `142` status `ready` deltaP `7.2892` edge `0.3251` maxDD `-1.7175`
- `market_context_high->equity_24h` score `3.1304` n `142` status `ready` deltaP `6.651` edge `0.4169` maxDD `-12.6963`
- `market_context_high->index_24h` score `1.6454` n `142` status `ready` deltaP `8.8493` edge `0.1762` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.5349` n `142` status `ready` deltaP `14.6836` edge `0.3394` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.955` n `142` status `ready` deltaP `6.0331` edge `0.1447` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.624` n `142` status `ready` deltaP `14.9777` edge `0.0643` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.055` n `142` status `ready` deltaP `4.3308` edge `0.0488` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0244` n `142` status `ready` deltaP `4.7968` edge `0.0143` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.2066` n `142` status `ready` deltaP `4.4014` edge `0.0914` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5397` n `142` status `ready` deltaP `14.4903` edge `0.2925` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5828` n `142` status `ready` deltaP `-0.2825` edge `0.0025` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6227` n `142` status `ready` deltaP `4.9465` edge `0.0632` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6652` n `142` status `ready` deltaP `-2.0346` edge `0.0025` maxDD `-0.2164`
- `market_context_high->equity_1h` score `-0.778` n `142` status `ready` deltaP `-1.8512` edge `0.0308` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.7915` n `142` status `ready` deltaP `-0.9151` edge `-0.0108` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8095` n `142` status `ready` deltaP `4.5248` edge `0.053` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1826` n `142` status `ready` deltaP `3.2098` edge `0.019` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3879` n `142` status `ready` deltaP `-1.8852` edge `-0.0159` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

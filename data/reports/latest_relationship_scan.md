# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T11:37:26.394788+00:00`
- Price records: `672`
- Market context records: `2862`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `5.2568` n `142` status `ready` deltaP `4.6117` edge `0.799` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.684` n `142` status `ready` deltaP `6.5947` edge `0.3095` maxDD `-1.7175`
- `market_context_high->equity_24h` score `2.4305` n `142` status `ready` deltaP `5.9565` edge `0.3632` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.431` n `142` status `ready` deltaP `14.51` edge `0.3319` maxDD `-12.4171`
- `market_context_high->index_24h` score `1.3391` n `142` status `ready` deltaP `8.1548` edge `0.1553` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.9418` n `142` status `ready` deltaP `6.0331` edge `0.1436` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.512` n `142` status `ready` deltaP `14.3679` edge `0.054` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0479` n `142` status `ready` deltaP `4.1811` edge `0.0492` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0399` n `142` status `ready` deltaP `4.6471` edge `0.0133` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.4498` n `142` status `ready` deltaP `3.7916` edge `0.0752` maxDD `-5.7037`
- `market_context_high->crypto_alt_1h` score `-0.579` n `142` status `ready` deltaP `5.0962` edge `0.0678` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6046` n `142` status `ready` deltaP `-0.4322` edge `0.0007` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6688` n `142` status `ready` deltaP `-2.0346` edge `0.0022` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.6999` n `142` status `ready` deltaP `14.0329` edge `0.2822` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.7518` n `142` status `ready` deltaP `4.6745` edge `0.0594` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.7612` n `142` status `ready` deltaP `-1.7015` edge `0.0312` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.7853` n `142` status `ready` deltaP `-0.7654` edge `-0.011` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2431` n `142` status `ready` deltaP `2.7525` edge `0.0143` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3891` n `142` status `ready` deltaP `-1.8852` edge `-0.016` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

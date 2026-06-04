# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T23:37:24.920866+00:00`
- Price records: `672`
- Market context records: `2914`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `12.8657` n `142` status `ready` deltaP `12.077` edge `1.3833` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.4571` n `142` status `ready` deltaP `14.2899` edge `0.6432` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.7366` n `142` status `ready` deltaP `12.4975` edge `0.4412` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.185` n `142` status `ready` deltaP `10.2382` edge `0.2119` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7904` n `142` status `ready` deltaP `15.5516` edge `0.3549` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4899` n `142` status `ready` deltaP `13.1484` edge `0.0593` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.3217` n `142` status `ready` deltaP `6.5355` edge `0.1212` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1443` n `142` status `ready` deltaP `4.5087` edge `0.0873` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.036` n `142` status `ready` deltaP `4.198` edge `0.0168` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.1221` n `142` status `ready` deltaP `15.4049` edge `0.3212` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.2821` n `142` status `ready` deltaP `4.1811` edge `0.0217` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.3956` n `142` status `ready` deltaP `0.6937` edge `0.0457` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4644` n `142` status `ready` deltaP `6.1441` edge `0.0755` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5514` n `142` status `ready` deltaP `-0.6873` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6132` n `142` status `ready` deltaP `-0.7316` edge `0.0016` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6263` n `142` status `ready` deltaP `6.0218` edge `0.0665` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6598` n `142` status `ready` deltaP `-0.1666` edge `0.0011` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.985` n `142` status `ready` deltaP `-1.7713` edge `0.0076` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2464` n `142` status `ready` deltaP `2.4476` edge `0.0159` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2744` n `142` status `ready` deltaP `-1.7116` edge `-0.0076` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

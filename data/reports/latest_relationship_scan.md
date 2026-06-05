# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T00:37:21.453447+00:00`
- Price records: `672`
- Market context records: `2919`
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

- `market_context_high->crypto_alt_24h` score `13.4804` n `142` status `ready` deltaP `12.7715` edge `1.4299` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.6543` n `142` status `ready` deltaP `14.9843` edge `0.655` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.9637` n `142` status `ready` deltaP `13.192` edge `0.4555` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2566` n `142` status `ready` deltaP `10.759` edge `0.2144` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8192` n `142` status `ready` deltaP `15.5516` edge `0.3573` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5267` n `142` status `ready` deltaP `13.3009` edge `0.063` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.4411` n `142` status `ready` deltaP `6.9929` edge `0.1281` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.0995` n `142` status `ready` deltaP `4.2039` edge `0.0856` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.022` n `142` status `ready` deltaP `4.198` edge `0.0186` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0717` n `142` status `ready` deltaP `15.4049` edge `0.3254` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.3361` n `142` status `ready` deltaP `4.0314` edge `0.0182` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.3524` n `142` status `ready` deltaP `0.8434` edge `0.0483` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4777` n `142` status `ready` deltaP `5.9944` edge `0.0748` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5263` n `142` status `ready` deltaP `-0.3879` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.606` n `142` status `ready` deltaP `0.4322` edge `0.004` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6217` n `142` status `ready` deltaP `-0.8813` edge `0.0015` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6442` n `142` status `ready` deltaP `5.8721` edge `0.0652` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.9862` n `142` status `ready` deltaP `-1.7713` edge `0.0075` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2646` n `142` status `ready` deltaP `2.1427` edge `0.0156` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2732` n `142` status `ready` deltaP `-1.7116` edge `-0.0075` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

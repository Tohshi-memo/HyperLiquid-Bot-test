# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T02:22:30.293419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `56.9387` n `50` status `ready` deltaP `19.0641` edge `4.6178` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6859` n `50` status `ready` deltaP `46.6066` edge `2.6239` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.8078` n `50` status `ready` deltaP `27.5009` edge `0.6833` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.8327` n `71` status `ready` deltaP `17.8911` edge `0.6478` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.0003` n `50` status `ready` deltaP `30.1005` edge `0.4755` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.2474` n `120` status `ready` deltaP `12.3974` edge `0.5112` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4946` n `50` status `ready` deltaP `43.4073` edge `0.0894` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3118` n `120` status `ready` deltaP `28.7406` edge `0.1863` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7529` n `77` status `ready` deltaP `6.4061` edge `0.2224` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4646` n `50` status `ready` deltaP `26.9948` edge `0.0405` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2753` n `120` status `ready` deltaP `17.5508` edge `0.1133` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2625` n `71` status `ready` deltaP `33.0685` edge `0.023` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9431` n `120` status `ready` deltaP `9.2416` edge `0.062` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5718` n `77` status `ready` deltaP `12.1355` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3936` n `77` status `ready` deltaP `11.6378` edge `0.0049` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.049` n `120` status `ready` deltaP `11.0162` edge `0.012` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3639` n `120` status `ready` deltaP `4.0619` edge `-0.0005` maxDD `-0.8587`
- `market_context_high->crypto_major_4h` score `-0.4169` n `120` status `ready` deltaP `13.7906` edge `0.2184` maxDD `-20.9394`
- `news_risk_high->index_1h` score `-0.4489` n `77` status `ready` deltaP `-0.7465` edge `-0.0089` maxDD `-0.8275`
- `market_context_high->crypto_alt_4h` score `-0.5039` n `120` status `ready` deltaP `15.4674` edge `0.3169` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T01:07:27.688925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9964`

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

- `market_context_high->unknown_4h` score `41.8798` n `51` status `ready` deltaP `7.3171` edge `3.4412` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `23.5355` n `51` status `ready` deltaP `15.6148` edge `2.1511` maxDD `-21.179`
- `market_context_high->equity_24h` score `11.7402` n `51` status `ready` deltaP `8.8439` edge `1.0485` maxDD `-7.9954`
- `news_risk_high->crypto_major_24h` score `10.5138` n `101` status `ready` deltaP `-0.3627` edge `1.5644` maxDD `-46.1999`
- `market_context_high->crypto_alt_24h` score `8.4725` n `51` status `ready` deltaP `13.9808` edge `0.8992` maxDD `-21.2421`
- `news_risk_high->crypto_alt_24h` score `6.0222` n `101` status `ready` deltaP `0.0223` edge `0.9898` maxDD `-32.7147`
- `market_context_high->index_24h` score `4.0993` n `51` status `ready` deltaP `12.837` edge `0.2958` maxDD `-0.8486`
- `news_risk_high->crypto_alt_4h` score `3.0028` n `101` status `ready` deltaP `14.6507` edge `0.2735` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.5624` n `101` status `ready` deltaP `31.5302` edge `0.2489` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3265` n `101` status `ready` deltaP `14.2853` edge `0.1452` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1332` n `101` status `ready` deltaP `16.3276` edge `0.1947` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6467` n `101` status `ready` deltaP `16.0817` edge `0.0823` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.6215` n `51` status `ready` deltaP `4.8257` edge `0.0444` maxDD `-0.3155`
- `news_risk_high->fx_4h` score `0.5604` n `101` status `ready` deltaP `12.2992` edge `0.0283` maxDD `-0.421`
- `market_context_high->index_4h` score `0.5419` n `51` status `ready` deltaP `15.4322` edge `0.0083` maxDD `-0.6704`
- `market_context_high->index_1h` score `0.5279` n `51` status `ready` deltaP `8.8823` edge `0.0101` maxDD `-0.0259`
- `news_risk_high->metal_1h` score `0.4687` n `101` status `ready` deltaP `13.101` edge `0.0119` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.1979` n `101` status `ready` deltaP `13.4403` edge `0.0323` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.1285` n `51` status `ready` deltaP `6.1142` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->fx_1h` score `0.0176` n `101` status `ready` deltaP `5.6871` edge `0.0079` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

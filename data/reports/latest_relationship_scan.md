# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T16:37:16.461751+00:00`
- Price records: `672`
- Market context records: `884`
- Flow alert records: `2483`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.5872` n `32` status `ready` deltaP `32.4653` edge `1.5825` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.5872` n `32` status `ready` deltaP `32.4653` edge `1.5825` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.7303` n `167` status `ready` deltaP `28.8725` edge `0.9851` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.3438` n `32` status `ready` deltaP `25.3472` edge `0.943` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.3438` n `32` status `ready` deltaP `25.3472` edge `0.943` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.8979` n `32` status `ready` deltaP `7.6389` edge `1.0239` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.8979` n `32` status `ready` deltaP `7.6389` edge `1.0239` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8716` n `167` status `ready` deltaP `7.0401` edge `0.5305` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.3013` n `32` status `ready` deltaP `27.9514` edge `0.1721` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.3013` n `32` status `ready` deltaP `27.9514` edge `0.1721` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5038` n `32` status `ready` deltaP `8.4604` edge `0.2721` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5038` n `32` status `ready` deltaP `8.4604` edge `0.2721` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.4789` n `32` status `ready` deltaP `24.1616` edge `0.1493` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.4789` n `32` status `ready` deltaP `24.1616` edge `0.1493` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `3.0813` n `32` status `ready` deltaP `22.2561` edge `0.1456` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.0813` n `32` status `ready` deltaP `22.2561` edge `0.1456` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5667` n `32` status `ready` deltaP `14.1006` edge `0.1287` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5667` n `32` status `ready` deltaP `14.1006` edge `0.1287` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.5167` n `32` status `ready` deltaP `-8.6806` edge `0.3269` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.5167` n `32` status `ready` deltaP `-8.6806` edge `0.3269` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

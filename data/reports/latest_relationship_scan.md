# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T10:37:25.460463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10935`

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

- `risk_on_high->unknown_4h` score `22.069` n `143` status `ready` deltaP `8.7466` edge `1.8426` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.069` n `143` status `ready` deltaP `8.7466` edge `1.8426` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `11.1312` n `228` status `ready` deltaP `8.673` edge `0.9428` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3943` n `37` status `ready` deltaP `25.1783` edge `0.4753` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.1241` n `37` status `ready` deltaP `22.9167` edge `0.1909` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5922` n `37` status `ready` deltaP `17.1803` edge `0.2261` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.164` n `37` status `ready` deltaP `21.7123` edge `0.0577` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `2.0092` n `37` status `ready` deltaP `12.6483` edge `0.1032` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6374` n `37` status `ready` deltaP `13.6835` edge `0.0843` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.2218` n `37` status `ready` deltaP `6.6152` edge `0.076` maxDD `-0.4628`
- `news_risk_high->metal_1h` score `1.2083` n `37` status `ready` deltaP `14.4158` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `0.8662` n `37` status `ready` deltaP `8.4278` edge `0.0425` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.755` n `37` status `ready` deltaP `15.3623` edge `0.272` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.5243` n `37` status `ready` deltaP `6.3983` edge `0.0339` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.3734` n `37` status `ready` deltaP `13.7059` edge `0.0413` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.2664` n `129` status `ready` deltaP `21.7943` edge `0.7513` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2664` n `129` status `ready` deltaP `21.7943` edge `0.7513` maxDD `-56.9519`
- `market_context_high->equity_24h` score `0.0894` n `192` status `ready` deltaP `15.7986` edge `0.3407` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.0835` n `152` status `ready` deltaP `12.0509` edge `0.0016` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

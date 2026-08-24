# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T01:07:27.270296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `47.7183` n `42` status `ready` deltaP `25.1736` edge `3.8087` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.955` n `42` status `ready` deltaP `43.7748` edge `0.9781` maxDD `-0.5615`
- `news_risk_high->unknown_4h` score `11.6775` n `51` status `ready` deltaP `26.2404` edge `0.8032` maxDD `-0.0674`
- `news_risk_high->index_24h` score `6.0145` n `42` status `ready` deltaP `15.3026` edge `0.4291` maxDD `-1.0593`
- `news_risk_high->crypto_alt_24h` score `4.7076` n `42` status `ready` deltaP `28.125` edge `0.2048` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2658` n `37` status `ready` deltaP `18.8571` edge `0.1748` maxDD `-0.6023`
- `risk_on_and_context->equity_4h` score `3.2658` n `37` status `ready` deltaP `18.8571` edge `0.1748` maxDD `-0.6023`
- `risk_on_high->unknown_1h` score `3.2528` n `37` status `ready` deltaP `-7.9139` edge `0.5123` maxDD `-1.4012`
- `risk_on_and_context->unknown_1h` score `3.2528` n `37` status `ready` deltaP `-7.9139` edge `0.5123` maxDD `-1.4012`
- `news_risk_high->index_4h` score `2.8997` n `51` status `ready` deltaP `24.8625` edge `0.0821` maxDD `-0.1636`
- `news_risk_high->unknown_1h` score `2.8346` n `51` status `ready` deltaP `17.6822` edge `0.1476` maxDD `-0.6742`
- `news_risk_high->metal_24h` score `2.4223` n `42` status `ready` deltaP `40.1042` edge `-0.0655` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3527` n `37` status `ready` deltaP `30.6526` edge `0.0005` maxDD `-0.0367`
- `news_risk_high->fx_24h` score `1.9012` n `42` status `ready` deltaP `2.5297` edge `0.3385` maxDD `-1.2626`
- `market_context_high->unknown_4h` score `1.8742` n `144` status `ready` deltaP `21.9512` edge `0.0189` maxDD `-0.0578`
- `market_context_high->unknown_1h` score `1.197` n `156` status `ready` deltaP `7.7652` edge `0.0905` maxDD `-1.4012`
- `news_risk_high->equity_1h` score `1.0261` n `51` status `ready` deltaP `19.1059` edge `0.0492` maxDD `-0.9349`
- `news_risk_high->equity_4h` score `0.7508` n `51` status `ready` deltaP `14.5116` edge `0.1348` maxDD `-5.4894`
- `risk_on_high->unknown_4h` score `0.4681` n `37` status `ready` deltaP `28.2012` edge `-0.149` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

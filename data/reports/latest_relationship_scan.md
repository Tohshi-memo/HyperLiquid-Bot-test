# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T02:07:27.161209+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.8093` n `110` status `ready` deltaP `28.6142` edge `0.983` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8093` n `110` status `ready` deltaP `28.6142` edge `0.983` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.0644` n `232` status `ready` deltaP `21.0907` edge `0.6975` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.1874` n `110` status `ready` deltaP `36.9179` edge `0.39` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.1874` n `110` status `ready` deltaP `36.9179` edge `0.39` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.8013` n `110` status `ready` deltaP `22.7778` edge `1.1269` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.8013` n `110` status `ready` deltaP `22.7778` edge `1.1269` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.0187` n `110` status `ready` deltaP `26.8043` edge `0.3254` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0187` n `110` status `ready` deltaP `26.8043` edge `0.3254` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8907` n `110` status `ready` deltaP `29.0435` edge `0.0515` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8907` n `110` status `ready` deltaP `29.0435` edge `0.0515` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.3435` n `232` status `ready` deltaP `12.6736` edge `0.1108` maxDD `0.0`
- `market_context_high->index_24h` score `2.1939` n `232` status `ready` deltaP `24.0122` edge `0.0621` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.3727` n `110` status `ready` deltaP `12.6736` edge `0.0299` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3727` n `110` status `ready` deltaP `12.6736` edge `0.0299` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0768` n `110` status `ready` deltaP `4.1508` edge `0.0973` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0768` n `110` status `ready` deltaP `4.1508` edge `0.0973` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5037` n `110` status `ready` deltaP `14.7932` edge `-0.0035` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5037` n `110` status `ready` deltaP `14.7932` edge `-0.0035` maxDD `-2.2516`
- `risk_on_high->metal_24h` score `0.4635` n `110` status `ready` deltaP `17.8346` edge `0.0561` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

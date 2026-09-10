# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T04:52:24.924602+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.6565` n `99` status `ready` deltaP `30.0189` edge `0.9609` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6565` n `99` status `ready` deltaP `30.0189` edge `0.9609` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.6143` n `221` status `ready` deltaP `22.3997` edge `0.7346` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2454` n `99` status `ready` deltaP `37.3275` edge `0.3921` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2454` n `99` status `ready` deltaP `37.3275` edge `0.3921` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.2289` n `99` status `ready` deltaP `21.3542` edge `0.9348` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.2289` n `99` status `ready` deltaP `21.3542` edge `0.9348` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1395` n `99` status `ready` deltaP `26.3489` edge `0.3385` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1395` n `99` status `ready` deltaP `26.3489` edge `0.3385` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9689` n `99` status `ready` deltaP `30.6503` edge `0.0473` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9689` n `99` status `ready` deltaP `30.6503` edge `0.0473` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6727` n `221` status `ready` deltaP `14.5833` edge `0.1255` maxDD `0.0`
- `market_context_high->index_24h` score `2.3494` n `221` status `ready` deltaP `25.5358` edge `0.0649` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.2113` n `99` status `ready` deltaP `5.2169` edge `0.1014` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.2113` n `99` status `ready` deltaP `5.2169` edge `0.1014` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `1.1565` n `99` status `ready` deltaP `21.4154` edge `-0.0123` maxDD `-1.0611`
- `risk_on_and_context->equity_4h` score `1.1565` n `99` status `ready` deltaP `21.4154` edge `-0.0123` maxDD `-1.0611`
- `risk_on_high->commodity_24h` score `1.1355` n `99` status `ready` deltaP `11.9318` edge `0.036` maxDD `-0.3404`
- `risk_on_and_context->commodity_24h` score `1.1355` n `99` status `ready` deltaP `11.9318` edge `0.036` maxDD `-0.3404`
- `risk_on_high->equity_24h` score `1.0743` n `99` status `ready` deltaP `14.5833` edge `-0.0077` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

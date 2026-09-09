# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T21:07:28.435025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10146`

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

- `risk_on_high->crypto_alt_24h` score `11.9573` n `117` status `ready` deltaP `25.414` edge `0.85` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.9573` n `117` status `ready` deltaP `25.414` edge `0.85` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `6.9099` n `241` status `ready` deltaP `18.0692` edge `0.5381` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.3592` n `117` status `ready` deltaP `21.1005` edge `1.0814` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.3592` n `117` status `ready` deltaP `21.1005` edge `1.0814` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.0965` n `117` status `ready` deltaP `34.1411` edge `0.3176` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.0965` n `117` status `ready` deltaP `34.1411` edge `0.3176` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.2427` n `117` status `ready` deltaP `24.3043` edge `0.2774` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2427` n `117` status `ready` deltaP `24.3043` edge `0.2774` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.5588` n `117` status `ready` deltaP `25.7345` edge `0.0459` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.5588` n `117` status `ready` deltaP `25.7345` edge `0.0459` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.8373` n `241` status `ready` deltaP `20.8297` edge `0.0536` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.5149` n `241` status `ready` deltaP `9.2014` edge `0.0649` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0293` n `117` status `ready` deltaP `4.097` edge `0.0937` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0293` n `117` status `ready` deltaP `4.097` edge `0.0937` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.8297` n `117` status `ready` deltaP `9.2014` edge `0.0078` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.8297` n `117` status `ready` deltaP `9.2014` edge `0.0078` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7777` n `117` status `ready` deltaP `19.7383` edge `0.0837` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7777` n `117` status `ready` deltaP `19.7383` edge `0.0837` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4257` n `117` status `ready` deltaP `14.2229` edge `-0.0062` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

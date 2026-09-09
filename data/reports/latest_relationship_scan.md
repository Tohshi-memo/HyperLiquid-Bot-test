# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T23:21:58.844451+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.4095` n `117` status `ready` deltaP `26.9765` edge `0.9606` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.4095` n `117` status `ready` deltaP `26.9765` edge `0.9606` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.3621` n `241` status `ready` deltaP `19.6317` edge `0.6487` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.3117` n `117` status `ready` deltaP `22.663` edge `1.1931` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3117` n `117` status `ready` deltaP `22.663` edge `1.1931` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.7907` n `117` status `ready` deltaP `35.5131` edge `0.3663` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.7907` n `117` status `ready` deltaP `35.5131` edge `0.3663` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.7665` n `117` status `ready` deltaP `25.6762` edge `0.3119` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.7665` n `117` status `ready` deltaP `25.6762` edge `0.3119` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.739` n `117` status `ready` deltaP `27.297` edge `0.0505` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.739` n `117` status `ready` deltaP `27.297` edge `0.0505` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.0175` n `241` status `ready` deltaP `22.3922` edge `0.0582` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.9879` n `241` status `ready` deltaP `10.7639` edge `0.0939` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.3027` n `117` status `ready` deltaP `10.7639` edge `0.0368` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3027` n `117` status `ready` deltaP `10.7639` edge `0.0368` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.2416` n `117` status `ready` deltaP `4.8455` edge `0.1064` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.2416` n `117` status `ready` deltaP `4.8455` edge `0.1064` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.8097` n `117` status `ready` deltaP `19.7383` edge `0.0878` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8097` n `117` status `ready` deltaP `19.7383` edge `0.0878` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.5072` n `117` status `ready` deltaP `14.9714` edge `-0.0044` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

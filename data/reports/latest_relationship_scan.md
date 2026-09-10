# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T19:52:33.914272+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `12090`

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

- `risk_on_high->crypto_alt_24h` score `19.9532` n `91` status `ready` deltaP `36.1722` edge `1.4446` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.9532` n `91` status `ready` deltaP `36.1722` edge `1.4446` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.3645` n `201` status `ready` deltaP `27.7364` edge `1.1782` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.1112` n `91` status `ready` deltaP `42.8605` edge `0.5107` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.1112` n `91` status `ready` deltaP `42.8605` edge `0.5107` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.8181` n `91` status `ready` deltaP `33.1161` edge `0.5166` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8181` n `91` status `ready` deltaP `33.1161` edge `0.5166` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2604` n `91` status `ready` deltaP `25.021` edge `1.1708` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2604` n `91` status `ready` deltaP `25.021` edge `1.1708` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.212` n `201` status `ready` deltaP `25.0` edge `0.351` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.6184` n `91` status `ready` deltaP `25.0` edge `0.2182` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.6184` n `91` status `ready` deltaP `25.0` edge `0.2182` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1949` n `91` status `ready` deltaP `40.8005` edge `0.0818` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.1949` n `91` status `ready` deltaP `40.8005` edge `0.0818` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.3231` n `201` status `ready` deltaP `35.142` edge `0.082` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.0276` n `91` status `ready` deltaP `29.8395` edge `0.0627` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `3.0276` n `91` status `ready` deltaP `29.8395` edge `0.0627` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.902` n `201` status `ready` deltaP `23.0001` edge `0.0907` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.5133` n `91` status `ready` deltaP `20.1356` edge `0.0197` maxDD `-0.2263`
- `risk_on_and_context->equity_1h` score `1.5133` n `91` status `ready` deltaP `20.1356` edge `0.0197` maxDD `-0.2263`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

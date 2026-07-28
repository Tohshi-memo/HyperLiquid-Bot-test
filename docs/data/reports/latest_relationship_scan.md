# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T14:22:35.926230+00:00`
- Price records: `672`
- Market context records: `8204`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8212.9887` n `43` status `ready` deltaP `36.9792` edge `684.1692` maxDD `0.0`
- `market_context_high->equity_24h` score `22.6551` n `37` status `ready` deltaP `43.9283` edge `1.6861` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5357` n `38` status `ready` deltaP `46.7586` edge `0.4872` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.0686` n `37` status `ready` deltaP `47.2222` edge `0.4409` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.8948` n `37` status `ready` deltaP `23.522` edge `1.1099` maxDD `-5.1085`
- `market_context_high->crypto_major_24h` score `7.5543` n `37` status `ready` deltaP `23.0012` edge `1.0416` maxDD `-13.1148`
- `news_risk_high->equity_4h` score `7.0209` n `54` status `ready` deltaP `25.3161` edge `0.476` maxDD `-3.4427`
- `market_context_high->index_4h` score `4.042` n `38` status `ready` deltaP `38.4468` edge `0.0848` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.8247` n `38` status `ready` deltaP `37.492` edge `0.0866` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.2746` n `38` status `ready` deltaP `16.9241` edge `0.1747` maxDD `-0.1718`
- `market_context_high->index_24h` score `3.2467` n `37` status `ready` deltaP `31.4565` edge `0.2685` maxDD `-0.9576`
- `market_context_high->crypto_alt_4h` score `3.2383` n `38` status `ready` deltaP `12.4679` edge `0.225` maxDD `-1.3942`
- `news_risk_high->equity_1h` score `3.1889` n `54` status `ready` deltaP `22.5771` edge `0.1461` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `2.7194` n `54` status `ready` deltaP `13.8325` edge `0.3258` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6567` n `54` status `ready` deltaP `22.2674` edge `0.092` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `2.0285` n `54` status `ready` deltaP `13.7503` edge `0.1171` maxDD `-1.1783`
- `market_context_high->crypto_major_4h` score `2.001` n `38` status `ready` deltaP `15.0995` edge `0.2523` maxDD `-4.0473`
- `news_risk_high->crypto_alt_1h` score `1.9094` n `54` status `ready` deltaP `15.3027` edge `0.1005` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.8189` n `37` status `ready` deltaP `34.0372` edge `0.0711` maxDD `-0.5196`
- `market_context_high->metal_1h` score `1.5141` n `38` status `ready` deltaP `17.2235` edge `0.0288` maxDD `-0.0623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

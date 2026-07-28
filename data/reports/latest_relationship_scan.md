# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T13:22:35.178484+00:00`
- Price records: `672`
- Market context records: `8200`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8314.9431` n `43` status `ready` deltaP `36.9792` edge `692.6654` maxDD `0.0`
- `market_context_high->equity_24h` score `21.8148` n `41` status `ready` deltaP `45.0796` edge `1.6084` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.6194` n `42` status `ready` deltaP `46.3995` edge `0.5799` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.049` n `41` status `ready` deltaP `46.5278` edge `0.4439` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.1516` n `41` status `ready` deltaP `17.721` edge `0.9762` maxDD `-7.8644`
- `news_risk_high->equity_4h` score `6.6793` n `54` status `ready` deltaP `24.7064` edge `0.4516` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `4.7441` n `41` status `ready` deltaP `17.2002` edge `0.8184` maxDD `-19.6551`
- `market_context_high->index_4h` score `4.2489` n `42` status `ready` deltaP `38.5888` edge `0.1011` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9187` n `42` status `ready` deltaP `38.0372` edge `0.0908` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.7109` n `42` status `ready` deltaP `19.3328` edge `0.195` maxDD `-0.1718`
- `news_risk_high->equity_1h` score `2.9526` n `54` status `ready` deltaP `21.9783` edge `0.1304` maxDD `-1.1366`
- `market_context_high->index_24h` score `2.7488` n `41` status `ready` deltaP `24.8645` edge `0.2492` maxDD `-1.0044`
- `news_risk_high->crypto_major_4h` score `2.7132` n `54` status `ready` deltaP `13.8325` edge `0.325` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.5816` n `54` status `ready` deltaP `21.6576` edge `0.0898` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `1.9937` n `54` status `ready` deltaP `13.6006` edge `0.1152` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8494` n `54` status `ready` deltaP `15.0033` edge `0.0975` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.7219` n `41` status `ready` deltaP `32.5034` edge `0.0689` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4409` n `54` status `ready` deltaP `17.5362` edge `0.207` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3852` n `42` status `ready` deltaP `24.558` edge `0.0277` maxDD `-0.1069`
- `market_context_high->crypto_alt_4h` score `1.3501` n `42` status `ready` deltaP `6.9542` edge `0.1926` maxDD `-2.2695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

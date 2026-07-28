# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T19:07:37.207253+00:00`
- Price records: `672`
- Market context records: `8225`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.0941` n `43` status `ready` deltaP `38.0208` edge `662.8377` maxDD `0.0`
- `market_context_high->equity_24h` score `21.914` n `30` status `ready` deltaP `38.2639` edge `1.6621` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.5365` n `30` status `ready` deltaP `36.875` edge `1.3883` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.5074` n `30` status `ready` deltaP `38.4375` edge `1.2697` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9335` n `30` status `ready` deltaP `47.8862` edge `0.4295` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.3238` n `30` status `ready` deltaP `47.1875` edge `0.3892` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.4084` n `54` status `ready` deltaP `27.1454` edge `0.4961` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.5409` n `30` status `ready` deltaP `28.6484` edge `0.372` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8775` n `30` status `ready` deltaP `37.743` edge `0.2775` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `4.9496` n `30` status `ready` deltaP `23.5061` edge `0.276` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8273` n `30` status `ready` deltaP `37.4085` edge `0.0826` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.5356` n `30` status `ready` deltaP `35.7317` edge `0.0607` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1553` n `54` status `ready` deltaP `22.5771` edge `0.1433` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7406` n `30` status `ready` deltaP `45.3819` edge `0.0819` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.596` n `54` status `ready` deltaP `21.6576` edge `0.091` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3187` n `54` status `ready` deltaP `11.241` edge `0.2917` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8386` n `54` status `ready` deltaP `15.0033` edge `0.0966` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.8031` n `54` status `ready` deltaP `12.403` edge `0.1073` maxDD `-1.1783`
- `market_context_high->equity_1h` score `1.7201` n `30` status `ready` deltaP `8.503` edge `0.1013` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.3739` n `30` status `ready` deltaP `13.1437` edge `0.0464` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

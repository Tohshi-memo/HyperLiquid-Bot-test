# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T17:22:37.010006+00:00`
- Price records: `672`
- Market context records: `8218`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5936`

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

- `news_risk_high->unknown_24h` score `7957.1955` n `43` status `ready` deltaP `36.9792` edge `662.8531` maxDD `0.0`
- `market_context_high->equity_24h` score `21.5516` n `30` status `ready` deltaP `38.2639` edge `1.6319` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.3289` n `30` status `ready` deltaP `36.875` edge `1.371` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.132` n `30` status `ready` deltaP `37.5694` edge `1.2442` maxDD `-3.0264`
- `market_context_high->equity_4h` score `9.0055` n `30` status `ready` deltaP `47.8862` edge `0.4355` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.1198` n `30` status `ready` deltaP `45.9723` edge `0.3803` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.4804` n `54` status `ready` deltaP `27.1454` edge `0.5021` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.7389` n `30` status `ready` deltaP `29.563` edge `0.3824` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8511` n `30` status `ready` deltaP `37.743` edge `0.2753` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `4.982` n `30` status `ready` deltaP `23.5061` edge `0.2787` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8503` n `30` status `ready` deltaP `37.561` edge `0.0835` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.5877` n `30` status `ready` deltaP `36.189` edge `0.062` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1708` n `54` status `ready` deltaP `22.8765` edge `0.1426` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7344` n `30` status `ready` deltaP `45.3819` edge `0.0811` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6481` n `54` status `ready` deltaP `22.1149` edge `0.0923` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.4473` n `54` status `ready` deltaP `12.1556` edge `0.3021` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8126` n `54` status `ready` deltaP `12.7024` edge `0.1061` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7643` n `54` status `ready` deltaP `14.5542` edge `0.0934` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.7356` n `30` status `ready` deltaP `8.8024` edge `0.1006` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.3835` n `30` status `ready` deltaP `13.4431` edge `0.0452` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

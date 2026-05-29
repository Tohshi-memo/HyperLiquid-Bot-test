# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T12:37:20.460916+00:00`
- Price records: `672`
- Market context records: `2245`
- Flow alert records: `8355`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.2327` n `40` status `ready` deltaP `55.2431` edge `1.7933` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.2564` n `40` status `ready` deltaP `45.0694` edge `1.0982` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.4539` n `40` status `ready` deltaP `36.0417` edge `1.079` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.0014` n `131` status `ready` deltaP `32.2821` edge `0.8827` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.8345` n `131` status `ready` deltaP `38.5473` edge `0.7047` maxDD `-2.3715`
- `news_risk_high->unknown_24h` score `9.8481` n `40` status `ready` deltaP `36.1458` edge `0.6023` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `9.2015` n `118` status `ready` deltaP `30.1289` edge `0.652` maxDD `-5.2188`
- `news_risk_high->crypto_major_24h` score `8.7947` n `40` status `ready` deltaP `23.9236` edge `1.0261` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `6.4955` n `118` status `ready` deltaP `18.288` edge `1.1001` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.8115` n `131` status `ready` deltaP `22.0606` edge `0.3826` maxDD `-1.6306`
- `market_context_high->index_4h` score `4.1329` n `131` status `ready` deltaP `31.5409` edge `0.1715` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.8998` n `43` status `ready` deltaP `33.2246` edge `0.3456` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.6402` n `131` status `ready` deltaP `22.5377` edge `0.2358` maxDD `-2.9497`
- `news_risk_high->fx_24h` score `3.5251` n `40` status `ready` deltaP `35.6597` edge `0.0745` maxDD `-0.1442`
- `news_risk_high->index_24h` score `3.482` n `40` status `ready` deltaP `12.7431` edge `0.2471` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.3691` n `118` status `ready` deltaP `14.0567` edge `0.2388` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.1194` n `118` status `ready` deltaP `21.5925` edge `0.2687` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.5308` n `143` status `ready` deltaP `14.6351` edge `0.1997` maxDD `-4.9097`
- `market_context_high->crypto_major_1h` score `2.1764` n `143` status `ready` deltaP `13.5359` edge `0.1709` maxDD `-3.0485`
- `news_risk_high->fx_4h` score `2.15` n `43` status `ready` deltaP `27.2794` edge `0.0157` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

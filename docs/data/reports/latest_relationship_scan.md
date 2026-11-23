# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T06:37:28.045891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5232`

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

- `market_context_high->unknown_1h` score `16475.0738` n `82` status `ready` deltaP `2.4134` edge `1372.9229` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10750.8985` n `82` status `ready` deltaP `3.5061` edge `895.8987` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1326.2987` n `31` status `ready` deltaP `3.2789` edge `110.5206` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1169.5609` n `31` status `ready` deltaP `3.9388` edge `97.4428` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.1639` n `31` status `ready` deltaP `36.1576` edge `0.7375` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.5706` n `31` status `ready` deltaP `24.0165` edge `0.8078` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3585` n `31` status `ready` deltaP `12.6623` edge `0.8725` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7388` n `31` status `ready` deltaP `18.6401` edge `0.206` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4614` n `31` status `ready` deltaP `36.31` edge `0.0724` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6387` n `31` status `ready` deltaP `30.9446` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.366` n `31` status `ready` deltaP `9.1124` edge `0.2887` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9661` n `31` status `ready` deltaP `7.6154` edge `0.237` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4924` n `31` status `ready` deltaP `28.5348` edge `0.029` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4458` n `31` status `ready` deltaP `19.9793` edge `0.1079` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8351` n `31` status `ready` deltaP `18.1255` edge `0.026` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.2305` n `82` status `ready` deltaP `12.0427` edge `0.0137` maxDD `-0.4876`
- `news_risk_high->commodity_1h` score `-0.0513` n `31` status `ready` deltaP `1.3811` edge `0.0127` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.0779` n `82` status `ready` deltaP `4.3413` edge `0.0129` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1131` n `82` status `ready` deltaP `3.9579` edge `0.0047` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.8704` n `82` status `ready` deltaP `7.4695` edge `0.0181` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

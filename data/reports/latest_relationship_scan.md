# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T03:07:31.785886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8956` n `91` status `ready` deltaP `-3.5965` edge `3.4025` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.2264` n `43` status `ready` deltaP `43.4451` edge `0.8959` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.3238` n `43` status `ready` deltaP `43.9768` edge `0.8239` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.0597` n `43` status `ready` deltaP `28.5449` edge `0.7413` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.6749` n `90` status `ready` deltaP `22.0139` edge `1.391` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.84` n `90` status `ready` deltaP `28.9583` edge `0.5865` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8853` n `43` status `ready` deltaP `49.8264` edge `0.2416` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1747` n `43` status `ready` deltaP `33.2672` edge `0.3133` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5717` n `43` status `ready` deltaP `45.0829` edge `0.0849` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.7104` n `43` status `ready` deltaP `15.8752` edge `0.2389` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.4068` n `90` status `ready` deltaP `13.5417` edge `0.9403` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.904` n `43` status `ready` deltaP `7.1717` edge `0.2259` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.6351` n `43` status `ready` deltaP `31.6251` edge `0.0177` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.2207` n `43` status `ready` deltaP `28.6821` edge `0.0023` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7544` n `91` status `ready` deltaP `17.8588` edge `0.2389` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.1967` n `43` status `ready` deltaP `19.0797` edge `0.0678` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.1488` n `90` status `ready` deltaP `20.2777` edge `0.1606` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.5771` n `43` status `ready` deltaP `12.0422` edge `0.0242` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.4152` n `91` status `ready` deltaP `8.4935` edge `0.0022` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.4066` n `91` status `ready` deltaP `14.6191` edge `0.0111` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T12:22:28.719948+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2242.2575` n `114` status `ready` deltaP `-7.0998` edge `186.9451` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `93.9162` n `98` status `ready` deltaP `-5.493` edge `7.8916` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `57.1928` n `114` status `ready` deltaP `1.3291` edge `4.7705` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.3013` n `43` status `ready` deltaP `45.8696` edge `1.1411` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.4646` n `114` status `ready` deltaP `25.795` edge `0.9758` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.899` n `98` status `ready` deltaP `18.0283` edge `0.4267` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.6177` n `114` status `ready` deltaP `42.0779` edge `0.1226` maxDD `-0.1315`
- `market_context_high->metal_4h` score `0.9541` n `114` status `ready` deltaP `19.4855` edge `0.0375` maxDD `-0.9401`
- `news_risk_high->crypto_alt_1h` score `0.8768` n `98` status `ready` deltaP `7.7966` edge `0.104` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5857` n `114` status `ready` deltaP `13.1999` edge `0.0161` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.4617` n `114` status `ready` deltaP `4.6534` edge `0.1675` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.2022` n `114` status `ready` deltaP `4.2573` edge `0.0851` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.1989` n `114` status `ready` deltaP `7.4456` edge `0.0697` maxDD `-5.2213`
- `market_context_high->metal_24h` score `0.0123` n `114` status `ready` deltaP `11.6502` edge `0.1886` maxDD `-10.5088`
- `market_context_high->fx_1h` score `-0.0083` n `114` status `ready` deltaP `4.6434` edge `-0.0008` maxDD `-0.1642`
- `market_context_high->commodity_4h` score `-0.0318` n `114` status `ready` deltaP `10.1412` edge `0.0502` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.3565` n `114` status `ready` deltaP `3.1291` edge `-0.0015` maxDD `-0.2591`
- `market_context_high->commodity_1h` score `-0.5342` n `114` status `ready` deltaP `-0.9429` edge `0.0132` maxDD `-0.4475`
- `market_context_high->crypto_major_4h` score `-0.5357` n `114` status `ready` deltaP `14.0752` edge `0.1115` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.5422` n `114` status `ready` deltaP `1.434` edge `0.0011` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
